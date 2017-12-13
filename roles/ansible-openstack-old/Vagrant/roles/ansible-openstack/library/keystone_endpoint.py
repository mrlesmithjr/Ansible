#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Davide Guerri <davide.guerri@gmail.com>
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Based on Lorin Hochstein keystone_user module
# keystone_user module is based on Jimmy Tang's implementation


DOCUMENTATION = '''
---
module: keystone_endpoint
short_description: Manage OpenStack Identity (keystone) endpoints
description:
   - Manage endpoints from OpenStack.
options:
   login_user:
     description:
        - login username to authenticate to keystone
     required: false
     default: None
   login_password:
     description:
        - Password of login user
     required: false
     default: None
   login_tenant_name:
     description:
        - The tenant login_user belongs to
     required: false
     default: None
   service_name:
     description:
        - OpenStack service name (e.g. keystone)
     required: true
   region:
     description:
        - OpenStack region to which endpoint will be added
     required: false
     default: 'RegionOne'
   public_url:
     description:
        - Public endpoint URL
     required: true
   internal_url:
     description:
        - Internal endpoint URL
     required: false
     default: None
   admin_url:
     description:
        - Admin endpoint URL
     required: false
     default: None
   token:
     description:
        - The token to be uses in case the password is not specified
     required: false
     default: None
   endpoint:
     description:
        - The keystone url for authentication
     required: false
     default: 'http://127.0.0.1:35357/v2.0/'
   state:
     description:
        - Indicate desired state of the resource
     choices: ['present', 'absent']
     default: present
requirements: [ python-keystoneclient ]
author: Davide Guerri
'''

EXAMPLES = '''
# Create a Glance endpoint in region aw1
- name: Create Glance endpoints
  keystone_endpoint: >
    service_name="glance"
    region="aw1"
    public_url="https://glance.aw1.bigcompany.com/"
    internal_url="http://glance-aw1.internal:9292/"
    admin_url="https://glance.aw1.bigcompany.com/"
    endpoint="http://keystone-aw1.internal.com:35357/v2.0"
    token="my secret token"
    state=present

# Delete a Keystone endpoint in region aw2
- name: Delete Glance endpoints
  keystone_endpoint: >
    service_name="glance"
    region="aw2"
    public_url="https://glance.aw1.bigcompany.com/"
    internal_url="http://glance-aw1.internal:9292/"
    admin_url="https://glance.aw1.bigcompany.com/"
    endpoint="http://keystone-aw1.internal.com:35357/v2.0"
    token="my secret token"
    state="absent"
'''

try:
    from keystoneclient.v2_0 import client
except ImportError:
    keystoneclient_found = False
else:
    keystoneclient_found = True


def authenticate(endpoint, token, login_user, login_password,
                 login_tenant_name):
    """Return a keystone client object"""

    if token:
        return client.Client(endpoint=endpoint, token=token)
    else:
        return client.Client(auth_url=endpoint, username=login_user,
                             password=login_password,
                             tenant_name=login_tenant_name)


def endpoint_match(endpoint, service_id, region, public_url, internal_url,
                   admin_url):
    return endpoint.service_id == service_id and \
           endpoint.region == region and \
           endpoint.publicurl == public_url and \
           getattr(endpoint, 'internalurl') == internal_url and \
           getattr(endpoint, 'adminurl') == admin_url


def get_service(keystone, service_name):
    """ Retrieve a service by name"""
    services = [x for x in keystone.services.list() if x.name == service_name]
    count = len(services)
    if count == 0:
        raise KeyError("No keystone services with name %s" % service_name)
    elif count > 1:
        raise ValueError("%d services with name %s" % (count, service_name))
    else:
        return services[0]


def endpoint_exists(keystone, service_id, region, public_url, internal_url,
                    admin_url):
    """ Return True if endpoint already exists"""
    endpoints = [x for x in keystone.endpoints.list() if
                 endpoint_match(x, service_id, region, public_url, internal_url,
                                admin_url)]

    return any(endpoints)


def get_endpoint(keystone, service_id, region, public_url, internal_url,
                 admin_url):
    """ Retrieve an endpoint by name"""
    endpoints = [x for x in keystone.endpoints.list() if
                 endpoint_match(x, service_id, region, public_url, internal_url,
                                admin_url)]
    count = len(endpoints)
    if count == 0:
        raise KeyError(
            "No keystone endpoint with service id: %s, region: %s, public_url: "
            "%s, internal_url: %s, admin_url: %s" % (
                service_id, region, public_url, internal_url, admin_url))
    elif count > 1:
        # Should never be reached as Keystone ensure endpoints to be unique
        raise ValueError(
            "%d services with service id: %s, region: %s, public_url: %s, "
            "internal_url: %s, admin_url: %s" % (
                count, service_id, region, public_url, internal_url, admin_url))
    else:
        return endpoints[0]


