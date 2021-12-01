from typing import List
from utilidades import Utilidades

class Aluno:
    def __init__(self, nota_1: float, nota_2: float) -> None:
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.gerar_media(nota_1, nota_2)

    def gerar_media(self, nota_1, nota_2):
        self.media = (nota_1+nota_2)/2

alunos = []

def recebe_notas():
    for i in range(5):
        alunos.append(Aluno(Utilidades.entrada_tratada_float(f'Digite a primeira nota do aluno {i}: '), Utilidades.entrada_tratada_float(f'Digite a segunda nota do aluno {i}: ')))
    print([j.media for j in alunos])
    print([j.media for j in alunos if j.media>=7]) 

recebe_notas()