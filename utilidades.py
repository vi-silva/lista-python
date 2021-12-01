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