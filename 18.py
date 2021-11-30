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

class Carro:
    def __init__(self, consumo:float) -> None:
        self.consumo = consumo
        self.combustivel = 0

    def obter_gasolina(self):
        return self.combustivel
    
    def adicionar_gasolina(self, litros):
        self.combustivel+=litros
    
    def consumir_gasolina(self, distância):
        if(self.combustivel < distância*self.consumo):
            raise Exception("Não há gasolina suficiente para esta distância")
        self.combustivel -= (distância*self.consumo)

    def rodar(self, distancia):
        try:
            self.consumir_gasolina(distancia)
            print(f'Foram percorridos {distancia} Km')
        except Exception as e:
            print(e)

class CarroService:
    def __init__(self, carro: Carro) -> None:
        self.carro = carro

    def obter_gasolina(self):
        print(f'A quantidade restante de gasolina é de: {self.carro.obter_gasolina()}')

    def adicionar_gasolina(self):
        self.carro.adicionar_gasolina(Utilidades.entrada_tratada_int("Digite os litros a serem abastecidos: "))
    
    def rodar(self):
        self.carro.rodar(Utilidades.entrada_tratada_float("Digite a kilometragem que será percorrida: "))

class Menu():
    def __init__(self, carro_service: CarroService) -> None:
        self.carro_service = carro_service
    
    def menu(self):
        while True:
            entrada = input("\nMENU\n1.Mostrar gasolina restante\n2.Adicionar gasolina\n3.Rodar com o carro\n")
            if(entrada == '1'):
                self.carro_service.obter_gasolina()
            elif(entrada == '2'):
                self.carro_service.adicionar_gasolina()
            elif(entrada == '3'):
                self.carro_service.rodar()

class Inicializador:
    def inicializar(self) -> Menu:
        return Menu(CarroService(Carro(Utilidades.entrada_tratada_float("Digite o consumo do carro em Km por Litro: "))))

class Aplicacao:
    def __init__(self) -> None:
        self.menu = Inicializador().inicializar()
    
    def aplicacao(self):
        self.menu.menu()

app = Aplicacao()
app.aplicacao()