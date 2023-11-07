import urllib
import urllib.request

try:
    site_pudim = urllib.request.urlopen('http://www.pudim.com.br')
    print('\033[32mO site pudim está em acesso disponivel.\033[m')
except urllib.error.URLError:
    print('\033[31mO site pudim não está em acesso diponivel no momento.\033[m')
