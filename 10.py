from typing import List


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

class Funcionario:
    def __init__(self, nome, salario ) -> None:
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual_aumento):
        self.salario += (self.salario/100)*percentual_aumento

    def __str__(self) -> str:
        return f'Funcionário: {self.nome}\nSeu salário é de: {self.salario}'

class Aplicacao:
    def aplicacao(self):
        menu = Menu()
        menu.menu()

class FuncionarioRepositorio:
    def __init__(self) -> None:
        self.funcionarios: List[Funcionario] = []

    def funcionario_por_id(self, id):
        return self.funcionarios[id]
    

class Menu:
    def __init__(self) -> None:
        self._funcionario_repositorio = FuncionarioRepositorio()

    def menu(self):
        while True:
            opcao = input("\nMENU\n1.Cadastrar funcionário\n2.Aumentar salario\n")
            if(opcao == '1'):
                self.entrada_funcionario()
            elif(opcao == '2'):
                self.aumentar_salario()

    def entrada_funcionario(self):
        print("Entre com o Funcionário: ")
        funcionario = Funcionario(input("Digite o nome do funcionário: "), Utilidades.entrada_tratada_float("Digite o valor do salário: "))
        self._funcionario_repositorio.funcionarios.append(funcionario)
        print(f'ID: {len(self._funcionario_repositorio.funcionarios) -1} \n{self._funcionario_repositorio.funcionarios[-1]}')
    
    def aumentar_salario(self):
        try:
            funcionario = self._funcionario_repositorio.funcionario_por_id(Utilidades.entrada_tratada_int("Digite o ID do funcionário: "))
            funcionario.aumentar_salario(Utilidades.entrada_tratada_float("Digite a porcentagem do aumento: "))
            print(funcionario)
        except:
            print("Parâmetro inválido")


app = Aplicacao()
app.aplicacao()

        
