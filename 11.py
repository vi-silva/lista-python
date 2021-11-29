# Não esta funcionando conforme esperado
# A ideia seria uma anotação que trata erros apenas mostrando o erro
def tratamento_de_erro(func):
    try:
        return func
    except Exception as e:
        print(e)

class Utilidades:
    @staticmethod
    def entrada_tratada_int(mensagem):
        while True:
            try:
                return int(input(mensagem))
            except:
                print('Informe um valor numérico')

    @staticmethod
    def entrada_tratada_float(mensagem):
        while True:
            try:
                return float(input(mensagem))
            except:
                print('Informe um valor numérico')

class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self._tipo_combustivel = tipo_combustivel
        self._quantidade_combustivel = quantidade_combustivel
        self._valor_litro = valor_litro

    def abastecer_por_valor(self, valor) -> float:
        try:
            litros = valor/self._valor_litro
            self.alterar_litros(litros)
            return litros
        except Exception as e:
            print(e)
    
    def abastecer_por_litro(self, litros) -> float:
        try:
            self.alterar_litros(litros)
            return litros*self._valor_litro
        except Exception as e:
            print(e)
    
    def alterar_valor(self, valor):
        self._valor_litro = valor
    
    def alterar_combustivel(self, combustivel):
        self._tipo_combustivel = combustivel
    
    def altera_quantidade_combustivel(self, quantidade):
        try:
            if(quantidade<=0):
                raise Exception("Digite um valor maior que zero")
            self._quantidade_combustivel = quantidade
        except Exception as e:
            print(e)

    def alterar_litros(self, litros):
        if(self.quantidade_combustivel < litros):
            raise Exception("Não há quantidade suficiente de combustivel")
        self._quantidade_combustivel-=litros

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @property
    def quantidade_combustivel(self):
        return self._quantidade_combustivel
    
    @property
    def valor_litro(self):
        return self._valor_litro

class BombaService:
    def __init__(self, bomba: BombaDeCombustivel):
        self.bomba = bomba
    
    def abastecer_por_litro(self):
        litros = Utilidades.entrada_tratada_int("Quantos litros serão abastecidos: ")
        print(f'O valor será de: {self.bomba.abastecer_por_litro(litros)}')

    def abastecer_por_valor(self):
        valor = Utilidades.entrada_tratada_float("Qual valor será abastecido: ")
        print(f'A quantidade de litros será de: {self.bomba.abastecer_por_valor(valor)}')

    def alterar_valor_litro(self):
        valor = Utilidades.entrada_tratada_float("Qual será o novo valor:")
        self.bomba.alterar_valor(valor)
        print(f'O novo valor será de: {valor}')

    def alterar_tipo_combustivel(self):
        tipo = input("Insira o tipo de combustível: ")
        self.bomba.alterar_combustivel(tipo)
        print(f'O novo tipo de combustível é de: {tipo}')

    def alterar_quantidade_litros(self):
        litros = Utilidades.entrada_tratada_int("Insira a quantidade de litros na bomba: ")
        self.bomba.altera_quantidade_combustivel(litros)
        print(f'A nova quantidade de litros na bomba é de {self.bomba.quantidade_combustivel}')

class Menu:
    def __init__(self, bomba):
        self._bomba_service: BombaService = bomba

    def menu(self):
        while True:
            entrada = input("\nMENU\n1.Abastecer por valor\n2.Abastecer por litro\n3.Alterar valor do litro\n4.Alterar tipo de combustivel\n5.Alterar quantidade de litros\n")
            if(entrada == '1'):
                self._bomba_service.abastecer_por_valor()
            elif(entrada == '2'):
                self._bomba_service.abastecer_por_litro()
            elif(entrada == '3'):
                self._bomba_service.alterar_valor_litro()
            elif(entrada == '4'):
                self._bomba_service.alterar_tipo_combustivel()
            elif(entrada == '5'):
                self._bomba_service.alterar_quantidade_litros()

class Inicializador():
    def inicializador(self) -> Menu:
        return Menu(
            BombaService(
                BombaDeCombustivel(
                    input("Insira o tipo de combustível: "),
                    Utilidades.entrada_tratada_float("Insira o valor do combustível: "), 
                    Utilidades.entrada_tratada_int("Insira a quantidade inicial de combustível: "))))


class Aplicacao:
    def __init__(self):
        self.inicializador = Inicializador()

    def aplicacao(self):
        menu = self.inicializador.inicializador()
        menu.menu()

app = Aplicacao()
app.aplicacao()
    