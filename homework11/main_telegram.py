import telebot
import requests
with open('api_key_telegram.txt', 'r') as file:
    bot_token = file.read()
bot = telebot.TeleBot(bot_token)
with open('api_key.txt', 'r') as file:
    api_key = file.read()


def search_gif(search_term, api_key, num_results):
    url = (
        f'https://api.giphy.com/v1/gifs/search?'
        f'api_key={api_key}&q={search_term}&limit={num_results}'
    )
    response = requests.get(url)
    data = response.json()
    gif_urls = []
    if 'data' in data:
        for gif_data in data['data']:
            gif_url = gif_data['images']['original']['url']
            gif_urls.append(gif_url)
        return gif_urls
    else:
        return ["GIF не знайдено"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Привіт! Для пошуку GIF напиши категорію GIF яку хочеш отримати: \
""")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text:
        search_term = message.text
        num_results = 5
        gif_urls = search_gif(search_term, api_key, num_results)
        for i, gif_url in enumerate(gif_urls, start=1):
            bot.send_message(message.chat.id, f"{i}. {gif_url}")
