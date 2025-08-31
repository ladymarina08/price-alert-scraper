import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

remetente = os.getenv("EMAIL_REMETENTE")
senha = os.getenv("EMAIL_SENHA")
destinatario = os.getenv("EMAIL_DESTINATARIO")


def enviar_email_alerta(preco, preco_alvo, url_produto):
   
    #Email
    assunto = "💥 O Whey baixou de preço!"
    corpo = f"""
    Olá, minha marombinha favorita! 😎💪

    O whey que você está monitorando caiu de preço!

    🔻 Preço atual: R${preco:.2f}
    🎯 Preço desejado: R${preco_alvo:.2f}

    Corre lá: {url_produto}

    🤖
    """

    #Criação da mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
            print("Email enviado.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")