#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
import subprocess
import sys


def gen_new_key_req_pair(hostname, domain='verwaltung.uni-muenchen.de', key_length=4096, ou='VI', days=365):
    print("Generate Private Key and Request")
    subprocess.call([
        'openssl',
        'req',
        '-new',
        '-newkey',
        'rsa:'+str(key_length),
        '-subj',
        '/C=DE/ST=Bayern/L=Muenchen/O=Ludwig-Maximilians-Universitaet Muenchen/OU=' + ou + '/CN=' + hostname + "." + domain,
        '-nodes',
        '-days',
        str(days),
        '-keyout',
        'server-ssl/key/' + hostname + "." + domain + '_key.pem',
        '-out',
        'server-ssl/req/' + hostname + "." + domain + '_req.pem'
    ])
    print("key generated")
    print("generate intermediate crt")
    subprocess.call([
        'openssl',
        'x509',
        '-req',
        '-sha256',
        '-days',
        str(days),
        '-in',
        'server-ssl/req/' + hostname + "." + domain + '_req.pem',
        '-signkey',
        'server-ssl/key/' + hostname + "." + domain + '_key.pem',
        '-out',
        'server-ssl/crt/' + hostname + "." + domain + '_crt.pem'
    ])


def gen_new_req_from_key(hostname, domain='verwaltung.uni-muenchen.de', key_length=4096, ou='VI'):
    pass


def show_key(arg):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Interenes Script um einfacher Keys und Key-Signing-Requests für SSL Zetrifikate zu erzeugen.")
    parser.add_argument('hostname', type=str, help='Hostname / DNS-Name for which this Request is.')
    parser.add_argument('--domain', type=str, help='Domain of the Host (default: ".verwaltung.uni-muenchen.de")', required=False, default='.verwaltung.uni-muenchen.de')
    parser.add_argument('--ou', type=str, help='Organisation Unit (default: "VI")', required=False, default='VI')
    parser.add_argument('--key_length', type=int, help='Key Length for RSA-Key (default: 4096)', required=False, default=4096)
    parser.add_argument('--days', type=int, help='Days for Cert', required=False, default=365)

    parser.add_argument('--show')

    args = parser.parse_args()
    print(args.__dict__)
    if args.show:
        show_key(args.hostname)
    else:
        gen_new_key_req_pair(args.hostname, domain=args.domain, key_length=args.key_length, ou=args.ou, days=args.days)
