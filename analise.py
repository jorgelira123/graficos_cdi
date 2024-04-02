import subprocess
from sys import argv

import extracao
import visualizacao

try:
    subprocess.run(['python', 'extracao.py'])
    subprocess.run(['python', f'visualizacao.py {argv[1]}'])
except Exception as exc:
    print('Erro, parando a execução.')
    raise exc
else:
    print('Arquivos criados com sucesso!')