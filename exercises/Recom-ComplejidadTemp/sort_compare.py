import time
import random
import matplotlib.pyplot as plt

def generator(n):
    num_list = []

    for i in range(n):
        num = random.randint(1,1000)
        num_list.append(num)

    return num_list


def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(lista, inicio, fin):
    if inicio >= fin:
        return

    pivote = lista[inicio]
    i = inicio
    j = fin

    while i < j:
        while i < j and lista[j] >= pivote:
            j -= 1
        lista[i] = lista[j]

        while i < j and lista[i] <= pivote:
            i += 1
        lista[j] = lista[i]

    lista[i] = pivote
    quick_sort(lista, inicio, i - 1)
    quick_sort(lista, i + 1, fin)


def ordenador(lista, algoritmo):
    inicio = time.time()

    if algoritmo == 'bubble':
        bubble_sort(lista)
    elif algoritmo == 'merge':
        merge_sort(lista)
    elif algoritmo == 'quickSort':
        quick_sort(lista)
    
    fin = time.time()

    return fin - inicio

def graficador(N, tb, tm, tq):
    plt.plot(N, tb, label="Bubble")
    plt.plot(N, tm, label="Merge")
    plt.plot(N, tq, label="Quick")
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.legend()
    plt.show()


def imprimir_tabla(N, tb, tm, tq):
    print(f"{'N':>6} | {'Bubble':>10} | {'Merge':>10} | {'Quick':>10}")
    print("-" * 46)

    for i in range(len(N)):
        print(f"{N[i]:>6} | {tb[i]:>10.6f} | {tm[i]:>10.6f} | {tq[i]:>10.6f}")


def main():
    Ns = []
    tb = []
    tm = []
    tq = []

    for n in range(50, 1001, 50):
        lista = generator(n)

        copia = lista.copy()
        inicio = time.perf_counter()
        bubble_sort(copia)
        tb.append(time.perf_counter() - inicio)

        copia = lista.copy()
        inicio = time.perf_counter()
        merge_sort(copia)
        tm.append(time.perf_counter() - inicio)

        copia = lista.copy()
        inicio = time.perf_counter()
        quick_sort(copia, 0, len(copia) - 1)
        tq.append(time.perf_counter() - inicio)

        Ns.append(n)

    imprimir_tabla(Ns, tb, tm, tq)
    graficador(Ns, tb, tm, tq)

main()


