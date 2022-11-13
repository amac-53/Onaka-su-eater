from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests
import json
import xmltodict
import config

api_key = config.HOTPEPPER_API_KEY

app = FastAPI()


origins = [
    "*"
    # "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# return json
# http://127.0.0.1:8000/items/?latitude=34.910047&longitude=135.7805467&range=300
@app.get("/items/")
async def get_items(latitude: float = 0, longitude: float = 0, range: int = 1, count: int = 100):
    range_list =  {300: 1, 500: 2, 1000: 3, 2000: 4, 3000: 5}
    base_url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    query = {
    'key': api_key,
    'lat': str(latitude),
    'lng': str(longitude),
    'range': str(range_list[range]),
    'count': str(count)
    }

    res = requests.get(base_url, query)
    dict_data = xmltodict.parse(res.text)  # XML to dict
    # return Response(content=res.text, media_type="application/xml")
    return dict_data

# http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=296aec41c1f8b322&lat=34.67&lng=135.52&range=5&order=4

# 各店の詳細情報を取得
@app.get("/items/detail/")
async def get_items(id: str):
    base_url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    query = {
    'key': api_key,
    'id': id,
    }

    res = requests.get(base_url, query)
    dict_data = xmltodict.parse(res.text)  # XML to dict
    # return Response(content=res.text, media_type="application/xml")
    return dict_data