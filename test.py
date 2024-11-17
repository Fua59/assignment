import requests

client_id = "yuvKS9Kasf1Qc36eL7"
client_secret = "#4J2@L*Rawf!Tzd1%@%$(8WFK7Bo5Xu9"


url = f"https://dida365.com/oauth/authorize?scope=scope&client_id={client_id}&state=state&redirect_uri=redirect_uri&response_type=code"

resp = requests.get(
    url=url
)

print(resp.text)
