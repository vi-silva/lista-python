from typing import List

# 7 10 11 18


class Utilidades:
    @staticmethod
    def media(lista):
        x = 0
        y = 0
        for nota in lista:
            x+=nota
            y+=1
        return x/y

    @staticmethod
    def entrada_tratada_float(mensagem):
        while True:
            try:
                return float(input(mensagem))
            except:
                print('Informe um valor numérico')

class Aluno:
    def __init__(self):
        self.notas: List[float] = []
        self.media = float
    
class Aplicacao:
    def aplicacao(self):
        turma : List[Aluno] = []
        while True:
            turma.append(Aluno())
            turma[-1].notas.append(Utilidades.entrada_tratada_float("Entre com a primeira nota do aluno:"))
            turma[-1].notas.append(Utilidades.entrada_tratada_float("Entre com a segunda nota do aluno:"))
            turma[-1].notas.append(Utilidades.entrada_tratada_float("Entre com a terceira nota do aluno:"))
            turma[-1].notas.append(Utilidades.entrada_tratada_float("Entre com a quarta nota do aluno:"))
            turma[-1].media = Utilidades.media(turma[-1].notas)
            print(f'A média deste aluno é: {turma[-1].media}')
            if(input("-----------------\nDeseja adicionar outro aluno?\ns-Sim\nn-Não\n") != "s"):
                return

app = Aplicacao()
app.aplicacao()



        