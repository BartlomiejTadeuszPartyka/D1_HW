# Importy wszystkich modułów z folderu D1
from D2.multitool import Multitool


# importuje biblioteki
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(smtp_server: str= "smtp.interia.pl", smtp_port: int=465, login: str= "test_python@interia.pl",
               pwd:str= "testpython12345!", recipient:str= "test_python@interia.pl"):

    # przygotowuję maila z tematem treścią i odbiorcą
    msg = MIMEMultipart()
    msg["From"] = login
    msg["To"] = recipient
    msg["Subject"] = "Python SMTP"

    body = "Jeśli to czytasz, to znaczy, że mój program działa!"
    msg.attach(MIMEText(body, "plain"))

    print(msg.as_string())

    # tworze obiekt mailera
    # witam się z serwerem smtp – tworzę połączenie
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    try:
        # loguję się (podając login i hasło)
        server.login(login, pwd)
        # wysyłam maila
        server.send_message(msg)
        # kończę połączenie z serwerem
        server.quit()
        print(f"Wysłano wiadomość do {msg["To"]}")
    except Exception as e:
        print(e)

def main():
   # Multitool().mainloop()
    send_email()


if __name__ == "__main__":
    main()
