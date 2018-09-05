#!/usr/bin/env python

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback.default import CallbackModule

class AnsibleInventory(InventoryManager):
    def __init__(self, inventory_info, group_vars, loader):
        super(AnsibleInventory, self).__init__(loader)
        self.inventory_info = inventory_info
        self.group_vars = group_vars
        self.loader = loader

    def set_inventory(self):
        pass

class Options(object):
    def __init__(self, connection='ssh', forks=10, listtags=False, listtasks=False, listhosts=False, syntax=False,
                 ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=False, become_method=None,
                 become_user=None, verbosity=None, check=False, diff=False, host_key_checking=False, module_path=None,
                 remote_user=None, private_key_file=None, ssh_common_args=None):
        self.connection = connection
        self.forks = forks
        self.listtags = listtags
        self.listtasks = listtasks
        self.listhosts = listhosts
        self.syntax = syntax
        self.ssh_extra_args = ssh_extra_args
        self.sftp_extra_args = sftp_extra_args
        self.scp_extra_args = scp_extra_args
        self.become = become
        self.become_method = become_method
        self.become_user = become_user
        self.verbosity = verbosity
        self.check = check
        self.diff = diff
        self.host_key_checking = host_key_checking
        self.module_path = module_path
        self.remote_user = remote_user
        self.private_key_file = private_key_file
        self.ssh_common_args = ssh_common_args


class ResultCallback(CallbackModule):
    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.ok = {}
        self.failed = {}
        self.unreachable = {}

    def v2_runner_on_ok(self, result):
        self.ok[result._host.get_name()] = result
        super(ResultCallback, self).v2_runner_on_ok(result)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.failed[result._host.get_name()] = self._dump_results(result._result)
        super(ResultCallback, self).v2_runner_on_failed(result, ignore_errors=False)

    def v2_runner_on_unreachable(self, result):
        self.unreachable[result._host.get_name()] = result
        super(ResultCallback, self).v2_runner_on_unreachable(result)


class Playbook(object):
    def __init__(self, hosts='/path/to/hosts', playbooks=['/path/to/playbook']):
        self.playbooks = playbooks
        self.loader = DataLoader()
        # self.inventory = AnsibleInventory(inventory_info, self.loader)
        self.inventory = InventoryManager(self.loader, hosts)
        self.options = Options(connection='ssh', forks=10)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        self.callback = ResultCallback()

    def run(self):
        pbex = PlaybookExecutor(playbooks=self.playbooks,
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            options=self.options,
            loader=self.loader,
            passwords={})
        pbex._tqm._stdout_callback = self.callback
        pbex.run()


def main():
    hosts = './hosts'
    playbooks = ['./test.yml']
    pb = Playbook(hosts=hosts, playbooks=playbooks)
    pb.run()

if __name__ == "__main__":
    main()
