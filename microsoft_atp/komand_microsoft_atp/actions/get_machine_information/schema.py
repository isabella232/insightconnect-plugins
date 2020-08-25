# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get details about a machine with its ID"


class Input:
    MACHINE = "machine"
    

class Output:
    MACHINE = "machine"
    

class GetMachineInformationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine": {
      "type": "string",
      "title": "Machine",
      "description": "Machine IP address, hostname and machine ID",
      "order": 1
    }
  },
  "required": [
    "machine"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetMachineInformationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine": {
      "$ref": "#/definitions/machine",
      "title": "Machine",
      "description": "Machine information",
      "order": 1
    }
  },
  "required": [
    "machine"
  ],
  "definitions": {
    "machine": {
      "type": "object",
      "title": "machine",
      "properties": {
        "agentVersion": {
          "type": "string",
          "title": "Agent Version",
          "description": "Agent version",
          "order": 1
        },
        "computerDnsName": {
          "type": "string",
          "title": "Computer DNS Name",
          "description": "Computer DNS name",
          "order": 2
        },
        "exposureLevel": {
          "type": "string",
          "title": "Exposure Level",
          "description": "Exposure level",
          "order": 3
        },
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "description": "First seen",
          "order": 4
        },
        "healthStatus": {
          "type": "string",
          "title": "Health Status",
          "description": "Health status",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 6
        },
        "lastExternalIpAddress": {
          "type": "string",
          "title": "Last External IP Address",
          "description": "Last external IP address",
          "order": 7
        },
        "lastIpAddress": {
          "type": "string",
          "title": "Last IP Address",
          "description": "Last IP address",
          "order": 8
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "description": "Last seen",
          "order": 9
        },
        "machineTags": {
          "type": "array",
          "title": "Machine Tags",
          "description": "Machine Tags",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "osBuild": {
          "type": "integer",
          "title": "OS Build",
          "description": "OS build",
          "order": 10
        },
        "osPlatform": {
          "type": "string",
          "title": "OS Platform",
          "description": "OS platform",
          "order": 11
        },
        "osProcessor": {
          "type": "string",
          "title": "OS Processor",
          "description": "OS processor",
          "order": 12
        },
        "rbacGroupId": {
          "type": "integer",
          "title": "RBAC Group ID",
          "description": "RBAC group ID",
          "order": 13
        },
        "riskScore": {
          "type": "string",
          "title": "Risk Score",
          "description": "Risk score",
          "order": 14
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 15
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
