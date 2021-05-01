#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date


class Item(BaseModel):
    id: int
    author: str
    title: str
    content: str
    date:date

app = FastAPI()

d = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{blog_id}")
async def get_by_id(blog_id:int):
    print(d)
    res = d[blog_id] if blog_id in d else f'Blog id {blog_id} not present'
    json_compatible_item_data = jsonable_encoder(res)
    return JSONResponse(content=json_compatible_item_data)

@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)

@app.post("/items/")
async def post_item(item: Item):
    d[item.id] = item
    return JSONResponse(jsonable_encoder(item))


