import requests
from datetime import datetime

MY_LAT = 33.747700 # Your latitude
MY_LONG = -90.721700 # Your longitude


def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if MY_LAT >= (iss_latitude - 5) and MY_LAT <= (iss_latitude + 5):
        if MY_LONG >= (iss_longitude - 5) and MY_LONG <= (iss_longitude + 5):
            return True
            
        else:
            return False
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()



    
is_above()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



