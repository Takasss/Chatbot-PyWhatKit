from PySimpleGUI import PySimpleGUI as sg
from uteis import metodos


class TelaPython:
    def __init__(self):
        # Layout

        layout = [
            [sg.Image('imagem.png')],
            [sg.Text('Mensagem: ', size=(10, 0)), sg.Multiline(
                size=(30, 10), key='mensagem')],
            [sg.Button('Enviar')],
            [sg.Output(size=(50, 20), key='output')]
        ]

        # Janela

        self.janela = sg.Window(
            'Envio de mensagens via WhatsApp',element_justification='c').layout(layout)

        # Extrair os dados da tela

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            mensagem = self.values['mensagem']

            metodos.enviar_mensagem(mensagem)


tela = TelaPython()
tela.iniciar()
