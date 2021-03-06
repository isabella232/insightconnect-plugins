# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Poll for Blacklisted Addresses"


class Input:
    
    DAYS = "days"
    FREQUENCY = "frequency"
    LIMIT = "limit"
    TAG = "tag"
    

class Output:
    
    RESULTS = "results"
    

class PollAddressBlacklistInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "days": {
      "type": "integer",
      "title": "Days",
      "description": "Age of Data in Days",
      "enum": [
        1,
        2,
        3
      ],
      "order": 3
    },
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "Poll frequency in seconds",
      "default": 300,
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Number of Results, 1-5000",
      "default": 1,
      "order": 2
    },
    "tag": {
      "type": "string",
      "title": "Tag",
      "description": "Tag",
      "enum": [
        "blacklist",
        "malware",
        "botnet",
        "spam",
        "phishing",
        "malicious activity",
        "dnsbl"
      ],
      "order": 4
    }
  },
  "required": [
    "days",
    "limit",
    "tag"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PollAddressBlacklistOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/ip_blacklist",
      "title": "Results",
      "description": "Results",
      "order": 1
    }
  },
  "definitions": {
    "ip_blacklist": {
      "type": "object",
      "title": "ip_blacklist",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "next": {
          "type": "string",
          "title": "Next",
          "order": 2
        },
        "previous": {
          "type": "string",
          "title": "Previous",
          "order": 3
        },
        "results": {
          "type": "array",
          "title": "Results",
          "items": {
            "$ref": "#/definitions/ip_results"
          },
          "order": 4
        }
      },
      "definitions": {
        "ip_results": {
          "type": "object",
          "title": "ip_results",
          "properties": {
            "addr": {
              "type": "string",
              "title": "Addr",
              "order": 1
            },
            "url": {
              "type": "string",
              "title": "Url",
              "order": 2
            }
          }
        }
      }
    },
    "ip_results": {
      "type": "object",
      "title": "ip_results",
      "properties": {
        "addr": {
          "type": "string",
          "title": "Addr",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "Url",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
