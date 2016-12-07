=============================================
LMU Ansible Playbooks (lmu.ansible.playbooks)
=============================================

Introduction
============



Preconditions & Requirements
============================




Install ansible & lmu.ansible.playbooks
---------------------------------------


Install lmu.ansible_roles and external dependencies
---------------------------------------------------

Run ``ansible-galaxy -p roles -r requirements.yml install`` to install required roles;


A Set of Ansible Playbooks used at LMU IT Department to setup several maschines for different Services.

Services
========

* Plone
* Redmine
* Sentry
* Open Monitoring Distribution (OMD)

  * Nagios
  * NagViz
  * Check_mk

* Piwik
* Solr
* Dashing
* Jenkins
* The Foreman

Roles
=====

At the moment this repository contains a set of roles, those should be moved into own repositories.

necessary roles should be installed by


Documentation
=============

For a detailed documentation please refere to the docs folder.

License
=======

BSD-3-Clause
