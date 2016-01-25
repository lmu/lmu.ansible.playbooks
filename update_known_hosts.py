#!/usr/bin/env python
"""Helper Module for Ansible Playbooks to set known_hosts."""

from __future__ import print_function

import subprocess
import StringIO


if __name__ == '__main__':
    hosts = subprocess.check_output(['ansible', 'all', '--list-hosts'])

    for host in hosts.split():
        try:
            subprocess.check_call(['ssh-keyscan', '-H', host],
                                  stdout=None,
                                  stderr=None)
        except subprocess.CalledProcessError as e:
            print(e)
        except:
            # import ipdb; ipdb.set_trace()
            pass
