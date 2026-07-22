from weather import get_weather #this gets the getweather function from the weather file


def display_weather(data):#this creates a function we can use over again 
    print("\n -----Weather Report-----") #this just prints weather report at the top to make it look good, the \n means add a new line
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")  #the api will return a specific order of things so python will look in the main folder then temp and then spit out the value in temp
    print(f"Feels Like: {data['main']['feels_like']}°C")    #same idea as last one api spits something and python looks in the folder and spit out the value in feels like
    print(f"Humidity: {data['main']['humidity']}%") #same idea
    print(f"Weather: {data['weather'][0]['description'].title()}") # this follows the same idea, but then we have a list the 0 is telling python to find the first value in the list and print it out then the .title just mean capitalize first letter of every word
    print(f"Wind Speed: {data['wind']['speed']} kph")
    print("----------------------------") # this is a divider to make the output easy to read

def main(): #this is creating another function but this controls the whole program

    city = input("What city do you want to know the weather of: ")
    weather = get_weather(city) #inside the weather folder get weather gets the api dictionary then it stores it into the weather variable

    if weather is None:
        print("City not found") #in the weather folder we set it as if it found no city then return none, this means if it is none then to print city not found
        return #this wont run anything after

    display_weather(weather) # if everything works this means it should print everything

main() #then this line starts the program