from fastapi import FastAPI, Request
from datetime import datetime
storage = FastAPI(title='MY FASTAPI')

@storage.get('/')
def index():
    return "My name is Innocent, This is my first API"

@storage.get('/today')
def today():
    return str(datetime.now())

@storage.get('/my_name')
def names(first_name: bool = False, last_name: bool = False, full_name_: bool=False):

    full_name = ""
    if first_name:
        full_name += 'Innocent'
    if last_name:
        full_name += ' Mukoki'
    if full_name_:
        full_name = 'My name is Innocent Mukoki'
    return full_name
