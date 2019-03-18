import psutil
import platform
import socket

def processador():
    freq_proc = psutil.cpu_freq()
    print('- INFORMAÇÕES SOBRE O PROCESSADOR')
    print('    Processador:', platform.processor())
    print('    Sistema Operacional:', platform.platform(terse='true'))
    print('    Arquitetura do processador:', platform.machine())
    print('    Percentual de uso da CPU:', psutil.cpu_percent(interval=1), '%')
    print('    Frequência máxima da CPU:', freq_proc.max/1000, 'GHz')

def memoria():
    mem = psutil.virtual_memory()
    print('- INFORMAÇÕES SOBRE A MEMÓRIA PRINCIPAL')
    print('    Capacidade total:', round(mem.total/(1024**3), 2), 'GB')
    print('    Capacidade disponível:', round(mem.available/(1024**3), 2), 'GB')

def disco():
    disco = psutil.disk_usage('.')
    print('- INFORMAÇÕES SOBRE O DISCO')
    print('    Capacidade total do disco:', round(disco.total/(1024**3), 2), 'GB')
    print('    Quantidade em uso do disco:', round(disco.used/(1024**3), 2), 'GB')
    print('    Quantidade livre do disco:', round(disco.free/(1024**3), 2), 'GB')
    print('    Percentual de disco usado:', disco.percent, '%')

def rede():
    ip = socket.gethostbyname('www.google.com')
    print('- INFORMAÇÕES SOBRE O IP')
    print('    Endereço IP:', ip)

def resumo():
    freq_proc = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    disco = psutil.disk_usage('.')
    ip = socket.gethostbyname('www.google.com')
    print('- RESUMO')
    print('    Processador:', platform.processor())
    print('    Sistema Operacional:', platform.platform(terse='true'))
    print('    Frequência máxima da CPU:', freq_proc.max / 1000, 'GHz')
    print('    Capacidade total da memória principal:', round(mem.total / (1024 ** 3), 2), 'GB')
    print('    Capacidade total do disco:', round(disco.total / (1024 ** 3), 2), 'GB')
    print('    Quantidade livre do disco:', round(disco.free / (1024 ** 3), 2), 'GB')
    print('    Endereço IP:', ip)

print('----------------------------------------------------------------------------------------')
processador()
print('----------------------------------------------------------------------------------------')
memoria()
print('----------------------------------------------------------------------------------------')
disco()
print('----------------------------------------------------------------------------------------')
rede()
print('----------------------------------------------------------------------------------------')
resumo()
print('----------------------------------------------------------------------------------------')