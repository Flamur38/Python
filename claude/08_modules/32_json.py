import json

raw = '{"source_ip": "10.0.0.9", "user": "admin", "action": "login", "success": false}'
event = json.loads(raw)         # loads = "load string" -> Python dict

print(type(event))              # <class 'dict'>
print(event['source_ip'])       # 10.0.0.9
print(event['success'])         # 10.0.0.9



