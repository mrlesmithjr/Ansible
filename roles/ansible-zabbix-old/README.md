#Readme
This ansible role deploys zabbix server and/or Zabbix agent for Ubuntu 12.04 (tested on vagrant)

##Prerequisite
* Having ansible installed on your workstation. 
* Having a DB postgresql or mysql server

##How to install
* Use github to clone/fork in your role directory
* *Note:* if you intend to install database I would recommend to use one of the following
  * ```ansible-galaxy install ANXS.postgresql```
  * ```ansible-galaxy install ANXS.mysql```

## Design
With Zabbix it is easy to change from one design to another, at least in theory. I am not going to cover the design here only the basics.
Zabbix  has the following component
* Database (This playbook support postgresql and mysql(experimental) )
* Zabbix Server or Zabbix Proxy server
* Zabbix Frontend (Apache2 and php)
* Zabbix agent (Will be installed by default)
* Zabbix Java gateway (currently not supported)

### Types of zabbix server Installation
1. Standalone
2. Distributed
3. HA (not supported) 

### Types of zabbix agent
1. Just an agent :)

### Server Standalone
TODO

### Server Distributed
 TODO
 
##Run
    
  ```ansible-playbook -l hostname zabbix_server_postgresql.yml```
