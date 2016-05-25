#!/usr/bin/env python
"""Helper Module for Ansible Playbooks to set known_hosts."""

from __future__ import print_function

import subprocess
import StringIO


if __name__ == '__main__':
    hosts = subprocess.check_output(['ansible', 'all', '--list-hosts'])

    hosts = hosts.splitlines()
    if hosts[0].strip().startswith('hosts'):
        hosts = hosts[1:]

    for host in hosts:
        try:
            subprocess.check_call(['ssh-copy-id', 'fachadmin' + host.strip()])
        except subprocess.CalledProcessError as e:
            print(e)
        except:
            # import ipdb; ipdb.set_trace()
            pass
