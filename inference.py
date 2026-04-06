import requests

BASE = "http://localhost:7860"

res = requests.post(f"{BASE}/reset").json()

action = {
    "type": "security",
    "priority": "high",
    "route": "security_team"
}

result = requests.post(f"{BASE}/step", json=action).json()

print(result)