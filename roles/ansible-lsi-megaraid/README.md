Role Name
=========

Manage LSI Controller logic devices. Ability to create new logic devices.

Requirements
------------

Identify controller(s), enclosure id(s) and slot(s) to configure. Host(s) require a reboot in order to discover newly created logic devices.

Role Variables
--------------

````
---
# defaults file for ansible-lsi-megaraid
megacli_bin: MegaCli64
megacli_config_logic_device:
  - name: ld0  #Bogus name for creating additional logic_devices
    controller: 0  #Should usually be 0 unless more than one controller exists.
    enclosure_id: 252  #enclosure id of enclose attached to controller
    raid_level: 5  #defines the raid-level to create...0,1,5,6,etc.
    slots:  #defines the slot(s) to use for creating the logic_deivce.
      - 0
      - 1
      - 2
      - 3
megacli_create_logic_devices: false  #defines if script should be executed in order to create logic_device(s) defined
megacli_path: /opt/MegaRAID/MegaCli
megacli_reboot_after_creation: false #defines if nodes should be rebooted after creation of logic devices
````

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        - install_lsi_megaraid_utils: true
        - megacli_config_logic_device:
            - name: ld1  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 3
            - name: ld2  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 4
            - name: ld3  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 5
            - name: ld4  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 6
            - name: ld5  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 7
            - name: ld6  #Bogus name for creating additional logic_devices
              controller: 0  #Should usually be 0 unless more than one controller exists.
              enclosure_id: 252  #enclosure id of enclose attached to controller
              raid_level: 0  #defines the raid-level to create...0,1,5,6,etc.
              slots:  #defines the slot(s) to use for creating the logic_deivce.
                - 8
        - megacli_create_logic_devices: true  #defines if script should be executed in order to create logic_device(s) defined
        - megacli_reboot_after_creation: true
      roles:
         - role: ansible-lsi-megaraid

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
