# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Delete capture file"


class Input:
    CID = "cid"
    

class Output:
    ID = "id"
    MESSAGE = "message"
    STATUS = "status"
    

class DeleteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cid": {
      "type": "string",
      "title": "Cid",
      "description": "Cloud Shark ID",
      "order": 1
    }
  },
  "required": [
    "cid"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Cloud Shark ID",
      "description": "Cloudshark ID",
      "order": 3
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 2
    },
    "status": {
      "type": "integer",
      "title": "HTTP Status",
      "description": "HTTP status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
