from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from exception.custom_exception import CustomException
from typing import List
from typing_extensions import Annotated
from typing import Any
from fastapi import status
from config.message import csgrpmessage
from config.constants import constants

def cs_grp_name_checker(value: str) -> str:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value == "":
         raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message=csgrpmessage.CS_GRP_NAME,
            data=[]
        )
    return value

def cs_grp_status_checker(value: int) -> int:
    # https://docs.pydantic.dev/latest/concepts/validators/
    if value != 0 and value != 1:
         raise CustomException(
            status_code=status.HTTP_400_BAD_REQUEST,
            status=constants.STATUS_BAD_REQUEST,
            message=csgrpmessage.CS_GRP_STATUS,
            data=[]
        )
    return value


class CsgmSave(BaseModel):
    cs_grp_name: Annotated[str, PlainValidator(cs_grp_name_checker)]
    cs_grp_code: str | None = None
    status: Annotated[int | None, Field(default=1), PlainValidator(cs_grp_status_checker)]
