class Entradas:    
    @staticmethod
    def entrada_tratada_dia(mensagem) -> int:
        while True:
            try:
                dia = int(input(mensagem))
                if(dia >= 1 and dia <=31):
                    return dia
                print('Informe um valor numérico entre 1 e 31')
            except:
                print('Informe um valor numérico entre 1 e 31')
    
    @staticmethod
    def entrada_tratada_mes(mensagem) -> int:
        while True:
            try:
                mes = int(input(mensagem))
                if(mes >= 1 and mes <=12):
                    return mes
                print('Informe um valor numérico entre 1 e 12')
            except:
                print('Informe um valor numérico entre 1 e 12')
    
    @staticmethod
    def entrada_tratada_ano(mensagem) -> int:
        while True:
            try:
                ano = int(input(mensagem))
                if(ano > 0):
                    return ano
                print('Informe um valor numérico maior que 0')
            except:
                print('Informe um valor numérico maior que 0')

class UtilitarioData:
    @staticmethod
    def avancar_dia(data):
        data.dia += 1
        if(data.dia == 32):
            data.dia = 1
            data.mes += 1
        
        if (data.dia == 31 and data.mes not in (1,3,5,7,8,10,12)):
            data.dia = 1
            data.mes += 1
        
        if(data.mes == 4):
            if((data.ano % 4) != 0 and data.dia == 29):
                data.dia = 1
                data.mes += 1
            
            if(data.dia > 29):
                data.dia=1
                data.mes+=1
        
        if(data.mes > 12):
            data.mes = 1
            data.ano += 1
        
        return data

    @staticmethod
    def checa_data(data):
        if(data.dia == 31 and data.mes not in (1,3,5,7,8,10,12)):
            raise Exception("Dia inválido para o mês")
        if(data.mes==4):
            if(data.dia == 29 and (data.ano%4) != 0):
                raise Exception("Dia inválido para o mês")
            if(data.dia>=30):
                raise Exception("Dia inválido para o mês")
            
        return data

class Data:
    def __init__(self,dia,mes,ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

class Aplicacao():
    def aplicacao(self):
        while True:
            try:
                data = UtilitarioData.checa_data(Data(Entradas.entrada_tratada_dia("Digite o dia: "),Entradas.entrada_tratada_mes("Digite o mes: "),Entradas.entrada_tratada_ano("Digite o ano: ")))
                print(data)
                print(UtilitarioData.avancar_dia(data))
            except Exception as e:
                print(e)


app = Aplicacao()
app.aplicacao()
            