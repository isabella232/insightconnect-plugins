# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get Solution Details"


class Input:
    ID = "id"
    

class Output:
    SOLUTION = "solution"
    

class GetSolutionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Solution ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSolutionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "solution": {
      "$ref": "#/definitions/vulnerability_solution",
      "title": "Vulnerability Solution",
      "description": "Vulnerability solution",
      "order": 1
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    },
    "step": {
      "type": "object",
      "title": "step",
      "properties": {
        "html": {
          "type": "string",
          "title": "HTML",
          "description": "HTML description",
          "order": 1
        },
        "text": {
          "type": "string",
          "title": "Text",
          "description": "Text description",
          "order": 2
        }
      }
    },
    "vulnerability_solution": {
      "type": "object",
      "title": "vulnerability_solution",
      "properties": {
        "additional_information": {
          "type": "object",
          "title": "Additional Information",
          "description": "What the vulnerability applies to",
          "order": 3
        },
        "applies_to": {
          "type": "string",
          "title": "Applies To",
          "description": "What the vulnerability applies to",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "Solution ID",
          "description": "Solution ID",
          "order": 6
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 1
        },
        "resourse": {
          "type": "array",
          "title": "Resources",
          "description": "Resources",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "steps": {
          "$ref": "#/definitions/step",
          "title": "Solution Step",
          "description": "Solution steps",
          "order": 4
        },
        "summary": {
          "$ref": "#/definitions/step",
          "title": "Solution Summary",
          "description": "Solution Summary",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Solution type",
          "order": 7
        }
      },
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "URL",
              "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Link relation type following RFC 5988",
              "order": 2
            }
          }
        },
        "step": {
          "type": "object",
          "title": "step",
          "properties": {
            "html": {
              "type": "string",
              "title": "HTML",
              "description": "HTML description",
              "order": 1
            },
            "text": {
              "type": "string",
              "title": "Text",
              "description": "Text description",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
