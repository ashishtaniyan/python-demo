from google import genai
import requests
from google.genai import types
from datetime import datetime


#Defining a function that fetches weather data from an external API
def get_weather(latitude, longitude, date=None):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    if date:
        url = base_url + f"&current=temperature_2m,wind_speed_10m&start_date={date}&end_date={date}"
    else:
        url = base_url + "&current=temperature_2m,wind_speed_10m"
    
    response = requests.get(url)
    data = response.json()
    if date:
        print (f"date is {date}")
        return data["hourly"]["temperature_2m"][date]
    else:
        return data["current"]["temperature_2m"]

#Defining a function that fetches coordinates from an external API based on the place name.
def get_coordinates(place):
    url = f"https://geocode.maps.co/search?q={place}"
    response = requests.get(url)
    data = response.json()
    if data:
        return {
            "latitude": data[0]["lat"],
            "longitude": data[0]["lon"]
        }
    else:
        return {"error": "Location not found"}

def ask_me(question):
     # Configure Gemini with your API key
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )
    return response.text

#Creating a function that will provide travel and clothing instructions based on the weather of that location. 
def smart_get_itenary(prompt: str) -> str:
    # Defining the Tools Definition. Details about the functions that would be avaliable to the model.
    weather_function_definition = {
            "name": "get_weather",
            "description": "Gets the current weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {
                        "type": "number",
                        "description": "The latitude of the location, e.g. 37.7749 for San Francisco",
                    },
                    "longitude": {
                        "type": "number",
                        "description": "The longitude of the location, e.g. -122.4194 for San Francisco",
                    },
                    "date": {
                        "type": "string",
                        "description": "The date for which the weather is requested in YYYY-MM-DD format. If not provided, current weather will be fetched.",
                    },
                },
                "required": ["latitude", "longitude"],
            }
        }
    
    coordinate_function_definition = {
            "name": "get_coordinates",
            "description": "Gets the coordinates for a given place.",
            "parameters": {
                "type": "object",
                "properties": {
                    "place": {
                        "type": "string",
                        "description": "The name of the place, e.g. San Francisco",
                    },
                    },
                "required": ["place"],
            }
    }
    
    input_messages =  [prompt]
    
    # Configure Gemini with your API key
    client = genai.Client()
    tools = types.Tool(function_declarations=[weather_function_definition, coordinate_function_definition])
    config = types.GenerateContentConfig(tools=[tools])

    # Step 1: Call model with tools
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=input_messages,
        config=config,
    )
    
    current_date = datetime.now().date().isoformat()

    #Step 2: Handle Function Calls. Here 'tool_call' is being returned by the model and we need to parse it. Also the if the model calls the function, 
    #Then "function_call" will be populated in the response.
    candidate = response.candidates[0]
    content = candidate.content
    parts = getattr(content, "parts", []) if content else []


    if parts and hasattr(parts[0], 'function_call') and parts[0].function_call:
        function_call = parts[0].function_call
        function_name = function_call.name
        function_args = function_call.args
        if function_name == "get_weather":
            weather = get_weather(
                    latitude=function_args["latitude"],
                    longitude=function_args["longitude"],
                    date=current_date
                    )
            # Step 3: Call the model again with the function result
            follow_up_message = [input_messages, f"Given that current date is  {current_date}, The current temperature at the location is {weather}°C."]
        
        elif function_name == "get_coordinates":
            coordinates = get_coordinates(place=function_args["place"]) #Here the model calls the get_cordinates function to get the lat and long of the place.
            if "error" in coordinates:
                follow_up_message = [input_messages, f"The location {function_args['place']} was not found. Please try again with a different location."]
            else:  #If the coordinates are found, we call the model again with the coordinates. and Add more message to the conversation for the model to understand the context.
                follow_up_message = [input_messages, f"Given that current date is  {current_date},The coordinates for {function_args['place']} are Latitude: {coordinates['latitude']}, Longitude: {coordinates['longitude']}."]
        
        follow_up_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=follow_up_message,
        )
        return follow_up_response.text
    else:
        print("No function call found in the response.")
        return response.text
        
print(smart_get_itenary("I want to travel to Kerala tommorrow. What is the weather like there? What should I pack?"))
#print(ask_me("What is the date today"))
#print(get_weather(28.6139,77.2090,"2024-10-01"))
