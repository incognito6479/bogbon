import requests
from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
GROUP_CHAT_ID = env('GROUP_CHAT_ID')


def send_user_data_to_group(user, product):
    text = f"\nПользователь: {user.get('name')} \nЭл. адрес: {user.get('email')} \nТелефон: {user.get('phone')}"
    text += f"\nТовар: {product} \nТовар ID: {user.get('product_id')}"
    send_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&text={text}"
    resp = requests.get(send_text)
    return

