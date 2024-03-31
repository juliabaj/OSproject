import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
#funkcja generator stron
import random
import matplotlib.pyplot as plt
from algorytmy import fifo, lru

def main():
    lista_stron_generator = generator()                   # lista stron wygenerowana z danych zadanych przez użytkownika
    fifo(10, lista_stron_generator)
    lru(10, lista_stron_generator)

    # lista_stron = experiment(19, 100)      # wygenerowana lista do eskperymentu z większym zakresem
    # page_fault_ratio_fifo10, page_hit_ratio_fifo10, time_fifo10 = fifo(10, lista_stron)
    # page_fault_ratio_lru10, page_hit_ratio_lru10, time_lru10 = lru(10, lista_stron)
    #
    # page_fault_ratio_fifo5, page_hit_ratio_fifo5, time_fifo5 = fifo(5, lista_stron)
    # page_fault_ratio_lru5, page_hit_ratio_lru5, time_lru5 = lru(5, lista_stron)
    #
    # generate_combined_pie_chart(page_fault_ratio_fifo10, page_hit_ratio_fifo10, page_fault_ratio_lru10, page_hit_ratio_lru10, time_fifo10, time_lru10, 'Eksperyment dla pami�ci = 10')
    # generate_combined_pie_chart(page_fault_ratio_fifo5, page_hit_ratio_fifo5, page_fault_ratio_lru5, page_hit_ratio_lru5, time_fifo5, time_lru5, 'Eksperyment dla pami�ci = 5')

# funkcja generująca dane dla wartości zadanych przez użytkownika tj. zakres oraz ilość stron
def generator():
    zakres = int(input("Podaj zakres stron: "))
    ilosc = int(input("Podaj ilosc stron: "))
    strony = [random.randint(0, zakres) for _ in range(ilosc)]
    print(strony)
    return strony

# funkcja generująca dane konieczne do przeprowadzenia eksperymentu
def experiment(zakres, ilosc_stron):
    strony = [random.randint(0, zakres) for _ in range(ilosc_stron)]
    print(f"Wygenerowane strony:{strony}")
    return strony

# funkcja generująca wykresy z wynikami dla danych uzyskanych po przeprowadzeniu eksperymentu
def generate_combined_pie_chart(page_fault_ratio1, page_hit_ratio1, page_fault_ratio2, page_hit_ratio2, time_fifo, time_lru, title):
    labels = ['Page Faults', 'Page Hits']
    ratios1 = [page_fault_ratio1, page_hit_ratio1]
    ratios2 = [page_fault_ratio2, page_hit_ratio2]

    fig, axs = plt.subplots(1, 2, figsize=(16, 8))  # 1 wiersz, 2 kolumny

    axs[0].pie(ratios1, labels=labels, autopct='%1.1f%%', startangle=90, colors=['yellow', 'green'])
    axs[0].set_title('Algorytm FIFO')
    axs[0].text(0.5, -0.1, f'Time: {time_fifo:.5f} ms', size=12, ha="center", transform=axs[0].transAxes)

    axs[1].pie(ratios2, labels=labels, autopct='%1.1f%%', startangle=90, colors=['yellow', 'green'])
    axs[1].set_title('Algorytm LRU')
    axs[1].text(0.5, -0.1, f'Time: {time_lru:.5f} ms', size=12, ha="center", transform=axs[1].transAxes)

    plt.suptitle(title)
    plt.show()

if __name__ == "__main__":
    main()
