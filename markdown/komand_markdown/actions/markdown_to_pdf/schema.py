# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Convert Markdown to PDF"


class Input:
    MARKDOWN = "markdown"
    MARKDOWN_STRING = "markdown_string"
    

class Output:
    PDF = "pdf"
    PDF_STRING = "pdf_string"
    

class MarkdownToPdfInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "markdown": {
      "type": "string",
      "title": "Markdown Bytes",
      "displayType": "bytes",
      "description": "Markdown content represented in base64",
      "format": "bytes",
      "order": 1
    },
    "markdown_string": {
      "type": "string",
      "title": "Markdown String",
      "description": "Markdown content as a string",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MarkdownToPdfOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pdf": {
      "type": "string",
      "title": "PDF",
      "displayType": "bytes",
      "description": "PDF data as bytes",
      "format": "bytes",
      "order": 1
    },
    "pdf_string": {
      "type": "string",
      "title": "PDF",
      "description": "PDF data as string",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
