from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import config

api_key = config.HOTPEPPER_API_KEY

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/")
async def get_items(latitude: float = 0, longitude: float = 0, range: int = 1, count: int = 100, order: int = 0, keyword: str = ''):
    """
    現在地付近の店の情報を全て返す
    range: 現在地からの距離
    count: 店の数の上限
    order: ソート順（0: 近い順，4:おすすめ順）
    keyword: キーワード
    """

    range_list =  {300: 1, 500: 2, 1000: 3, 2000: 4, 3000: 5}
    base_url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    query = {
    'key': api_key,
    'lat': str(latitude),
    'lng': str(longitude),
    'range': str(range_list[range]),
    'count': str(count),
    'keyword': str(keyword),
    'format': 'json'
    }

    # 指定があればおすすめ順のクエリを追加
    if order == 4:
        query['order'] = str(order)

    res = requests.get(base_url, query)
    return res.json()


@app.get("/items/detail/")
async def get_an_item(id: str):
    """
    特定の店の情報を返す
    id: 店を一意に識別するid
    """

    base_url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    query = {
    'key': api_key,
    'id': id,
    'format': 'json'
    }

    res = requests.get(base_url, query)
    return res.json()