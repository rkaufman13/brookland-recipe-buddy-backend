
from fastapi import FastAPI
from functools import lru_cache
from pydantic import BaseModel,Field
from config import Settings
from validators import contains_url
from recipe_parsing import parse_recipe
from templatizer import generate_and_encode_template

@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
pattern = f"{settings.admin_email}"
github_api_key = settings.github_api_key

class RecipientEmail(BaseModel):
    address: str = Field(...,pattern=pattern)

class EmailPayload(BaseModel):
    date: str
    from_email: str = Field(..., alias="from")
    stripped_text: str = Field(..., alias="stripped-text")
    recipient: RecipientEmail


class IncomingEmail(BaseModel):
    payload: EmailPayload

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/incoming-message")
async def parse_message(message:IncomingEmail):
    message_body = message.payload.stripped_text
    message_sender = message.payload.from_email
    recipe_url = contains_url(message_body)
    if not recipe_url:
        return {"message": "no url found"}
    recipe = parse_recipe(recipe_url)
    if not recipe:
        return {"message": "no recipe found at URL"}
    encoded_template = generate_and_encode_template(recipe, message_sender)
    return {"message": "this was valid"}


