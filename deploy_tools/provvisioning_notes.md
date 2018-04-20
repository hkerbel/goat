Provisioning a new site
=======================

## required packages:

* ngingx
* Python 3.6
* virtualenv + pip
* Git

On CentOS 7:
    1 - Update system.
    sudo yum -y update
    sudo yum -y install yum-utils
    sudo yum -y groupinstall development

    2 - IUS repository.
    sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

    3 - Python 3.6 & pip
    sudo yum -y install python36u
    sudo yum -y install python36u-pip
    sudo yum -y install python36u-devel

## Nginx Virtual Host config

* see nginx.template.conf
* replace the literal DOMAIN with, for example, staging.my-domain.com

## Folder structure:

/var/local/
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
         