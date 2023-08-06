from fastapi import FastAPI
import uvicorn
from main import generate_password

app=FastAPI()

@app.get('/')
def index():
    return {'message': "Hello,Dev Nishant"}

@app.get("/generate")
def generate(digit=False,uppercase=False,schar=True,length=12):
    return {'password': generate_password(digit,uppercase,schar,length)}

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=10000)