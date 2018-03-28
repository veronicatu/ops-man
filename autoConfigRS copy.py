import argparse
from pprint import pprint
import json
import ConfigParser

config = ConfigParser.ConfigParser()
try:
    config.read("../hosts")
except Exception as e:
    print 'Something went bad when opening hosts file', e.value


#retrieve hostnames
options = config.options("ReplicaSet")
hosts = [item.split(" ")[0] for item in options ]

# retrieve relpica set name and the port numbers for the mongod processes
rs_name = config.get("local:vars", "rs_name")
ports = config.get("local:vars", "rs_mongod_ports")
ports = ports.split(" ")

# the configuration file use to create the replica set with Ops Manager
templateDoc = {
    "options": {
        "downloadBase": "/var/lib/mongodb-mms-automation",
        "downloadBaseWindows": "C:\\MMSAutomation\\versions"
    },
    "mongoDbVersions": [
    	{ "name": "3.6.2" }
    ],
    "monitoringVersions": [],
    "backupVersions": [],
    "agentVersion" : {
            "name" : "4.5.10.2429",
            "directoryUrl" : "/opt/mongodb/mms/agent/automation"
        },
    "processes": [
	    {
	        "version": "3.6.2",

	        "name": "<process_name>",
            "hostname": "<server1.example.net>",
	        "logRotate": {
	            "sizeThresholdMB": 1000,
	            "timeThresholdHrs": 24
	        },
	        "authSchemaVersion": 5,
	        "processType": "mongod",
	        "featureCompatibilityVersion": "3.6",
	        "args2_6": {
	            "net": {
	                "port": 27000
	            },
	            "storage": {
	                "dbPath": "/data/rs/1"
	            },
	            "systemLog": {
	                "path": "/data/rs/1/mongodb.log",
	                "destination": "file"
	            },
	            "replication": {
	                "replSetName": "<>"
	            }
	        }
	    },
	    {
	        "version": "3.6.2",
	        "name": "<process_name>",
            "hostname": "<server2.example.net>",
	        "logRotate": {
	            "sizeThresholdMB": 1000,
	            "timeThresholdHrs": 24
	        },
	        "authSchemaVersion": 5,
	        "processType": "mongod",
	        "featureCompatibilityVersion": "3.6",
	        "args2_6": {
	            "net": {
	                "port": 27000
	            },
	            "storage": {
	                "dbPath": "/data/rs/2"
	            },
	            "systemLog": {
	                "path": "/data/rs/2/mongodb.log",
	                "destination": "file"
	            },
	            "replication": {
	                "replSetName": "<>"
	            }
	        }
	    },
	    {
	        "version": "3.6.2",
	        "name": "<process_name>",
            "hostname": "<server3.example.net>",
	        "logRotate": {
	            "sizeThresholdMB": 1000,
	            "timeThresholdHrs": 24
	        },
	        "authSchemaVersion": 5,
	        "processType": "mongod",
	        "featureCompatibilityVersion": "3.6",
	        "args2_6": {
	            "net": {
	                "port": 27000
	            },
	            "storage": {
	                "dbPath": "/data/rs/3"
	            },
	            "systemLog": {
	                "path": "/data/rs/3/mongodb.log",
	                "destination": "file"
	            },
	            "replication": {
	                "replSetName": "<>"
	            }
	        }
	    }
    ],
    "replicaSets": [
	      {
	        "_id": "<>",
	        "members": [
	            {
	                "_id": 0,
	                "host": "<>"
	            },
	            {
	                "_id": 1,
	                "host": "<>"
	            },
	            {
	                "_id": 2,
	                "host": "<>"
	            }
	        ]
    	}
    ],
    "sharding": []
}

# name for the processes must be different in case deployed on the same host
templateDoc["processes"][0]["name"] = rs_name + "0_" + ports[0]
templateDoc["processes"][1]["name"] = rs_name + "1_" + ports[1]
templateDoc["processes"][2]["name"] = rs_name + "2_" + ports[2]

templateDoc["processes"][0]["hostname"] = hosts[0]
templateDoc["processes"][1]["hostname"] = hosts[1]
templateDoc["processes"][2]["hostname"] = hosts[2]


templateDoc["processes"][0]["args2_6"]["net"]["port"] = ports[0]
templateDoc["processes"][1]["args2_6"]["net"]["port"] = ports[1]
templateDoc["processes"][2]["args2_6"]["net"]["port"] = ports[2]

templateDoc["processes"][0]["args2_6"]["replication"]["replSetName"] = rs_name
templateDoc["processes"][1]["args2_6"]["replication"]["replSetName"] = rs_name
templateDoc["processes"][2]["args2_6"]["replication"]["replSetName"] = rs_name

templateDoc["replicaSets"][0]["_id"] = rs_name

templateDoc["replicaSets"][0]["members"][0]["host"] = hosts[0]
templateDoc["replicaSets"][0]["members"][1]["host"] = hosts[1]
templateDoc["replicaSets"][0]["members"][2]["host"] = hosts[2]

f = open('../files/autoConfigRS.json', 'w+')
f.write(json.dumps(templateDoc))
f.close()
