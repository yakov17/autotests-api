from jsonschema import validate

# Пример схемы
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

# Пример данных
data = {
  "name": "John Doe",
  "age": 30
}

validate(instance=data, schema=schema)