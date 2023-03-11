# This is used to test small bits of code

import requests
import json

data = requests.get("http://127.0.0.1:4000/api/staff/").text

json.loads(data)