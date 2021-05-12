#Definindo dia da semana e data
from datetime import datetime
dia_hoje = datetime.today().strftime('%A')
data_atual= datetime.today()
data_atual='{}'.format(data_atual.day)

#dados
segunda=['Geladeira Horizontal']
terca=['Geladeira Vertical']
quarta=['Armário Copos']
quinta=['Armário Bebidas']
sexta=['Máquina de Gelo']

diario =['Pia de Limpeza',
         'Pia de Apoio',
         'Bancadas',
         'Cafeteira',
         'Liquidificador',
         'Piso',
         'Ralo']

mensal = ['Luminárias','Trilhos']

dia=['Segunda','Terça','Quarta','Quinta','Sexta']
semana= [segunda,terca,quarta,quinta,sexta]

#Tarefas diárias
def tarefa_cllbd():
    for tarefa in diario:
      print(tarefa)

#Tarefas mensais
def tarefa_cllbm():
  if data_atual == '1':
    print('A tarefa mensal é:', mensal[0])
  elif data_atual == '15':
    print('A tarefa mensal é:', mensal[1])
  else:
    print('Não há tarefas mensais')

#Tarefas semanais
if dia_hoje == 'Monday':
    print('Tarefa da Segunda:',segunda)
elif dia_hoje == 'Tuesday':
  print('Tarefa da Terça:',terca)
elif dia_hoje == 'Wednesday':
  print('Tarefa da Quarta:',quarta)
elif dia_hoje == 'Thursday':
  print('Tarefa da Quinta:',quinta)
elif dia_hoje == 'Friday':
  print('Tarefa da Sexta:',sexta)
else:
  print('Dia de folga')
