import os
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import nexmo

# Load environment variables from .env
load_dotenv()

# Nexmo API credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
nexmo_phone_number = os.getenv("NEXMO_PHONE_NUMBER")

# Function to send SMS
def send_sms():
    numbers = phone_numbers_entry.get()
    message = message_text.get("1.0", "end")

    # Split the phone numbers into a list
    numbers_list = [n.strip() for n in numbers.split(",")]

    # Initialize the Nexmo client
    client = nexmo.Client(key=api_key, secret=api_secret)

    # Send SMS to each phone number
    for number in numbers_list:
        response = client.send_message({
            'from': nexmo_phone_number,
            'to': number,
            'text': message,
        })

        if response['messages'][0]['status'] == '0':
            result_label.config(text=f"Message to {number} sent successfully.", foreground='green')
        else:
            result_label.config(text=f"Message to {number} failed with error: {response['messages'][0]['error-text']}", foreground='red')

# Create the main application window
app = tk.Tk()
app.title("Dammytech SMS Sender")

# Create and configure the input frame
input_frame = ttk.Frame(app, padding=10)
input_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Phone Numbers Label and Entry
phone_numbers_label = ttk.Label(input_frame, text="Phone Numbers (comma-separated):")
phone_numbers_label.grid(column=0, row=0, sticky=tk.W)

phone_numbers_entry = ttk.Entry(input_frame, width=50)
phone_numbers_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

# Message Label and Text
message_label = ttk.Label(input_frame, text="Message:")
message_label.grid(column=0, row=1, sticky=tk.W)

message_text = tk.Text(input_frame, wrap=tk.WORD, width=50, height=10)
message_text.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Send SMS Button
send_button = ttk.Button(input_frame, text="Send SMS", command=send_sms)
send_button.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))

# Result Label
result_label = ttk.Label(input_frame, text="", foreground='black')
result_label.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.E))

# Start the Tkinter main loop
app.mainloop()
