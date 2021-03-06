# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search for OTRS tickets"


class Input:
    CUST_ID = "cust_id"
    DYNAMIC_FIELDS = "dynamic_fields"
    EXTERNAL_PARAMS = "external_params"
    QUEUE = "queue"
    

class Output:
    TICKET_IDS = "ticket_ids"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cust_id": {
      "type": "string",
      "title": "Customer ID",
      "description": "Customer ID",
      "order": 1
    },
    "dynamic_fields": {
      "type": "array",
      "title": "Dynamic Fields",
      "description": "Fields as array of objects e.g. [{\\"name\\":\\"TestName1\\",\\"value\\":\\"TestValue1\\", \\"operation\\":\\"Equals\\"},{\\"name\\":\\"TestName2\\",\\"value\\":\\"TestValue2\\"}]. The value field is what will be searched for",
      "items": {
        "$ref": "#/definitions/search_dynamic_field"
      },
      "order": 4
    },
    "external_params": {
      "type": "array",
      "title": "External Parameters",
      "description": "A key value object thats not a Dynamic Field e.g [{\\"Title\\":\\"Test Ticket\\"}]",
      "items": {
        "$ref": "#/definitions/external_param"
      },
      "order": 2
    },
    "queue": {
      "type": "string",
      "title": "Queue",
      "description": "Queue to search in",
      "order": 3
    }
  },
  "definitions": {
    "external_param": {
      "type": "object",
      "title": "external_param",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of parameter to search on",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value to search for",
          "order": 2
        }
      }
    },
    "search_dynamic_field": {
      "type": "object",
      "title": "search_dynamic_field",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Dynamic field name",
          "order": 1
        },
        "operator": {
          "type": "string",
          "title": "Operator",
          "description": "Dynamic field operator",
          "order": 3
        },
        "pattern": {
          "type": "array",
          "title": "Pattern",
          "description": "Search pattern",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Dynamic field value",
          "order": 2
        }
      },
      "required": [
        "name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_ids": {
      "type": "array",
      "title": "Ticket IDs",
      "description": "IDs of tickets matching search criteria",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
