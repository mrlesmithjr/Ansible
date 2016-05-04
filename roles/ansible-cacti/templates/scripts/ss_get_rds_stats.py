#!/usr/bin/env python
"""
Cacti script for polling Amazon RDS stats.

This program is part of Percona Monitoring Plugins
License: GPL License (see COPYING)

Author Roman Vynar
Copyright 2014 Percona LLC and/or its affiliates

$version = '1.1.4';
"""

import boto
import datetime
import fcntl
import optparse
import os
import pprint
import sys
import time
import traceback

def get_rds_info(indentifier=None):
    """Function for fetching RDS details"""
    rds = boto.connect_rds()
    try:
        if indentifier:
            info = rds.get_all_dbinstances(indentifier)[0]
        else:
            info = rds.get_all_dbinstances()
    except boto.exception.BotoServerError:
        info = None
    if not info:
        print 'Unable to get RDS details'
        sys.exit(1)
    return info

def get_rds_stats(db_ident, metric):
    """Function for fetching RDS statistics from CloudWatch"""
    cw = boto.connect_cloudwatch()
    result = cw.get_metric_statistics(300,
        datetime.datetime.utcnow() - datetime.timedelta(seconds=300),
        datetime.datetime.utcnow(),
        metric,
        'AWS/RDS',
        'Average',
        dimensions={'DBInstanceIdentifier': [db_ident]})
    debug('Result: %s' % result)
    if result:
        if metric in ('ReadLatency', 'WriteLatency'):
            # Transform into miliseconds
            result = '%.2f' % float(result[0]['Average'] * 1000)
        else:
            result = '%.2f' % float(result[0]['Average'])
    elif metric == 'ReplicaLag':
        # This metric can be missed
        result = 0
    else:
        print 'Unable to get RDS statistics'
        sys.exit(1)
    return float(result)

def debug(val):
    """Debugging output"""
    global options
    if options.debug:
        print 'DEBUG: %s' % val

