# fastapi-masterclass

https://docs.python.org/3/library/venv.html

Setup:
   Setup environment: python3 -m venv fastapi-env
   Activate the environment: source fastapi-env/bin/activate    
   Install fastapi: pip3 install fastapi
   Install fasapi server: pip3 install uvicorn    

Start fastapi server: uvicorn main:app --reload

Swagger: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc

Use this repository to face the CORS error message: https://github.com/Brunorodrigoss/app-practice

To generate a Rando Secret key, you can use it: openssl rand -hex 32

https://htmledit.squarefree.com/