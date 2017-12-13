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
module: keystone_service
short_description: Manage OpenStack Identity (keystone) services
description:
   - Manage OpenStack services.
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
   name:
     description:
        - OpenStack service name (e.g. keystone)
     required: true
   service_type:
     description:
        - OpenStack service type (e.g. identity)
     required: true
   description:
     description:
        - Service description
     required: false
     default: Not provided
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
# Add Glance service
- name: Create Glance service
  keystone_service: >
    name=glance
    service_type=image
    description="Glance image service"
    endpoint="http://keystone-aw1.internal.com:35357/v2.0"
    token="my secret token"
    state=present

# Delete Glance service
- name: Delete Glance service
  keystone_service: >
    name=glance
    service_type=image
    description="Glance image service"
    endpoint="http://keystone-aw1.internal.com:35357/v2.0"
    token="my secret token"
    state=absent
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


def service_exists(keystone, service_name):
    """ Return True if service already exists"""
    return service_name in [x.name for x in keystone.services.list()]


def get_service(keystone, service_name):
    """ Retrieve a service by name"""
    services = [x for x in keystone.services.list() if x.name == service_name]
    count = len(services)
    if count == 0:
        raise KeyError("No keystone services with name %s" % service_name)
    elif count > 1:
        # Should never be reached as Keystone ensure service names to be unique
        raise ValueError("%d services with name %s" % (count, service_name))
    else:
        return services[0]


def get_service_id(keystone, service_name):
    return get_service(keystone, service_name).id


def ensure_service_exists(keystone, service_name, service_type,
                          service_description, check_mode):
    """ Ensure that a service exists.

        Return (True, id) if a new service was created, (False, None) if it
        already existed.
    """

    # Check if service already exists
    try:
        service = get_service(keystone=keystone, service_name=service_name)
    except KeyError:
        # Service doesn't exist yet
        pass
    else:
        return False, service.id

    # We now know we will have to create a new service
    if check_mode:
        return True, None

    ks_service = keystone.services.create(name=service_name,
                                          service_type=service_type,
                                          description=service_description)
    return True, ks_service.id


def ensure_service_absent(keystone, service_name, check_mode):
    """ Ensure that a service does not exist

         Return True if the service was removed, False if it didn't exist
         in the first place
    """
    if not service_exists(keystone=keystone, service_name=service_name):
        return False

    # We now know we will have to delete the service
    if check_mode:
        return True

    service = get_service(keystone=keystone, service_name=service_name)
    keystone.services.delete(service.id)


def main():
    argument_spec = openstack_argument_spec()
    argument_spec.update(dict(
        name=dict(required=True),
        service_type=dict(required=True),
        description=dict(required=False, default="Not provided"),
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

    service_name = module.params['name']
    service_type = module.params['service_type']
    service_description = module.params['description']
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
            changed, id = ensure_service_exists(
                keystone=keystone,
                service_name=service_name,
                service_type=service_type,
                service_description=service_description,
                check_mode=check_mode)
        elif state == "absent":
            changed = ensure_service_absent(keystone=keystone,
                                            service_name=service_name,
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
