import requests
import json
from datetime import datetime
import csv
import os
import smtplib
from email.message import EmailMessage

# === Jobstronaut™ Auto Apply Script ===
# Created by Alise McNiel | jobstronaut.dev

# Load applicant profile
with open("autofill_profile.json", "r") as f:
    profile = json.load(f)

# Prepare data payload as form fields
data = {
    "name": profile.get("name"),
    "email": profile.get("email"),
    "interest": profile.get("interest")
}

# Attach the real resume with correct filename and MIME type
files = {
    "resume": ("resume.pdf", open("resume.pdf", "rb"), "application/pdf")
}

# Send POST request with the actual resume
response = requests.post(
    "https://jobstronaut-backend.onrender.com/apply",
    data=data,
    files=files
)

# Log the response
timestamp = datetime.now().isoformat()
print("Application submitted at:", timestamp)
print("Status:", response.status_code)
print("Response:", response.text)

# === Step 2: Save log entry ===
log_file = "application_log.csv"
log_exists = os.path.isfile(log_file)

with open(log_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    if not log_exists:
        writer.writerow(["timestamp", "name", "email", "interest", "status_code"])
    writer.writerow([
        timestamp,
        data["name"],
        data["email"],
        data["interest"],
        response.status_code
    ])

# === Step 3: Send email notification ===
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use an app password, not your main password
EMAIL_RECEIVER = profile.get("email")

if response.status_code == 200:
    subject = "Jobstronaut: Application Submitted"
    body = f"Hi {data['name']},\n\nYour application was submitted successfully at {timestamp}.\n\n– Jobstronaut"
else:
    subject = "Jobstronaut: Submission Failed"
    body = f"Hi {data['name']},\n\nYour application failed to submit.\nStatus: {response.status_code}\n\n– Jobstronaut"

msg = EmailMessage()
msg.set_content(body)
msg["Subject"] = subject
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email notification sent!")
except Exception as e:
    print("Email failed:", str(e))

# === End of Jobstronaut™ Auto Apply ===

