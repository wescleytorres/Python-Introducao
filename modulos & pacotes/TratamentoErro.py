import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não esta disponivel')
else:
    print('Consegui acessar!')