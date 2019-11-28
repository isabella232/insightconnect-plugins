# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve running processes for a specific agent"


class Input:
    IDS = "ids"
    

class Output:
    AGENTS_PROCESSES = "agents_processes"
    

class AgentsProcessesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ids": {
      "type": "array",
      "title": "IDS",
      "description": "Agent ID list",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "ids"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsProcessesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agents_processes": {
      "type": "array",
      "title": "Agents Processes",
      "description": "Agents processes entities",
      "items": {
        "$ref": "#/definitions/agents_processes"
      },
      "order": 1
    }
  },
  "definitions": {
    "agents_processes": {
      "type": "object",
      "title": "agents_processes",
      "properties": {
        "cpuUsage": {
          "type": "integer",
          "title": "CPU Usage",
          "description": "CPU Usage (%)",
          "order": 4
        },
        "executablePath": {
          "type": "string",
          "title": "Executable path",
          "description": "Executable path",
          "order": 5
        },
        "memoryUsage": {
          "type": "integer",
          "title": "Memory usage",
          "description": "Memory usage (MB)",
          "order": 3
        },
        "pid": {
          "type": "integer",
          "title": "PID",
          "description": "Process ID",
          "order": 6
        },
        "processName": {
          "type": "string",
          "title": "Process name",
          "description": "Process name",
          "order": 2
        },
        "startTime": {
          "type": "string",
          "title": "Start time",
          "description": "Start time",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)