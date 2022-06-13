import pywhatkit
from datetime import datetime
from time import sleep
import keyboard

def fechar_guia():
    #Gerar um comando de 'CTRL' + 'W' para fechar a guia do navegador

    keyboard.press_and_release('ctrl + w')

def carregar_lista():
    #Carregar lista de contatos no array 'lista'

    try:
        lista = list()
        with open('contatos.txt', 'r') as arq:
            for valor in arq:
                if '+55' in valor:
                    lista.append(valor.replace('\n', ''))
                else:
                    print(f'O número {valor} não foi adicionado.')
    except:
        print('Erro ao localizar o arquivo!')
    finally:
        arq.close()
    return lista


def enviar_mensagem(msg='Olá'):
    #Realiza o envio de mensagem para os contatos

    lista = carregar_lista()
    cont = 0
    listaSucesso = list()
    listaFalha = list()

    while cont < len(lista):
        try:
            print(f'Enviando para: {lista[cont]}')
            pywhatkit.sendwhatmsg(lista[cont], msg,
                                  datetime.today().hour, datetime.today().minute + 1, wait_time=10)
        except:
            print(f'Falha ao enviar para: {lista[cont]}')
            listaFalha.append(lista[cont])
            cont += 1
            continue
        else:
            listaSucesso.append(lista[cont])
            sleep(5)
            fechar_guia()

            # Caso seja o último item da lista, não precisará contar até 60s
            if cont == len(lista) - 1:
                print('\n\n-> Mensagens enviadas!')
                print(
                    f'Envios realizados com sucesso: {listaSucesso}')
                print(f'Falha no envio: {listaFalha}')
                break

            sleep(60)
            cont += 1
