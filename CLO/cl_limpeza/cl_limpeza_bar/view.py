import PySimpleGUI as sg

def get_layout():
    frame_tarefas = [

        [
            sg.Text('Diária'),
        ],

        [
            sg.Output(
                size=(100,1),
                key='-TDB-',
            )
        ],

        [
            sg.Text('Semanal'),
        ],

        [
            sg.Output(
                size=(),
                key='-TSB-',
            )
        ],

        [
            sg.Text('Mensal'),
        ],

        [
            sg.Output(
                size=(),
                key='-TMB-',
            )
        ],
    ]

    layout = [
        [
            sg.Frame(
                'Tarefas',
                frame_tarefas,
            )
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
        'CheckList Limpeza Bar',
        get_layout(),
    )