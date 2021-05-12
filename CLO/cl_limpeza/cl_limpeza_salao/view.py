import PySimpleGUI as sg

def get_layout():
    frame_tarefas = [
        
        [
            sg.Text('Diária'),
        ],

        [
            sg.Output(
                size=(100,1),
                key='-TDS-',
            )
        ],

        [
            sg.Text('Semanal'),
        ],
        [
            sg.Output(
                size=(100,1),
                key='-TSS-',
            )
        ],     

        [
            sg.Text('Mensal'),
        ],
        [
            sg.Output(
                size=(100,1),
                key='-TMS-',
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
            sg.Button(
                'Voltar',
                key='-Back-'
                ),
            sg.Button('CheckList de Operação'),
        ],
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'CheckList Limpeza Salão',
        get_layout(),
    )    