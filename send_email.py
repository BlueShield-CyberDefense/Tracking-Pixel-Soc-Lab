import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "ahmedtarek00tech@gmail.com"
recipient = "ahmedtarek00tech@gmail.com"
app_password = "PUT YOUR APP PASSWORD HERE"

with open("email.html", "r") as f:
    html_content = f.read()

msg = MIMEMultipart("alternative")
msg["Subject"] = "Security Alert – Tracking Pixel Test"
msg["From"] = sender
msg["To"] = recipient

msg.attach(MIMEText(html_content, "html"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, app_password)
    server.sendmail(sender, recipient, msg.as_string())

print("Email sent successfully!")
