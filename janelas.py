from PySimpleGUI import PySimpleGUI as sg

#Layout da Interface Gráfica - Criando Janela de Login, Janela Intermediária e Janela Final
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Checkbox('Deseja salvar seu login?')],
        [sg.Button('Entrar')]
    ]
    return sg.Window('Tela Login', layout=layout, finalize=True)

def janela_intermediaria():
    sg.theme('Reddit')
    layout= [
        [sg.Text('Bem-vindo')],
        [sg.Text('Para finalizar, clique no botão "Sair')],
        [sg.Button('Sair')]
    ]
    return sg.Window('Janela Intermediária', layout=layout, finalize=True)

def janela_final():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Programa Finalizado')]
    ]
    return sg.Window('Janela Final', layout=layout, finalize=True)

#Criando Janelas
janela1, janela2, janela3 = janela_login(), None, None

#Lendo Eventos
#Looping Infinito - O Programa precisa estar lendo o que acontece, por isso o loop 'while True:'
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if event == sg.WIN_CLOSED:
        break

    #Próxima Janela
    if window == janela1 and event == 'Entrar':
        if values['usuario'] == 'usuario' and values['senha'] == 'senha':
            janela2 = janela_intermediaria()
            janela1.hide()

    if window == janela2 and event == 'Sair':
        janela3 = janela_final()
        janela2.hide()



