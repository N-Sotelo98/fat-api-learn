from fastapi import FastAPI,Header,Depends
import auth
from fastapi.security.api_key import APIKey 
from typing import Annotated
import subprocess

def get_cwd():

    result=subprocess.run("pwd",stdout=subprocess.PIPE,text=True)
    return result.stdout
app = FastAPI()


@app.get("/read_directory/")
def execute_command(api_key:APIKey=Depends(auth.get_api_key))-> str:
    #Execute Bash: asynchronously for each cloud provider?
    #azure
    #oracle
    #gcp
    current_directory=get_cwd()
    
    return current_directory

@app.get("/test/")
def retrieve_header(user_agent:Annotated[str | None, Header()] = None):
    print(Header())
    return {"headers":user_agent}