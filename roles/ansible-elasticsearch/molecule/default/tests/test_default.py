import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_is_running(host):
    elasticsearch = host.service('elasticsearch')

    assert elasticsearch.is_running
    assert elasticsearch.is_enabled