def get_endpoint_id(keystone, service_name, region, public_url,
                    internal_url, admin_url, check_mode):
    return get_endpoint(keystone, service_name, region, public_url,
                        internal_url, admin_url, check_mode).id


def ensure_endpoint_exists(keystone, service_name, region, public_url,
                           internal_url, admin_url, check_mode):
    """ Ensure that an endpoint exists.

        Return (True, id) if a new endpoint was created, (False, None) if it
        already existed.
    """

    # Check if endpoint already exists
    service_id = get_service(keystone, service_name).id
    try:
        endpoint = get_endpoint(keystone=keystone, service_id=service_id,
                                region=region, public_url=public_url,
                                internal_url=internal_url, admin_url=admin_url)
    except KeyError:
        # endpoint doesn't exist yet
        pass
    else:
        return False, endpoint.id

    # We now know we will have to create a new service
    if check_mode:
        return True, None

    ks_service = keystone.endpoints.create(service_id=service_id,
                                           region=region,
                                           publicurl=public_url,
                                           internalurl=internal_url,
                                           adminurl=admin_url)
    return True, ks_service.id


def ensure_endpoint_absent(keystone, service_name, region, public_url,
                           internal_url, admin_url, check_mode):
    """ Ensure that an endpoint does not exist

         Return True if the endpoint was removed, False if it didn't exist
         in the first place
    """
    service_id = get_service(service_name).id
    if not endpoint_exists(keystone=keystone, service_id=service_id,
                           region=region, public_url=public_url,
                           internal_url=internal_url, admin_url=admin_url):
        return False

    # We now know we will have to delete the tenant
    if check_mode:
        return True

    endpoint = get_endpoint(keystone=keystone, service_id=service_id,
                            region=region, public_url=public_url,
                            internal_url=internal_url, admin_url=admin_url)
    keystone.endpoints.delete(endpoint.id)


def main():
    argument_spec = openstack_argument_spec()
    argument_spec.update(dict(
        service_name=dict(required=True),
        region=dict(false=True, default="RegionOne"),
        public_url=dict(required=True),
        internal_url=dict(required=False, default=None),
        admin_url=dict(required=False, default=None),
        state=dict(default='present', choices=['present', 'absent']),
        endpoint=dict(required=False, default="http://127.0.0.1:35357/v2.0"),
        token=dict(required=False),
        login_user=dict(required=False),
        login_password=dict(required=False),
        login_tenant_name=dict(required=False)
    ))
    # keystone operations themselves take an endpoint, not a keystone auth_url
    del (argument_spec['auth_url'])
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[['token', 'login_user'],
                            ['token', 'login_password'],
                            ['token', 'login_tenant_name']]
    )

    if not keystoneclient_found:
        module.fail_json(msg="the python-keystoneclient module is required")

    service_name = module.params['service_name']
    region = module.params['region']
    public_url = module.params['public_url']
    internal_url = module.params['internal_url']
    admin_url = module.params['admin_url']
    state = module.params['state']
    endpoint = module.params['endpoint']
    token = module.params['token']
    login_user = module.params['login_user']
    login_password = module.params['login_password']
    login_tenant_name = module.params['login_tenant_name']

    keystone = authenticate(endpoint=endpoint, token=token,
                            login_user=login_user,
                            login_password=login_password,
                            login_tenant_name=login_tenant_name)

    check_mode = module.check_mode

    id = None
    try:
        if state == "present":
            changed, id = ensure_endpoint_exists(keystone=keystone,
                                                 service_name=service_name,
                                                 region=region,
                                                 public_url=public_url,
                                                 internal_url=internal_url,
                                                 admin_url=admin_url,
                                                 check_mode=check_mode)
        elif state == "absent":
            changed = ensure_endpoint_absent(keystone=keystone,
                                             service_name=service_name,
                                             region=region,
                                             public_url=public_url,
                                             internal_url=internal_url,
                                             admin_url=admin_url,
                                             check_mode=check_mode)
        else:
            # Invalid state
            raise ValueError("Invalid state %s" % state)
    except Exception, e:
        if check_mode:
            # If we have a failure in check mode
            module.exit_json(changed=True,
                             msg="exception: %s" % e)
        else:
            module.fail_json(msg="exception: %s" % e)
    else:
        module.exit_json(changed=changed, id=id)


# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.openstack import *

if __name__ == '__main__':
    main()
