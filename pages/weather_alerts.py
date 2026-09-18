# weather_alerts.py

import requests
from twilio.rest import Client # Uncomment this line
import streamlit as st   # ◄ add Streamlit for UI feedback

import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
farmers = [
    {"name": "Farmer", "phone": "+918248573735", "city": "Avadi, Chennai"}
]

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    temp = res['main']['temp']
    desc = res['weather'][0]['description']
    return f"Weather in {city} today: {temp}°C, {desc}"

def send_sms(to, msg):
    client = Client(TWILIO_SID, TWILIO_AUTH) # Uncomment this line
    message = client.messages.create(body=msg, from_=TWILIO_PHONE, to=to) # Uncomment this line
    print(f"✅ Sent to {to}: {msg}") # Original print statement

def run_weather_alerts():
    st.subheader("◔ Weather Alerts")
    for farmer in farmers:
        weather_msg = get_weather(farmer["city"])
        final_msg = f"Vanakkam {farmer['name']}! 🌱\n{weather_msg}\nTake care of your crops."
        send_sms(farmer["phone"], final_msg)
        st.success(f"✅ SMS sent to {farmer['name']} ({farmer['phone']}) — {weather_msg}") # Uncomment this line
        # st.info(f"SMS functionality disabled. Processed for {farmer['name']} ({farmer['phone']}) — {weather_msg}") # Comment out this line

if __name__ == "__main__":   # ◄ corrected
    run_weather_alerts()