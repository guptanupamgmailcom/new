import socket

def port_scan(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)
  try:
    s.connect((host, port))
    print(f"Port {port} is open")
  except:
    print(f"Port {port} is closed")

    s.close()
host = "192.168.42.50"
for port in range(20, 30):
  port_scan(host, port)