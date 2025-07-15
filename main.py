import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 24.807390
MY_LONG = -107.394440

MY_EMAIL = "mail@gmail.com"
PASSWORD = "password"


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    return abs(MY_LAT - iss_lat) <= 5 and abs(MY_LONG - iss_long) <= 5


def is_dark():
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
    current_hour = datetime.utcnow().hour

    return current_hour >= sunset or current_hour <= sunrise


def notify_user():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email_to@gmail.com",
            msg="Subject:Mira al cielo 👀\n\nLa ISS está sobre ti."
        )

# Ejecuta cada 60 segundos
while True:
    if is_iss_close() and is_dark():
        notify_user()
        print("Correo enviado.")
    else:
        print("Nada que ver.")
    time.sleep(60)
