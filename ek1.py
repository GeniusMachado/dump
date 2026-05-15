"""So lets play with python code today for a while"""
from fastapi import FastAPI
import time
import SQLite
import httpx

URL = "https://linkedin.com/in/YOUR_USERNAME"
j = 2
for j in range(100):
  i=httpx.request(URL)

j=int(input("please enter the amount of times you want to visit the linkedin URL/hammer the profile for views"))



async def hammer(URL,j):
    time.sleep(3)
    r=httpx.request(URL,postl)
    return r
