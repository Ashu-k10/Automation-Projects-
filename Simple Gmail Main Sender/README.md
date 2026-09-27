# 📧 Simple Gmail Mail Sender using Python

A simple Python program to send emails using **Gmail's SMTP server** and Python's built-in `smtplib` and `email` modules.

This project demonstrates how to establish a secure SMTP connection with Gmail, authenticate using a **Google App Password**, and send an email programmatically.

---

## 🚀 Features

- 📩 Send emails using Python
- 🔐 Secure Gmail SMTP connection using SSL
- 🔑 Supports Gmail App Password authentication
- 📨 Custom sender, receiver, subject, and body
- 🐍 Uses only Python standard libraries
- ⚡ Simple and beginner-friendly implementation

---

## 🛠️ Technologies Used

- **Python 3**
- `smtplib`
- `email.message.EmailMessage`
- Gmail SMTP Server

### Gmail SMTP Configuration

| Setting | Value |
|---|---|
| SMTP Server | `smtp.gmail.com` |
| Port | `465` |
| Security | SSL |
| Authentication | Gmail App Password |

---

## 📁 Project Structure

```text
Simple-Gmail-Mail-Sender/
│
├── gmail_sender.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

This project uses only Python's built-in libraries, so **no external packages are required**.

### Python Version

Python **3.8+** is recommended.

You can check your Python version using:

```bash
python3 --version
```

---

## 🔐 Gmail App Password Setup

You should **not use your normal Gmail password** in the Python program.

Instead, create a **Google App Password**.

### Steps

1. Enable **2-Step Verification** on your Google Account.
2. Open your Google Account security settings.
3. Go to **App Passwords**.
4. Create a new App Password.
5. Copy the generated 16-character password.
6. Use that password in your Python program.

> ⚠️ **Important:** Never upload your App Password to GitHub or share it publicly.

---

## 💻 Code

```python
import smtplib
from email.message import EmailMessage


def send_mail(sender, app_password, receiver, subject, body):

    # Create email object
    msg = EmailMessage()

    # Set email headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Add email body
    msg.set_content(body)

    # Create secure SMTP SSL connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login using Gmail and App Password
    smtp.login(sender, app_password)

    # Send email
    smtp.send_message(msg)

    # Close SMTP connection
    smtp.quit()


def main():

    sender_email = "your_email@gmail.com"

    # Use your Gmail App Password
    app_password = "xxxx xxxx xxxx xxxx"

    receiver_email = "receiver@gmail.com"

    subject = "Test Mail from Python Script"

    body = """Hello,

This is a test email sent using Python.

Regards,
Python Gmail Sender
"""

    send_mail(
        sender_email,
        app_password,
        receiver_email,
        subject,
        body
    )

    print("Mail sent successfully!")


if __name__ == "__main__":
    main()
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Simple-Gmail-Mail-Sender.git
```

### 2. Navigate to the Project

```bash
cd Simple-Gmail-Mail-Sender
```

### 3. Run the Python Script

```bash
python3 gmail_sender.py
```

If everything is configured correctly, you should see:

```text
Mail sent successfully!
```

---

## 📧 How It Works

The program follows these steps:

```text
Python Program
      │
      ▼
Create EmailMessage
      │
      ▼
Set From / To / Subject
      │
      ▼
Add Email Body
      │
      ▼
Connect to Gmail SMTP
      │
      ▼
smtp.gmail.com:465
      │
      ▼
Login using App Password
      │
      ▼
Send Email
      │
      ▼
Close SMTP Connection
```

---

## 🔍 Important Python Components

### `smtplib`

Python's built-in `smtplib` module is used to communicate with an SMTP server.

```python
import smtplib
```

In this project, it connects to Gmail:

```python
smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
```

---

### `EmailMessage`

`EmailMessage` is used to construct the email.

```python
from email.message import EmailMessage
```

The message headers are configured using:

```python
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
```

The body is added using:

```python
msg.set_content(body)
```

---

### `SMTP_SSL`

The program uses:

```python
smtplib.SMTP_SSL()
```

This creates an SSL-encrypted connection directly to Gmail's SMTP server.

Port:

```text
465
```

---

### Authentication

The program authenticates using:

```python
smtp.login(sender, app_password)
```

The `app_password` should be a **Google App Password**, not your normal Gmail password.

---

## 🔒 Security Best Practices

### ❌ Don't do this

Never upload credentials directly to GitHub:

```python
app_password = "abcd efgh ijkl mnop"
```

### ✅ Better Approach

Use environment variables:

```python
import os

sender_email = os.getenv("GMAIL_EMAIL")
app_password = os.getenv("GMAIL_APP_PASSWORD")
```

Then configure them in your environment.

For example:

```bash
export GMAIL_EMAIL="your_email@gmail.com"
export GMAIL_APP_PASSWORD="your_app_password"
```

This prevents sensitive credentials from being stored directly in your source code.

---

## ⚠️ Common Errors

### `SMTPAuthenticationError`

Possible causes:

- Incorrect email address
- Incorrect App Password
- 2-Step Verification is not enabled
- App Password was revoked
- Wrong Gmail account

---

### `ConnectionRefusedError`

Check:

- Internet connection
- SMTP server address
- SMTP port

Correct configuration:

```text
Server: smtp.gmail.com
Port: 465
Protocol: SSL
```

---

### `ModuleNotFoundError`

The project uses only Python standard libraries, so normally you don't need to install anything with `pip`.

Make sure Python is installed correctly:

```bash
python3 --version
```

---

## 📦 Requirements

No external Python packages are required.

`requirements.txt` can therefore remain empty, or you can document that the project uses Python standard libraries only.

---

## 🔮 Future Improvements

Possible improvements for this project:

- [ ] Send HTML emails
- [ ] Add CC and BCC support
- [ ] Add file attachments
- [ ] Support multiple recipients
- [ ] Read credentials from `.env`
- [ ] Add email templates
- [ ] Add error handling
- [ ] Add logging
- [ ] Build a command-line interface
- [ ] Create a GUI email sender
- [ ] Support scheduled emails

---

## 👨‍💻 Author

**Ashutosh Kadu**

Python | Machine Learning | Automation 

---

## 📄 License

This project is created for **educational and learning purposes**.
