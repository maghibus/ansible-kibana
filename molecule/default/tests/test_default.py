import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kibana_running_and_enabled(host):
    kibana = host.service("kibana")
    assert kibana.is_running
    assert kibana.is_enabled
