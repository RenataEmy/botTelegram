import telebot
from regex import dadosRegex
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)



def supply_data():
    pass    

@bot.message_handler(commands=["Solicitar"])
def request(mensage):
    text = '''Para realizar um agendamento, por gentiliza nos informe os dados solicitados'''
    bot.reply_to(mensage, text)
    #supply_data() chamar função para incluir os dados

@bot.message_handler(commands=["Alterar"])
def change(mensage):
    pass

@bot.message_handler(commands=["Cancelar"])
def cancel(mensage):
    pass

@bot.message_handler(commands=["Encerrar"])
def close(mensage):
    pass


def check(mensage):
    return True

@bot.message_handler(func=check)
def respond(mensage):
    text = '''
    Olá! Seja bem-vindo ao atendimento da clínica. 
Selecione a opção desejada:
    /Solicitar agendamento
    /Alterar agendamento
    /Cancelar agendamento
    /Encerrar atendimento
Responder qualquer outra coisa não irá funcionar. 
'''
    bot.reply_to(mensage, text)

bot.polling()