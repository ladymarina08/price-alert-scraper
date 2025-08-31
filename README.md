# 📉 Price Alert Scraper – Monitoramento de Preço no Mercado Livre

Este projeto é um **web scraper em Python** que monitora o preço de um produto específico no Mercado Livre e **envia um alerta por e-mail** automaticamente quando o valor fica abaixo de um limite definido.

Ideal para economizar em compras e aprender scraping + automação + envio de e-mails em Python! 🛍️💌

---

## ✨ Funcionalidades

- 🔍 Acessa automaticamente a página de um produto
- 📦 Extrai o preço atual com BeautifulSoup
- 🎯 Compara com um preço-alvo definido
- 📬 Envia um e-mail de alerta quando o preço cair
- ⏰ Pode ser agendado para rodar automaticamente (schedule ou GitHub Actions)

---

## 🛠️ Tecnologias utilizadas

| Categoria      | Ferramentas                      |
|----------------|----------------------------------|
| Web Scraping   | `requests`, `BeautifulSoup`      |
| E-mail         | `smtplib`, `email.mime`          |
| Agendamento    | `schedule`                       |
| Outras libs    | `time`, `os`, `dotenv` (opcional)|
| Deploy         | Local ou GitHub Actions          |

---

## 🚀 Como rodar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/price-alert-scraper.git
cd price-alert-scraper
```

2. **Crie e ative o ambiente virtual:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Edite as configurações em `email_alert.py`:**

Preencha seu e-mail e a senha de app (Gmail):

```python
remetente = "seuemail@gmail.com"
senha = "sua_senha_de_app"
destinatario = "seuemail@gmail.com"
```

⚠️ Recomendado: crie um arquivo `.env` para esconder dados sensíveis

5. **Execute o script:**

```bash
python run.py
```

---

## ✉️ Exemplo de e-mail enviado

```
💥 O Whey baixou de preço!

🔻 Preço atual: R$129.00
🎯 Preço desejado: R$139.00

Corre lá: https://www.mercadolivre.com.br/...
```

---

## 🧠 Próximos passos (em construção)

- [ ] Agendamento com GitHub Actions
- [ ] Armazenar histórico de preços em CSV ou banco de dados
- [ ] Suporte para múltiplos produtos

---

## 🙋‍♀️ Desenvolvido por

**Marina Takeda**  
✨ Python Júnior Developer em formação  

