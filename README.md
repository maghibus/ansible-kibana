ansible-kibana
=========

[![Build Status](https://travis-ci.com/maghibus/ansible-kibana.svg?branch=master)](https://travis-ci.com/maghibus/ansible-kibana)

An Ansible Role that installs Kibana on RedHat/CentOS.


Role Variables
--------------
Available variables are listed below, along with default values (see `defaults/main.yml` and `vars/main.yml` ):

The version of kibana to install

    repo_name: "6.x"
    kibana_version: "6.2.4"
    allow_downgrades: true
    use_repository: true
    package_name: kibana

Kibana configuration
    
    elasticsearch_url: "http://localhost:9200"
    server_host: 0.0.0.0
    server_port: 5601
    user: kibana
    group: kibana

SSL configuration
    
    ssl_dir: "/etc/kibana"
    ssl_certificate_file: ""
    ssl_key_file: "

Authentication

    basic_auth: false
    elasticsearch_username: ""
    elasticsearch_password: ""
    
Default directories

    logging_dir: "/var/log/kibana"
    logging_dest: "{{logging_dir}}/kibana.log"
    conf_dir: "/etc/kibana"


Variables
    
    package_url: "https://artifacts.elastic.co/downloads/kibana/kibana"
    sysd_script: "/usr/lib/systemd/system/kibana.service"
    init_script: "/etc/init.d/kibana"
    default_file: "/etc/sysconfig/kibana"
    kibana_home: "/usr/share/kibana"                             



Dependencies
------------

None

Example Playbook
----------------

    - hosts: kibana
      roles:
        - ansible-kibana
      vars:
        elasticsearch_url: "http://localhost:9200"
        server_host: "localhost"
        kibana_version: 6.2.4                       


Install Kibana
----------------

	$ ansible-playbook -u user -i inventory inventory.yml --tags "install"


Remove Kibana
----------------
	$ ansible-playbook -u user -i inventory inventory.yml --tags "remove"

License
-------

MIT, BSD

Author Information
------------------

This role was created in 2018 by Francesco Salvatore
