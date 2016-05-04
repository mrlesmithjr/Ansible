#!/usr/bin/python
# vim: set encoding=utf-8:
# $Id: get_varnish_stats.py,v 1.5 2010/04/13 16:28:22 glen Exp $
# Author: Elan RuusamÃ¤e <glen@delfi.ee>
#
# Original varnish stat script by dmuntean from http://forums.cacti.net/viewtopic.php?t=31260
# Modified by glen to add support for new template: http://forums.cacti.net/viewtopic.php?p=182152
#

import re
import sys
import getopt
import os

opts, args = getopt.getopt(sys.argv[1:], "h:k:", ["host=", "key="])
host = '127.0.0.1'
key = '{{ cacti_conf_dir }}/.ssh/id_rsa'
for o, v in opts:
    if o in ("-h", "--host"):
        host = str(v)
    elif o in ("-k", "--key"):
        key = str(v)

out = os.popen('ssh -i' + key + ' -o StrictHostKeyChecking=no cacti@' + host +' /usr/bin/varnishstat -1 | grep -v "^MEMPOOL"').readlines()


# process results
split = re.compile('^\s*(?P<key>\S+)\s+(?P<value>\d+)\s+(?P<rest>.*)$')
for line in out:
        m = re.search(split, line);
        if m:
                print m.group('key') + ':' + m.group('value'),
print
