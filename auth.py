from fastapi import HTTPException, Security, Depends,Header
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

config_env={"API_KEY_HEADER":"abcd1234","user-agent":"chronicle"}

api_key_header=APIKeyHeader(name="access_token",auto_error=False)
async def get_api_key(api_key_header:str =Security(api_key_header),user_agent:str=Header()):
    if api_key_header==config_env["API_KEY_HEADER"] and user_agent=="chronicle":
        return api_key_header
    else:
        raise HTTPException(HTTP_403_FORBIDDEN)
