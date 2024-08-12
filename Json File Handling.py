# Json File Handling

import json

"""
Convert from Json to Python Dictionary
"""

# Sample Json Data
JsonData= '{"userId": 1,"id": 1,"title": "delectus aut autem","completed": false}'

# Conversion
data = json.loads(JsonData)

# Output Data
print(data["userId"])
print(data["title"])
print(data["completed"])

print("\n----------\n")

"""
Convert from Python Dictionary to Json
"""

# Sample Dictionary Data
rawData = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Convert data to Json with 4 indent before each key also sort keys
JSON = json.dumps(rawData,indent=4 , sort_keys=True)

# Output Json
print(JSON)
