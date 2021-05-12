
import csv
from os.path import isfile

def initialize(menu):
    from CLO.cl_limpeza import Menu_CLL

    MenuL = Menu_CLL(menu)
    MenuL.enable_window()

def import_CL(csv_path):
    if not isfile(csv.path):
        return -1
    
    with open(csv_path,'r', encoding='utf-8') as csv_file:
        dialec = csv.Sniffer().sniff(csv.read(1024))
        csv_file.seek(0)

        reader = csv.DictReader(csv_file, dialect=dialec)

        if not 'Atividade' in reader.fieldnames or not 'Periodicidade' in reader.fieldnames:
            return 0


    


