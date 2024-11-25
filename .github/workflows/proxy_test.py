import socket
import socks
import requests

# 定义代理账户信息
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

# Telegram 配置
telegram_token = "7056296159:AAGDFwNTx8OA0dzv1S0WN0CDh3iinBipeXs"
telegram_chat_id = 685294921

def send_tg_notification(message):
    """
    发送 Telegram 通知
    """
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            print("Telegram 通知发送成功")
        else:
            print(f"Telegram 通知发送失败: {response.text}")
    except Exception as e:
        print(f"Telegram 通知发送失败: {e}")

def test_socks5_connection(ip, port, username, password):
    """
    测试 SOCKS5 代理连接
    """
    original_socket = socket.socket
    try:
        # 设置 SOCKS5 代理
        socks.set_default_proxy(socks.SOCKS5, ip, port, True, username, password)
        socket.socket = socks.socksocket

        # 测试连接到公共地址
        test_socket = socket.create_connection(("www.google.com", 80), timeout=5)
        test_socket.close()
        print(f"成功连接到 {ip}:{port} ({username})")
        return True
    except Exception as e:
        print(f"连接失败 {ip}:{port} ({username}) - 错误: {e}")
        return False
    finally:
        # 恢复原始 socket
        socket.socket = original_socket

def main():
    all_failed = True  # 检查是否所有代理都失败

    for account in accounts:
        success = test_socks5_connection(account["ip"], account["port"], account["username"], account["password"])
        if success:
            all_failed = False

    # 如果所有代理都失败，发送 Telegram 通知
    if all_failed:
        send_tg_notification("所有代理测试均失败，请检查代理配置！")

if __name__ == "__main__":
    main()
