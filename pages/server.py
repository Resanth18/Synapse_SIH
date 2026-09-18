from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from twilio.rest import Client
import random, json, os

app = FastAPI()

# ---------------- CORS FIX ----------------
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- TWILIO ----------------
ACCOUNT_SID = "PASTE_YOUR_ACCOUNT_SID"
AUTH_TOKEN = "PASTE_YOUR_AUTH_TOKEN"
TWILIO_NUMBER = "whatsapp:+14155238886"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ---------------- DATABASE ----------------
DB_FILE = "users.json"
OTP_STORE = {}

class PhoneData(BaseModel):
    phone: str

class VerifyData(BaseModel):
    phone: str
    otp: str

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---------------- SEND OTP ----------------
@app.post("/send-otp")
def send_otp(data: PhoneData):

    phone = "whatsapp:" + data.phone
    otp = str(random.randint(100000, 999999))
    OTP_STORE[phone] = otp

    client.messages.create(
        body=f"🌾 AgroAURA Login OTP: {otp}",
        from_=TWILIO_NUMBER,
        to=phone
    )

    return {"status": "sent"}

# ---------------- VERIFY OTP ----------------
@app.post("/verify")
def verify(data: VerifyData):

    phone = "whatsapp:" + data.phone

    if OTP_STORE.get(phone) != data.otp:
        return {"status": "invalid"}

    users = load_users()

    if phone not in users:
        users[phone] = {"phone": phone}
        save_users(users)
        return {"status": "new"}

    return {"status": "existing"}