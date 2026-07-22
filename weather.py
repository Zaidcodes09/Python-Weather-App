import requests #this function tells python it can access web sites
from config import API_KEY     #this tells python to go into the config file and grab the api key

def get_weather(city):   #this creates and defines a getweather function which we can reuse in the code
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    ) #this builds the Api request url which python sends to open weather
    print("Sending request...")
    response = requests.get(url)  #the website sends information back so that gets store into response
    print("Response received!")
    


    response.status_code #this gets the status code and every web sends one, ex. 200 is success, 404 not found

    if response.status_code != 200:
        return None#this says if we get anything other than success it wont spit out anything
    
    return response.json() # the api sends data in a special way so .json puts it into the python dictionary