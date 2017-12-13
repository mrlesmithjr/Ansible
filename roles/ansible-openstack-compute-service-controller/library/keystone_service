#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: keystone_service
short_description: Manage OpenStack Identity (keystone) service endpoints
options:
  name:
    description:
        - name of service (e.g., keystone)
    required: yes
  type:
    description:
        - type of service (e.g., identity)
    required: yes
  description:
    description:
        - description of service (e.g., Identity Service)
    required: yes
  public_url:
    description:
        - public url of service.
        - 'Alias: I(url)'
        - 'Alias: I(publicurl)'
    required: yes
  internal_url:
    description:
        - internal url of service.
        - 'Alias: I(internalurl)'
    required: no
    default: value of public_url
  admin_url:
    description:
        - admin url of service.
        - 'Alias: I(adminurl)'
    required: no
    default: value of public_url
  insecure:
    description:
        - allow use of self-signed SSL certificates
    required: no
    choices: [ "yes", "no" ]
    default: no
  region:
    description:
        - region of service
    required: no
    default: RegionOne
  ignore_other_regions:
    description:
        - allow endpoint to exist in other regions
    required: no
    choices: [ "yes", "no" ]
    default: no
  state:
     description:
        - Indicate desired state of the resource
     choices: ['present', 'absent']
     default: present



requirements: [ python-keystoneclient ]
author: Lorin Hochstein
'''

EXAMPLES = '''
examples:
keystone_service: >
    name=keystone
    type=identity
    description="Keystone Identity Service"
    publicurl=http://192.168.206.130:5000/v2.0
    internalurl=http://192.168.206.130:5000/v2.0
    adminurl=http://192.168.206.130:35357/v2.0

keystone_service: >
    name=glance
    type=image
    description="Glance Identity Service"
    url=http://192.168.206.130:9292

