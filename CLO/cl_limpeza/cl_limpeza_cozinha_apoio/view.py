import PySimpleGUI as sg

def get_layout():
    frame_tarefas = [
        [
            sg.Text('Diária'),
        ],
        [
            sg.Output(
                size=(100,1),
                key='-TDC-',
            )
        ],

        [
            sg.Text('Semanal'),
        ],
        [
            sg.Output(
                size=(100,1),
                key='-TSC-',
            )
        ],     

        [
            sg.Text('Mensal'),
        ],
        [
            sg.Output(
                size=(100,1),
                key='-TMC-',
            )
        ],
    ]

    layout = [
        
        [
            sg.Frame(
                'Tarefas',
                frame_tarefas,
            ),
        ],

        [
            sg.Button('Voltar'),
            sg.Button('CheckList de Operação'),
        ],
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'CheckList Limpeza Cozinha de Apoio',
        get_layout(),
    )
