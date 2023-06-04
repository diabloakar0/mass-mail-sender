import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender_email = "mail@gmail.com"  # sender mail
sender_password = "password"  # sender 2fa pass
subject = "HTML E-posta"  # e mail subject

with open("email.html", "r") as file:
    html_content = file.read()

with open("mailler.txt", "r") as file: # mail list (mailler.txt)
    mailler = file.read().splitlines()

for mail in mailler:
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = mail
        msg["Subject"] = subject

        html_part = MIMEText(html_content, "html")
        msg.attach(html_part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, mail, msg.as_string())

        print(f"E-mail send: {mail}")
    except Exception as e:
        print(f"Error: {e}")

print("Email sending to all emails has been completed.")