def main():
    """Main function"""
    global options

    # DB instance classes as listed on http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html
    db_classes = {'db.t1.micro': 0.61,
                  'db.m1.small': 1.7,
                  'db.m1.medium': 3.75,
                  'db.m1.large': 7.5,
                  'db.m1.xlarge': 15,
                  'db.m2.xlarge': 17.1,
                  'db.m2.2xlarge': 34,
                  'db.m2.4xlarge': 68,
                  'db.cr1.8xlarge': 244}

    # RDS metrics as listed on http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/rds-metricscollected.html
    metrics = {'BinLogDiskUsage': 'binlog_disk_usage',  # The amount of disk space occupied by binary logs on the master.  Units: Bytes
               'CPUUtilization': 'utilization',  # The percentage of CPU utilization.  Units: Percent
               'DatabaseConnections': 'connections',  # The number of database connections in use.  Units: Count
               'DiskQueueDepth': 'disk_queue_depth',  # The number of outstanding IOs (read/write requests) waiting to access the disk.  Units: Count
               'ReplicaLag': 'replica_lag',  # The amount of time a Read Replica DB Instance lags behind the source DB Instance.  Units: Seconds
               'SwapUsage': 'swap_usage',  # The amount of swap space used on the DB Instance.  Units: Bytes
               'FreeableMemory': 'used_memory',  # The amount of available random access memory.  Units: Bytes
               'FreeStorageSpace': 'used_space',  # The amount of available storage space.  Units: Bytes
               'ReadIOPS': 'read_iops',  # The average number of disk I/O operations per second.  Units: Count/Second
               'WriteIOPS': 'write_iops',  # The average number of disk I/O operations per second.  Units: Count/Second
               'ReadLatency': 'read_latency',  # The average amount of time taken per disk I/O operation.  Units: Seconds
               'WriteLatency': 'write_latency',  # The average amount of time taken per disk I/O operation.  Units: Seconds
               'ReadThroughput': 'read_throughput',  # The average number of bytes read from disk per second.  Units: Bytes/Second
               'WriteThroughput': 'write_throughput'}  # The average number of bytes written to disk per second.  Units: Bytes/Second

    # Parse options
    parser = optparse.OptionParser()
    parser.add_option('-l', '--list', help='list DB instances',
                      action='store_true', default=False, dest='db_list')
    parser.add_option('-i', '--ident', help='DB instance identifier')
    parser.add_option('-p', '--print', help='print status and other details for a given DB instance',
                      action='store_true', default=False, dest='status')
    parser.add_option('-m', '--metric', help='metrics to retrive separated by comma: [%s]' % ', '.join(metrics.keys()))
    parser.add_option('-d', '--debug', help='enable debugging',
                      action='store_true', default=False)
    options, args = parser.parse_args()

    # Check args
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    elif options.db_list:
        info = get_rds_info()
        print 'List of all DB instances:'
        pprint.pprint(info)
        sys.exit()
    elif not options.ident:
        parser.print_help()
        parser.error('DB identifier is not set.')
    elif options.status:
        info = get_rds_info(options.ident)
        if info:
            pprint.pprint(vars(info))
        else:
            print 'No DB instance "%s" found on your AWS account.' % options.ident
        sys.exit()
    elif not options.metric:
        parser.print_help()
        parser.error('Metric is not set.')

    selected_metrics = options.metric.split(',')
    for metric in selected_metrics:
        if metric not in metrics.keys():
            parser.print_help()
            parser.error('Invalid metric.')

    # Do not remove the empty lines in the start and end of this docstring
    perl_magic_vars = """

    # Define the variables to output.  I use shortened variable names so maybe
    # it'll all fit in 1024 bytes for Cactid and Spine's benefit.  Strings must
    # have some non-hex characters (non a-f0-9) to avoid a Cacti bug.  This list
    # must come right after the word MAGIC_VARS_DEFINITIONS.  The Perl script
    # parses it and uses it as a Perl variable.
    $keys = array(
       'binlog_disk_usage'       =>  'gg',
       'utilization'             =>  'gh',
       'connections'             =>  'gi',
       'disk_queue_depth'        =>  'gj',
       'replica_lag'             =>  'gk',
       'swap_usage'              =>  'gl',
       'used_memory'             =>  'gm',
       'total_memory'            =>  'gn',
       'used_space'              =>  'go',
       'total_space'             =>  'gp',
       'read_iops'               =>  'gq',
       'write_iops'              =>  'gr',
       'read_latency'            =>  'gs',
       'write_latency'           =>  'gt',
       'read_throughput'         =>  'gu',
       'write_throughput'        =>  'gv',
    );

    """
    output = dict()
    for x in perl_magic_vars.split('\n'):
        if x.find('=>') >= 0:
            k = x.split(' => ')[0].strip().replace("'", '')
            v = x.split(' => ')[1].strip().replace("'", '').replace(',', '')
            output[k] = v
    debug('Perl magic vars: %s' % output)
    debug('Metric associations: %s' % dict((k, output[v]) for (k, v) in metrics.iteritems()))

    # Handle metrics
    results = []
    for metric in selected_metrics:
        stats = get_rds_stats(options.ident, metric)
        if metric == 'FreeableMemory':
            info = get_rds_info(options.ident)
            try:
                memory = db_classes[info.instance_class] * 1024 ** 3
            except:
                print 'Unknown DB instance class "%s"' % info.instance_class
                sys.exit(1)
            results.append('%s:%.0f' % (output['used_memory'], memory - stats))
            results.append('%s:%.0f' % (output['total_memory'], memory))
        elif metric == 'FreeStorageSpace':
            info = get_rds_info(options.ident)
            storage = float(info.allocated_storage) * 1024 ** 3
            results.append('%s:%.0f' % (output['used_space'], storage - stats))
            results.append('%s:%.0f' % (output['total_space'], storage))
        else:
            short_var = output.get(metrics[metric])
            if not short_var:
                print 'Chosen metric does not have a correspondent entry in perl magic vars'
                sys.exit(1)
            results.append('%s:%s' % (short_var, stats))

    print ' '.join(results)

if __name__ == '__main__':
    main()
