def request_google():
    import requests
    url = 'https://www.google.com'
    # url = "https://code.earthengine.google.com/"
    # url = "https://drive.google.com/drive/folders"
    html = requests.get(url).text
    print(html)


def set_socks5_proxy(ip, port):
    import socket
    import socks  # 需要安装PySocks
    socks.set_default_proxy(socks.SOCKS5, addr=ip, port=port)
    socket.socket = socks.socksocket


def set_http_proxy(ip, port):
    import socket
    import socks  # 需要安装PySocks
    socks.set_default_proxy(socks.HTTP, addr=ip, port=port)
    socket.socket = socks.socksocket


def main():
    set_socks5_proxy("127.0.0.1", 10808)
    request_google()


if __name__ == '__main__':
    main()