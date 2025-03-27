
from dotenv import load_dotenv
import os
import google.generativeai as ggi

load_dotenv(".env")

fetcheed_api_key = os.getenv("API_KEY")
ggi.configure(api_key = fetcheed_api_key)

for model in ggi.list_models():
    print(model)