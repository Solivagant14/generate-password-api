from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from main import generate_password

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {'message': "Hello,Dev Nishant"}

@app.get("/generate")
def generate(digit:bool=False,uppercase:bool=False,schar:bool=False,length:int=12):
    return {'password': generate_password(digit,uppercase,schar,length)}

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=10000)