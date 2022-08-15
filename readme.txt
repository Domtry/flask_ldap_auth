execute this script for install ldap container from docker
>> docker run -p 389:389 -p 636:636 --name my-openldap-container --detach osixia/openldap:1.2.4