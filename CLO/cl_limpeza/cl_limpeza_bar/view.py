from CLO.cl_limpeza.cl_limpeza_bar.manager import load_TLDB, load_TLSB, load_TLMB
import PySimpleGUI as sg

TLDB = load_TLDB()
TLSB = load_TLSB()
TLMB = load_TLMB()

def get_layout():
    frame_tarefas = [
        [
            sg.Text('Diária'),
        ],

        [
            sg.Multiline(
                TLDB,
            )
        ],

        [
            sg.Text('Semanal'),
        ],

        [
            sg.Multiline(
                TLSB,
            )
        ],    

        [
            sg.Text('Mensal'),
        ],

        [
            sg.Multiline(
                TLMB,
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
                key='-Back-',
                ),
            sg.Button(
                'CheckList de Operação',
                key='-CLO-',
                ),
        ],
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'CheckList Limpeza Bar',
        get_layout(),
    )
