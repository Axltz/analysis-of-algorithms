import time
import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


def generator(n):
    num_list = []
    for i in range(n):
        num = random.randint(1, 1000)
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


Ns = []
tb = []
tm = []
tq = []


def calcular():
    global Ns, tb, tm, tq

    Ns = []
    tb = []
    tm = []
    tq = []

    # Limpiar tabla
    for fila in tabla.get_children():
        tabla.delete(fila)

    nmin = int(entrada_nmin.get())
    nmax = int(entrada_nmax.get())
    inc = int(entrada_inc.get())

    for n in range(nmin, nmax + 1, inc):
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

        tabla.insert(
            "",
            "end",
            values=(
                n,
                f"{tb[-1]:.6f}",
                f"{tm[-1]:.6f}",
                f"{tq[-1]:.6f}"
            )
        )


def graficar():
    graficador(Ns, tb, tm, tq)


ventana = tk.Tk()
ventana.title("Comparación de Algoritmos de Ordenamiento")
ventana.geometry("600x400")

tk.Label(ventana, text="N_Max", font=("Arial", 12)).place(x=400, y=15)
tk.Label(ventana, text="N_Min", font=("Arial", 12)).place(x=400, y=60)
tk.Label(ventana, text="Incremento", font=("Arial", 12)).place(x=400, y=100)

entrada_nmax = tk.Entry(ventana, width=50)
entrada_nmax.place(x=50, y=20)

entrada_nmin = tk.Entry(ventana, width=50)
entrada_nmin.place(x=50, y=60)

entrada_inc = tk.Entry(ventana, width=50)
entrada_inc.place(x=50, y=100)

tk.Button(ventana, text="Calcular", command=calcular, width=10, height=2).place(x=50, y=150)
tk.Button(ventana, text="Graficar", command=graficar, width=10, height=2).place(x=200, y=150)

tabla = ttk.Treeview(
    ventana,
    columns=("N", "Bubble", "Merge", "Quick"),
    show="headings",
    height=8
)

tabla.heading("N", text="N")
tabla.heading("Bubble", text="Bubble")
tabla.heading("Merge", text="Merge")
tabla.heading("Quick", text="Quick")

tabla.column("N", width=80, anchor="center")
tabla.column("Bubble", width=120, anchor="center")
tabla.column("Merge", width=120, anchor="center")
tabla.column("Quick", width=120, anchor="center")

tabla.place(x=50, y=220)


ventana.mainloop()
