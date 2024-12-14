from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()

def get_curweather( city="Mumbai"):
   

    Request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    wedata=requests.get(Request_url).json()
    return wedata
  
if __name__=="__main__":
  print("wether condition are \n")
  city=input("enter city name\n")
  if not bool(city.strip()):
     city="mumbai" 
     
  weadat=get_curweather(city)
  print("\n")
  pprint(weadat)