'''

try:
    from keystoneclient.v2_0 import client
except ImportError:
    keystoneclient_found = False
else:
    keystoneclient_found = True

import traceback


def authenticate(endpoint, token, login_user, login_password, tenant_name,
                 insecure):
    """Return a keystone client object"""

    if token:
        return client.Client(endpoint=endpoint, token=token, insecure=insecure)
    else:
        return client.Client(auth_url=endpoint, username=login_user,
                             password=login_password, tenant_name=tenant_name,
                             insecure=insecure)


def get_service(keystone, name):
    """ Retrieve a service by name """
    services = [x for x in keystone.services.list() if x.name == name]
    count = len(services)
    if count == 0:
        raise KeyError("No keystone services with name %s" % name)
    elif count > 1:
        raise ValueError("%d services with name %s" % (count, name))
    else:
        return services[0]


def get_endpoint(keystone, name, region, ignore_other_regions):
    """ Retrieve a service endpoint by name """
    service = get_service(keystone, name)
    endpoints = [x for x in keystone.endpoints.list()
                   if x.service_id == service.id]

    # If this is a multi-region cloud only look at this region's endpoints
    if ignore_other_regions:
        endpoints = [x for x in endpoints if x.region == region]

    count = len(endpoints)
    if count == 0:
        raise KeyError("No keystone endpoints with service name %s" % name)
    elif count > 1:
        raise ValueError("%d endpoints with service name %s" % (count, name))
    else:
        return endpoints[0]


def ensure_present(keystone, name, service_type, description, public_url,
                   internal_url, admin_url, region, ignore_other_regions,
                   check_mode):
    """ Ensure the service and its endpoint are present and have the right values.

        Returns a tuple, where the first element is a boolean that indicates
        a state change, the second element is the service uuid (or None in
        check mode), and the third element is the endpoint uuid (or None in
        check mode)."""
    # Fetch service and endpoint, if they exist.
    service = None
    endpoint = None
    try: service = get_service(keystone, name)
    except KeyError: pass
    try: endpoint = get_endpoint(keystone, name, region, ignore_other_regions)
    except KeyError: pass

    changed = False

    # Delete endpoint if it exists and doesn't match.
    if endpoint is not None:
        identical = endpoint.publicurl == public_url and \
                    endpoint.adminurl == admin_url and \
                    endpoint.internalurl == internal_url and \
                    endpoint.region == region
        if not identical:
            changed = True
            ensure_endpoint_absent(keystone, name, check_mode, region,
                                   ignore_other_regions)
            endpoint = None

    # Delete service and its endpoint if the service exists and doesn't match.
    if service is not None:
        identical = service.name == name and \
                    service.type == service_type and \
                    service.description == description
        if not identical:
            changed = True
            ensure_endpoint_absent(keystone, name, check_mode, region,
                                   ignore_other_regions)
            endpoint = None
            ensure_service_absent(keystone, name, check_mode)
            service = None

    # Recreate service, if necessary.
    if service is None:
        if not check_mode:
            service = keystone.services.create(
                name=name,
                service_type=service_type,
                description=description,
            )
        changed = True

    # Recreate endpoint, if necessary.
    if endpoint is None:
        if not check_mode:
            endpoint = keystone.endpoints.create(
                region=region,
                service_id=service.id,
                publicurl=public_url,
                adminurl=admin_url,
                internalurl=internal_url,
            )
        changed = True

    if check_mode:
        # In check mode, the service/endpoint uuids will be the old uuids,
        # so omit them.
        return changed, None, None
    return changed, service.id, endpoint.id


def ensure_service_absent(keystone, name, check_mode):
    """ Ensure the service is absent"""
    try:
        service = get_service(keystone, name)
        endpoints = [x for x in keystone.endpoints.list()
                       if x.service_id == service.id]

        # Don't delete the service if it still has endpoints
        if endpoints:
            return False

        if not check_mode:
            keystone.services.delete(service.id)
        return True
    except KeyError:
        # Service doesn't exist, so we're done.
        return False


def ensure_endpoint_absent(keystone, name, check_mode, region,
                           ignore_other_regions):
    """ Ensure the service endpoint """
    try:
        endpoint = get_endpoint(keystone, name, region, ignore_other_regions)
        if not check_mode:
            keystone.endpoints.delete(endpoint.id)
        return True
    except KeyError:
        # Endpoint doesn't exist, so we're done.
        return False


def dispatch(keystone, name, service_type, description, public_url,
             internal_url, admin_url, region, ignore_other_regions, state,
             check_mode):

    if state == 'present':
        (changed, service_id, endpoint_id) = ensure_present(
            keystone,
            name,
            service_type,
            description,
            public_url,
            internal_url,
            admin_url,
            region,
            ignore_other_regions,
            check_mode,
        )
        return dict(changed=changed, service_id=service_id, endpoint_id=endpoint_id)
    elif state == 'absent':
        endpoint_changed = ensure_endpoint_absent(keystone, name, check_mode,
                                                  region, ignore_other_regions)
        service_changed = ensure_service_absent(keystone, name, check_mode)
        return dict(changed=service_changed or endpoint_changed)
    else:
        raise ValueError("Code should never reach here")



def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            type=dict(required=True),
            description=dict(required=False),
            public_url=dict(required=True, aliases=['url', 'publicurl']),
            internal_url=dict(required=False, aliases=['internalurl']),
            admin_url=dict(required=False, aliases=['adminurl']),
            region=dict(required=False, default='RegionOne'),
            ignore_other_regions=dict(required=False, default=False, type='bool'),
            state=dict(default='present', choices=['present', 'absent']),
            endpoint=dict(required=False,
                          default="http://127.0.0.1:35357/v2.0",
                          aliases=['auth_url']),
            token=dict(required=False),
            insecure=dict(required=False, default=False, type='bool'),

            login_user=dict(required=False),
            login_password=dict(required=False),
            tenant_name=dict(required=False, aliases=['tenant'])
        ),
        supports_check_mode=True,
        mutually_exclusive=[['token', 'login_user'],
                            ['token', 'login_password'],
                            ['token', 'tenant_name']]
    )

    endpoint = module.params['endpoint']
    token = module.params['token']
    login_user = module.params['login_user']
    login_password = module.params['login_password']
    tenant_name = module.params['tenant_name']
    insecure = module.boolean(module.params['insecure'])
    name = module.params['name']
    service_type = module.params['type']
    description = module.params['description']
    public_url = module.params['public_url']
    internal_url = module.params['internal_url']
    if internal_url is None:
        internal_url = public_url
    admin_url = module.params['admin_url']
    if admin_url is None:
        admin_url = public_url
    region = module.params['region']
    ignore_other_regions = module.boolean(module.params['ignore_other_regions'])
    state = module.params['state']

    keystone = authenticate(endpoint, token, login_user, login_password,
                            tenant_name, insecure)
    check_mode = module.check_mode

    try:
        d = dispatch(keystone, name, service_type, description,
                     public_url, internal_url, admin_url, region,
                     ignore_other_regions, state, check_mode)
    except Exception:
        if check_mode:
            # If we have a failure in check mode
            module.exit_json(changed=True,
                             msg="exception: %s" % traceback.format_exc())
        else:
            module.fail_json(msg=traceback.format_exc())
    else:
        module.exit_json(**d)


# this is magic, see lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
if __name__ == '__main__':
    main()
