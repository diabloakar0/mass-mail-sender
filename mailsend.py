import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time

sender_email = "mail@gmail.com"  # gönderen e-posta
sender_password = "password"  # gönderen 2FA parolası
subject = "HTML E-posta"  # e-posta konusu

with open("email.html", "r") as file:
    html_content = file.read()

with open("mailler.txt", "r") as file: # mail listesi (mailler.txt)
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

        print(f"E-posta gönderildi: {mail}")

#        time.sleep(60)  Attıktan sonra beklemesini istiyorsan "#" ı sil ve "60" yerine beklenecek saniyeyi gir.

    except Exception as e:
        print(f"Hata: {e}")

print("Tüm e-postaların gönderimi tamamlandı.")
