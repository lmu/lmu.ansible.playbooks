#!/usr/bin/env python

# This scripts generates a CMDB-like Overview of all Ansible managed Servers via ansible-cmdb

import json
import os.path
import shutil
import subprocess

from os import listdir
from os.path import isdir
from os.path import isfile


def execute_ansible_setup(
        inventory='/opt/lmu.ansible.playbooks/inventory',
        scope='all',
        limit=[],
        user='ansible',
        key='/home/fachadmin/.ssh/id_rsa',
        out_directory='/opt/lmu.ansible.playbooks/unchecked-out/'):
    """
    """
    command_set = ['ansible', '-m', 'setup']
    if user:
        command_set.extend(['-u', user])
    if inventory:
        command_set.extend(['-i', inventory])
    if limit:
        command_set.append('--limit=' + ','.join(limit))
    if out_directory:
        command_set.extend(['--tree', out_directory])
    if key:
        command_set.append('--private-key=' + key)
    if scope:
        command_set.append(scope)
    else:
        command_set.append('all')
    return subprocess.call(command_set)


def check_and_copy_ansible_setup_output(
        input_directory='/opt/lmu.ansible.playbooks/unchecked-out/',
        output_directory='/opt/lmu.ansible.playbooks/checked-out/'):
    if isdir(input_directory) and isdir(output_directory):
        for server_file in listdir(input_directory):
            if isfile(os.path.join(input_directory, server_file)):
                with open(os.path.join(input_directory, server_file), 'r') as f:
                        data = json.load(f)
                        #import pdb; pdb.set_trace()
                        if 'unreachable' not in data:
                            shutil.copy2(os.path.join(input_directory, server_file), output_directory)


def execute_ansible_cmdb(
        inventory='/opt/lmu.ansible.playbooks/inventory',
        fact_directory='/opt/lmu.ansible.playbooks/checked-out/',
        output_file='/opt/lmu.ansible.playbooks/cmdb/index.html'):
    """
    ansible-cmdb -i /opt/lmu.ansible.playbooks/inventory /opt/lmu.ansible.playbooks/checked-out/ > /opt/lmu.ansible.playbooks/cmdb/index.html
    """
    command_set = ['ansible-cmdb']
    if inventory:
        command_set.extend(['-i', inventory])
    if fact_directory:
        command_set.append(fact_directory)
    cmdb_data = subprocess.check_output(command_set)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(cmdb_data)

if __name__ == "__main__":
    execute_ansible_setup()
    check_and_copy_ansible_setup_output()
    execute_ansible_cmdb()
