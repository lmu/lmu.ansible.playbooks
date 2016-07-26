#!/usr/bin/env python
"""Helper Module for Ansible Playbooks to set known_hosts."""

from __future__ import print_function

import csv
import os


def check_fs_is_readonly():

    fs_table = {}
    if os.path.exists('proc/mounts'):
        with open('/proc/mounts', 'rb+') as f:
            for line in f:
                device, mount_point, filesystem, flags, uid, gid = line.split()
                if mount_point in ['/', '/var', '/data', '/backup']:
                    options = flags.split(',')
                    if 'ro' in options:
                        return True

    return False

if __name__ == '__main__':
    if check_fs_is_readonly():
        print("system will restart now due to invalid filesysteme state for operations")
        exec('reboot')
