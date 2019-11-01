# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DIRECTORY = "directory"
    INSTANCE_ID = "instance_id"
    PRIVATE_KEY = "private_key"
    REGION = "region"
    USER = "user"
    

class Output:
    MALWARE = "malware"
    

class ClamAvInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "directory": {
      "type": "string",
      "title": "Directory",
      "description": "Directory to scan",
      "order": 5
    },
    "instance_id": {
      "type": "string",
      "title": "Instance Id",
      "description": "Instance ID",
      "order": 1
    },
    "private_key": {
      "type": "string",
      "title": "Private Key",
      "description": "Private key",
      "order": 3
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "Region",
      "order": 2
    },
    "user": {
      "type": "string",
      "title": "User",
      "description": "User name",
      "order": 4
    }
  },
  "required": [
    "private_key",
    "user",
    "directory",
    "instance_id",
    "region"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ClamAvOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "malware": {
      "type": "array",
      "title": "Malware",
      "description": "Malware",
      "items": {
        "$ref": "#/definitions/malicious_files"
      },
      "order": 1
    }
  },
  "definitions": {
    "malicious_files": {
      "type": "object",
      "title": "malicious_files",
      "properties": {
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "order": 4
        },
        "file": {
          "type": "string",
          "title": "File",
          "order": 1
        },
        "hash_value": {
          "type": "string",
          "title": "Hash Value",
          "order": 3
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)