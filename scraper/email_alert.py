import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email_alerta(preco, preco_alvo, url_produto):
    #Configs
    remetente = "marina.takeda08@gmail.com"
    senha = "nvic ahvo idkc qwqy"
    destinatario = "lindinha08ex@gmail.com"

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