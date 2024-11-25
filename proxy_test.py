
import socket
import socks
import requests

# Telegram 配置
telegram_token = "7056296159:AAGDFwNTx8OA0dzv1S0WN0CDh3iinBipeXs"
telegram_chat_id = 685294921

# 代理账户信息
accounts = [
    {"ip": "s7.090227.xyz", "username": "i5x0cgri", "password": "CMLiussss", "port": 39339},
    {"ip": "s7.090227.xyz", "username": "6bjal1m9", "password": "CMLiussss", "port": 39340},
    {"ip": "s7.090227.xyz", "username": "1t2khnt5", "password": "CMLiussss", "port": 39341},
    {"ip": "s8.090227.xyz", "username": "xgsewxm1", "password": "CMLiussss", "port": 39339},
    {"ip": "s8.090227.xyz", "username": "05sys275", "password": "CMLiussss", "port": 39340},
    {"ip": "s8.090227.xyz", "username": "itytv5x0", "password": "CMLiussss", "port": 39341},
    {"ip": "s9.090227.xyz", "username": "eor5c9j3", "password": "CMLiussss", "port": 39339},
    {"ip": "s10.serv00.com", "username": "123", "password": "123", "port": 55749},
    {"ip": "herewwsag.serv00.net", "username": "4ZuDEltoos", "password": "2MpAFfnn0b", "port": 8868},
    {"ip": "lqilqi123456.serv00.net", "username": "TyqNCZ7CXs", "password": "JZ51BaGr3S", "port": 5688},
]

def test_socks5_connection(ip, port, username, password):
    try:
        socks.set_default_proxy(socks.SOCKS5, ip, port, True, username, password)
        socket.socket = socks.socksocket
        # 测试连接到 Google
        test_socket = socket.create_connection(("www.google.com", 80), timeout=5)
        test_socket.close()
        return True
    except Exception as e:
        return False

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Telegram 通知发送成功！")
    except Exception as e:
        print(f"发送 Telegram 通知失败: {e}")

if __name__ == "__main__":
    all_failed = True
    for account in accounts:
        success = test_socks5_connection(account["ip"], account["port"], account["username"], account["password"])
        if success:
            all_failed = False
            print(f"成功连接到 {account['ip']}:{account['port']} ({account['username']})")
        else:
            print(f"连接失败 {account['ip']}:{account['port']} ({account['username']})")

    if all_failed:
        send_telegram_message("所有代理连接均失败，请检查相关配置！")
