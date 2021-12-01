def separa_par_impar(lista):
    impar = list(filter(lambda i: float(i)%2 == 0, lista))
    par = list(filter(lambda i: float(i)%2 != 0, lista))
    print(par)
    print(impar)
    
def recebe_lista():
    lista = []
    for i in range(20):
        lista.append(input(f'\nEntre com o número {i}\n'))
    print(lista)
    separa_par_impar(lista)
recebe_lista()