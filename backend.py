from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    is_winning_hand: bool
    description: str | None = None
    winning_value: int | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/solve")
async def get_winning_hand_query(list_of_mahjong_tiles):
    # place holder for the mahjong winning hand
    query_dict = {} 
    query_dict.update({"is_winning_hand": True})
    query_dict.update({"description": "test description"})
    query_dict.update({"winning_value": 5})

    return query_dict 
