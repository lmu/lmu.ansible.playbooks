#!/usr/bin/env python3

# This scripts generates a CMDB-like Overview of all Ansible managed Servers via ansible-cmdb

import json
import os.path
import shutil
import subprocess

from os import listdir
from os import makedirs
from os.path import isdir
from os.path import isfile


def execute_ansible_setup(
        inventory='/opt/lmu.ansible.playbooks/inventory-avaliable',
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
    print(command_set)
    return subprocess.call(command_set)


def check_and_copy_ansible_setup_output(
        input_directory='/opt/lmu.ansible.playbooks/unchecked-out/',
        output_directory='/opt/lmu.ansible.playbooks/checked-out/'):
    if isdir(input_directory) and isdir(output_directory):
        for server_file in listdir(input_directory):
            if isfile(os.path.join(input_directory, server_file)):
                with open(os.path.join(input_directory, server_file), 'r') as f:
                        print("check File: " + input_directory + server_file)
                        data = json.load(f)
                        #import pdb; pdb.set_trace()
                        # if isfile(os.path.join(output_directory, server_file)):
                        #    print("delete file: " + server_file)
                        #    os.remove(
                        #        os.path.join(output_directory, server_file),
                        #    )
                        if 'unreachable' not in data:
                            print("write file: " + output_directory + server_file)
                            shutil.copyfile(
                                os.path.join(
                                    input_directory,
                                    server_file,
                                ),
                                os.path.join(
                                    output_directory,
                                    server_file,
                                )
                            )
                        else:
                            print("check failed, file not created: " + server_file + " : " + str(data))


def execute_ansible_cmdb(
        inventory='/opt/lmu.ansible.playbooks/inventory-avaliable',
        fact_directory='/opt/lmu.ansible.playbooks/checked-out/',
        output_file='/opt/lmu.ansible.playbooks/cmdb/index.html'):
    """
    /opt/dev-tools/ansible-cmdb/.venv/bin/ansible-cmdb -i /opt/lmu.ansible.playbooks/inventory /opt/lmu.ansible.playbooks/checked-out/ > /opt/lmu.ansible.playbooks/cmdb/index.html
    """
    command_set = ['/opt/dev-tools/ansible-cmdb/.venv/bin/ansible-cmdb']
    if inventory:
        command_set.extend(['-i', inventory])
    if fact_directory:
        command_set.append(fact_directory)
    try:
        cmdb_data = subprocess.check_output(command_set)

        if output_file:
            with open(output_file, 'w') as f:
                print("write Data to file: " + output_file)
                f.write(cmdb_data)
    except Exception as e:
        print(e)


def ensure_directories_exsists(
    dirs=[
        '/opt/lmu.ansible.playbooks/inventory-avaliable',
        '/opt/lmu.ansible.playbooks/cmdb/',
        '/opt/lmu.ansible.playbooks/unchecked-out/',
        '/opt/lmu.ansible.playbooks/checked-out/']):
    for dir in dirs:
        if not os.path.exists(dir):
            makedirs(dir)


if __name__ == "__main__":
    print("Ensure Directories exists")
    ensure_directories_exsists()
    print("Collect facts")
    execute_ansible_setup()
    print("Copy Files")
    check_and_copy_ansible_setup_output()
    print("generate CMDB Overview")
    execute_ansible_cmdb()
