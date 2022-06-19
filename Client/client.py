import requests
import json

url = "http://localhost:5000/users"

payload = json.dumps({
                "ime": "Despot",
                "prezime": "Krsmanovic",
                "username": "dkrsmanovic",
                "smer": "RI",
                "predmeti": [
                    { "ime" : "UUP", "espb" : 8 },
                    { "ime" : "MA", "espb" : 6 },
                    { "ime" : "PDS", "espb" : 6 }
                ],
                "id": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)