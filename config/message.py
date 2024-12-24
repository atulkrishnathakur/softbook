import os

from dotenv import load_dotenv
load_dotenv()

class CsgrpmMessage:
    CS_GRP_NAME: str = "CS group name is not given"
    CS_GRP_STATUS: str = "CS group status is only 0 or 1"

csgrpmessage = CsgrpmMessage()
