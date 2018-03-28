#!/usr/bin/env python2.7

from datetime import datetime, timedelta

import boto.ec2
conn = boto.ec2.connect_to_region("eu-west-1")
keyname = "veronica-sa-ie"
project = "Veronica Ops Manager Demo"

opsmanager = ""
replica_set = []

for r in conn.get_all_reservations(filters={"tag:project" : project}):
  for instance in r.instances:
    #print instance.public_dns_name + " " + instance.state + " " + instance.key_name + " " + instance.instance_type + " " + instance.tags['Name']
    if instance.key_name == keyname and instance.state == "running":
      if instance.instance_type == "m3.xlarge":
      	  opsmanager = instance.public_dns_name
      else:
          replica_set.append(instance.public_dns_name)

f = open('./hosts', 'a')
f.write('[opsManager]\n')
f.write(opsmanager + " ansible_user=ec2-user\n")
f.write("\n")
f.write("[opsManager:vars]\n")
f.write("opsmanagerurl=http://" + opsmanager + ":8080\n")
f.write("\n")
f.write("[ReplicaSet]\n")
for machine in replica_set:
  f.write(machine + " ansible_user=ec2-user\n")
f.write("\n")
f.write("[ReplicaSet:vars]\n")
f.write("opsmanagerurl=http://" + opsmanager + ":8080\n")
f.write("opsmanager=" + opsmanager + "\n")
f.close()

#print 'Written ./hosts'
