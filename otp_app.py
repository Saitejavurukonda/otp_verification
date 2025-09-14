from twilio.rest import Client
import random
import tkinter as tk
from tkinter import messagebox

print("[DEBUG] Script started.")

# ✅ Replace with your Twilio credentials
account_sid = ""
auth_token = ""
twilio_number = ""
recipient_number = ""

# Generate initial OTP
n = random.randint(1000, 9999)
verified = False

# ✅ Send OTP using Twilio (with error handling)
def send_otp():
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            to=recipient_number,
            from_=twilio_number,
            body=f"🔐 Your OTP is: {n}"
        )
        print(f"[DEBUG] OTP sent: {n}")
    except Exception as e:
        print("[ERROR] Failed to send OTP:", e)

# ✅ GUI Setup
root = tk.Tk()
root.title("OTP Verification")
root.geometry("400x300")

# OTP Input Field
tk.Label(root, text="Enter OTP", font=('Arial', 14)).pack(pady=20)
user = tk.Entry(root, font=('Arial', 14))
user.pack()

# ✅ OTP Check Function
def checkOTP():
    global verified, n
    try:
        user_input = int(user.get())
        if verified:
            messagebox.showinfo("Info", "✅ Already Verified")
        elif user_input == n:
            messagebox.showinfo("Success", "✅ Login Successful")
            verified = True
        else:
            messagebox.showerror("Error", "❌ Incorrect OTP")
    except ValueError:
        messagebox.showwarning("Warning", "⚠️ Enter a valid number")

# ✅ Resend OTP Function
def resendOTP():
    global n, verified
    n = random.randint(1000, 9999)
    verified = False
    send_otp()
    messagebox.showinfo("OTP", "🔄 OTP Resent")

# Buttons
tk.Button(root, text="Submit", font=('Arial', 12), command=checkOTP).pack(pady=10)
tk.Button(root, text="Resend OTP", font=('Arial', 12), command=resendOTP).pack(pady=5)

# ✅ Send first OTP when app opens (with error handling)
try:
    send_otp()
except Exception as e:
    print("[ERROR] During initial OTP sending:", e)

print("[DEBUG] Starting GUI...")

# ✅ Start GUI
root.mainloop() 
