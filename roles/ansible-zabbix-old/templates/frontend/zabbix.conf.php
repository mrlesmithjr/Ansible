<?php
//{{ ansible_managed }}
// Zabbix GUI configuration file
global $DB;

$DB['TYPE']     = '{{ zabbix_php_db}}';
$DB['SERVER']   = '{{ zabbix_server_db_host }}';
$DB['PORT']     = '{{ zabbix_server_db_port }}';
$DB['DATABASE'] = '{{ zabbix_server_db_name }}';
$DB['USER']     = '{{ zabbix_server_db_user }}';
$DB['PASSWORD'] = '{{ zabbix_server_db_pass }}';

// SCHEMA is relevant only for IBM_DB2 database
$DB['SCHEMA'] = '';

$ZBX_SERVER      = '{{ zabbix_server_host }}';
$ZBX_SERVER_PORT = '{{ zabbix_server_port }}';
$ZBX_SERVER_NAME = '{{ zabbix_server_name }}';

$IMAGE_FORMAT_DEFAULT = IMAGE_FORMAT_PNG;
?>

