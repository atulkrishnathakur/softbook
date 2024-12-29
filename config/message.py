import os

from dotenv import load_dotenv
load_dotenv()

class CsgrpmMessage:
    CS_GRP_NAME: str = "CS group name is not given"
    CS_GRP_STATUS: str = "CS group status is only 0 or 1"
    DELETE_SUCCESS: str = "CS group deleted successfully"
    CS_GRP_SAVE_MESSAGE: str = "CS group name successfully save"
    CS_GRP_LIST_MESSAGE: str = "CS group name list"
    CS_GRP_ACTIVE_LIST_MESSAGE: str = "CS group name active list"
    CS_GRP_UPDATE_MESSAGE: str = "CS group name successfully updated"
    
csgrpmessage = CsgrpmMessage()
