Vagrant Environment
===================

The Vagrant environment consists of the following nodes:  
client - run code from  
logstash
oscompute  
oscontroller  
oshaproxy  



Spin up environment
````
vagrant up
````

After all nodes are spun up connect to the client machine in order to provision all of the nodes.
````
vagrant ssh client
cd /vagrant
ansible-playbook -i hosts openstack.yml --user vagrant
````

Log into Horizon Dashboard  
http://127.0.0.1:8080/horizon  
user: admin  
password: 29b1416692cb38014ea0  

or ...

user: demo  
password: 54a27efd264beeb7843d  

When you are done and ready to tear down the environment.  
````
./cleanup.sh
````
