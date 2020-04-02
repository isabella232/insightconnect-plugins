# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return a single assessment with the specified ID"


class Input:
    ID = "id"
    

class Output:
    DATA = "data"
    

class AssessmentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The UUID of a specific assessment to return",
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


class AssessmentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/assessment",
      "title": "Data",
      "description": "Returned assessment data",
      "order": 1
    }
  },
  "definitions": {
    "assessment": {
      "type": "object",
      "title": "assessment",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "description": "The date and time the assessment was created, eg. 2019-07-02T16:22:15.879357Z",
          "order": 1
        },
        "document": {
          "type": "string",
          "title": "Document",
          "description": "The main content of the assessment",
          "order": 2
        },
        "editorId": {
          "type": "string",
          "title": "Editor ID",
          "description": "The UUID of the contributor who last edited the assessment",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The UUID of the assessment",
          "order": 4
        },
        "metadata": {
          "type": "object",
          "title": "Metadata",
          "description": "A JSON value containing key/value pairs describing various attributes about this assessment",
          "order": 5
        },
        "revisionDate": {
          "type": "string",
          "title": "Revision Date",
          "description": "The date and time the assessment was last changed, eg. 2019-07-02T16:22:15.879357Z",
          "order": 6
        },
        "topicId": {
          "type": "string",
          "title": "Topic ID",
          "description": "The UUID of the topic this assessment is based on",
          "order": 7
        }
      },
      "required": [
        "document",
        "topicId"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)