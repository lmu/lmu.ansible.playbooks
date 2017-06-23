===========================
CentOS Firewall (firewalld)
===========================

firewalld is the firewall service in CentOS/7, it replaces IP-Tables.

Zones
=====

Default Zones:

* public
* internal
* external
* home
* work
* dmz
* trusted
* drop
* block

Services
========

Default avaliable Services
--------------------------

Active:

* ssh
* dhcpv6-client

Avaliable / Useful:

* high-availability
* http
* https
* imap
* imaps
* smtp
* smtps
* kerberos
* ldap
* ldaps
* mosh
* mountd
* nfs
* ntp
* postgresql
* mysql
* puppetmaster
* radius
* rsyncd
* samba
* samba-client
* snmp
* snmptrap
* squid
* syslog
* syslog-tls

How to add new Services
-----------------------

Add a <service>.xml in folder ``/etc/firewalld/services/``

For example it would be useful to have:

* check_mk-agent
* varnish
* supervisor
* psdash
