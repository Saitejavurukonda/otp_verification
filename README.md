
# 🔐 OTP Verification System

A simple **OTP verification desktop app** built using **Python, Tkinter, and Twilio API**.  
Send and verify OTPs easily with a GUI interface.

---

## 📌 Features
- Generate **random 4-digit OTP**.
- Send OTP via **Twilio SMS API**.
- **Verify OTP** with instant success/error messages.
- **Resend OTP** functionality.
- GUI built with **Tkinter** for user-friendly experience.

---

## 🛠️ Technologies Used
- Python 3
- Tkinter (GUI)
- Twilio API (for sending SMS)

---

## ⚡ Getting Started
1. Clone this repository:

```bash
git clone https://github.com/your-username/otp-verification.git
````

2. Navigate to the project folder:

```bash
cd otp-verification
```

3. Install Twilio Python package if not installed:

```bash
pip install twilio
```

4. Open `otp_verification.py` and replace the placeholders:

```python
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_number = "YOUR_TWILIO_NUMBER"
recipient_number = "RECIPIENT_PHONE_NUMBER"
```

5. Run the app:

```bash
python otp_verification.py
```

---

## 💡 Notes

* Ensure your Twilio account is **active** and has **sufficient balance** to send SMS.
* The app works only if **internet is available**.
* Can be used for **login verification, authentication demos, or learning purposes**.

---

## 👨‍💻 Author

**Saiteja Vurukonda**
[GitHub Profile](https://github.com/Saitejavurukonda)

```
