import requests

BOT_TOKEN = '5258919405:AAHdr_uKAvwNhrYyaL4w80-YSYQM-zlIWio'
GROUP_CHAT_ID = "-1001725929489"
USER_ID = "104566710"


def send_user_data_to_group(user, product):
    text = f"\nПользователь: {user.get('name')} \nЭл. адрес: {user.get('email')} \nТелефон: {user.get('phone')}"
    text += f"\nТовар: {product} \nТовар ID: {user.get('product_id')}"
    send_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&text={text}"
    resp = requests.get(send_text)
    return

