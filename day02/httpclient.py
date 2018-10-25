import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))
request = "GET / HTTP/1.1\r\n"
request += 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36\r\n'
request += 'Cookie: session=eyJiYWlkdSI6InB5dGhvbiIsInRhb2JhbyI6InJ1YnkifQ.Dq69QQ.FWXpgTewamjN6sqUELVZH87k_x4\r\n\r\n'

client.send(request.encode())
recv_data = client.recv(4096)
print(recv_data)
client.close()
