from ticktick.oauth2 import OAuth2 # OAuth2 Manager
from ticktick.api import TickTickClient # Main Interface
import os

from dotenv import load_dotenv

load_dotenv()

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

uri = ""

auth_client = OAuth2(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=uri
)

client = TickTickClient(username, password, auth_client)


