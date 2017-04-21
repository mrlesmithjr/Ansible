#! /usr/bin/env python

# macgen.py script to generate a MAC address for guests on Xen
#
mac_1 = 0x00
mac_2 = 0x16
mac_3 = 0x3e

import random
#
def randomMAC():
	mac = [ mac_1, mac_2, mac_3,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))
#
print randomMAC()
