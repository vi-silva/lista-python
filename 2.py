from typing import List


class Entrada:
    def __init__(self, entrada):
        self.entrada = entrada
        self.consantes: List[str] = self._separa_consoantes(self.entrada)

    def _separa_consoantes(self, entrada) -> List[str]:
        entrada.lower()
        consoantes: List[str] = []
        for caractere in entrada:
            if(caractere) not in ('a','e','i','o','u',' '):
                consoantes.append(caractere)
        return consoantes


class Aplicacao:
    entrada = Entrada(input('Entre com a frase: '))
    print(entrada.consantes)
    print(len(entrada.consantes))