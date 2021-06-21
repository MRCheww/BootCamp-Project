import requests
from datetime import datetime  # allows to work with dates and times


def record():
    # open text file and record data
    outfile = open(r"D:\python2\Weather.txt", 'w')  # w - store and delete previous data
    # Store into text file
    outfile.write("-------------------------------------------------------------\n")
    outfile.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
    outfile.write("-------------------------------------------------------------\n")
    outfile.write("Current temperature is: {:.2f} degree Celsius\n".format(temp_city))
    outfile.write("Current weather desc  : {}\n".format(weather_desc))
    outfile.write("Current Humidity      : {} %\n".format(hmdt))
    outfile.write("Current wind speed    : {} kmph".format(wind_spd))
    outfile.close()


def read_print():
    # Open text file to read data
    infile = open(r"D:\python2\Weather.txt", "r")
    # read the content of the file and store it the program variable, content
    content = infile.readlines()
    # display the value line by line (Repetition)
    for line in content:
        print(line)
    infile.close()


api_key = '6f660c45352dd10ee3260d998d9d0b3c'  # set a variable for api key
location = input("Enter the city name: ")  # input city name

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key  # create a complete api link
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15) # kelvin to celsius (minus 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# call the function
record()
read_print()
