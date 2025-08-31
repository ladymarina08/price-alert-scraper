import schedule
import time
from scraper.main import obter_preco_atual
from scraper.email_alert import enviar_email_alerta

URL_PRODUTO = "https://www.mercadolivre.com.br/100-pure-whey-zero-lactose-900-g-probiotica-sabor-morango/p/MLB39207420"
PRECO_ALVO = 120.00

def checar_preco():
    preco_atual = obter_preco_atual(URL_PRODUTO)
    if preco_atual:
        print(f"Preço atual: R${preco_atual:.2f}")
        if preco_atual <= PRECO_ALVO:
            print("💥 Alerta: O preço baixo! Compre já!")
            enviar_email_alerta(preco_atual, PRECO_ALVO, URL_PRODUTO)
        else:
            print("Ainda está caro...")

# Agendando para rodar a cada 12 horas
schedule.every(12).minutes.do(checar_preco)


print("⏰ Monitoramento de preços iniciado...")

while True:
    schedule.run_pending()
    time.sleep(60)
