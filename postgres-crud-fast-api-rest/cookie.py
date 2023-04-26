#
# Manipulação de Cookie
# https://docs.roy4801.tw/Programming%20Language/python/libs/fastapi/
#
# uvicorn cookie:app --reload
#

from typing  import Optional

from fastapi import FastAPI, HTTPException 
app = FastAPI()

# getCookie - Recupera um Cookie existente
from fastapi import Cookie
@app.get('/getCookie')
def get_cookie(test: Optional[str] = Cookie(...)):
    return test

# setCookie - Guarda um valor em um Cookie
from fastapi import Response
@app.get('/setCookie')
def set_cookie(response: Response):
    response.set_cookie(key='test', value='teste de cookie')
    response.set_cookie(key='test2', value='teste 2 de cookie')
    return {'message': 'success'}