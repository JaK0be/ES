import re
import datetime

def pagar(): # Valor a pagar at� 5 d�gitos, excluindo os c�ntimos
    while True:
        valor = input('Valor a pagar: \n')
        if re.match("^[0-9]{1,5}\.[0-9]{2}$", valor):
            return valor
        else:
            print('Por favor insira o valor seguido dos c�ntimos (ex: 105.20)')

def dob(): # Data de nascimento (formato DD-MM-AAAA)
    while True:
        dob = input('Data de nascimento (dd/mm/aaaa): \n')
        isValid = False
        try:
            date = datetime.datetime.strptime(dob, '%d/%m/%Y')
            print("Date: " + str(date))
            today = datetime.datetime.today()
            if(date < today):
                return dob
            else:
                print("Data de nascimento deve estar no passado")
        except ValueError:
            print("Data de nascimento inv�lida, tente DD/MM/AAAA")

def nome(): # Nome (desde de que tenha pelo menos uma letra para primeiro e �ltimo nome, no m�ximo 6 nomes desde que comecem por letra mai�scula); cada nome pr�prio tem no m�ximo 10 caracteres; n�o permite "da Costa" por exemplo, ou deve escrever "Da Costa"
    while True:
        nome = input('Escreva o seu nome: \n')
        if re.match("^([A-Z][a-z]{0,9})(\s[A-Z][a-z]{0,9}){1,5}$", nome):
            return nome
        else:
            print("Escreva o nome no formato correto, deve ter pelo menos primeiro e �ltimo nome e devem come�ar por letra mai�scula")

def nif(): # N�mero de identifica��o fiscal
    while True:
        nif = input('Escreva o seu NIF (9 d�gitos): \n')
        if re.match("^[0-9]{9}$", nif):
            return nif
        else:
            print("Escreva o NIF no formato correto")

def nic(): # N�mero de identifica��o de cidad�o https://www.autenticacao.gov.pt/documents/20126/115760/Valida%C3%A7%C3%A3o+de+N%C3%BAmero+de+Documento+do+Cart%C3%A3o+de+Cidad%C3%A3o.pdf/bdc4eb37-7316-3ff4-164a-f869382b7053?t=1588780568207&download=true
    while True:
        nic = input('Escreva o seu n�mero de identifica��o de cidad�o:\n')
        if re.match("^[0-9]{8}\s[0-9]\s([A-Z]|[0-9]){2}[0-9]$", nic):
            return nic
        else:
            print("Escreva o seu NIC no formato correto")

def cardNr(): # Valida n�mero do cart�o
    while True:
        nr = input('Insira o seu n�mero de cart�o de cr�dito\n')
        if re.match("^[0-9]{14}$", nr):
            return nr
        else:
            print("Formato incorreto")

def dataValidade():
    while True:
        val = input('Insira a data de validade do cart�o:\n')
        if re.match("^(0[6-9]/20|(0[1-9]|[1][0,1,2])/2[1-6])$", val):
            return val
        else:
            print("Formato ou data inv�lida, tente MM/AA")

def cvv():
    while True:
        cvv = input('Insira o seu CVC/CVV:\n')
        if re.match("^[0-9]{3,4}$", cvv):
            return cvv
        else:
            print("Formato inv�lido, tente novamente")

def credito(): # Nr. cart�o de cr�dito, validade e CVC/CVV
    nc = cardNr()
    dv = dataValidade()
    c = cvv()
    return nc, dv, c

def main():
    p = pagar()
    d = dob()
    n = nome()
    nifs = nif()
    nics = nic()
    a, b, d = credito()

    print("Recolhidos todos os dados\n")
    print("Mostrando dados recolhidos: \n")
    print("Valor a pagar: " + p)
    print("Data de nascimento: " + d)
    print("Nome: " + n)
    print("NIF: " + nifs)
    print("NIC: " + nics)
    print("Cart�o de cr�dito nr.: " + a + " de validade " + b + " e CVC/CVV " + d)


main()