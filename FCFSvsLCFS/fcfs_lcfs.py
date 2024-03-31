import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import random
import matplotlib.pyplot as plt
import numpy as np
from algorytmy import fcfs, lcfs

def main():
    proces_num = int(input("Podaj liczbe procesow: "))    # wersja programu w której użytkownik podaje ilość danych do wygenerowania
    procesy = generator(proces_num)
    print("FCFS")
    fcfs(procesy)
    print("LCFS")
    lcfs(procesy)

    # processes_number = [25, 50, 75, 100, 125]
    # results_fcfs_b, results_lcfs_b = experiment_burst(processes_number)
    # results_fcfs_a, results_lcfs_a = experiment_arrival(processes_number)
    # plot_results(processes_number, results_fcfs_b, results_lcfs_b)
    # plot_results(processes_number, results_fcfs_a, results_lcfs_a)


# generator z losową wartością burst i arrival time
def generator(process_number):
    procesy = []                                        # zainicjonowanie listy jako pamięci przechowującej wygenerowane procesy
    for i in range(1, process_number + 1):
        burst = random.randint(1, 10)             # burst - ile czasu system operacyjny potrzebuje do wykonania konkretnego procesu
        arrival = random.randint(0, 10)           # arrival - czas w którym dany proces jest gotowy do wykonania i wchodzi do "kolejki"
        procesy.append((i, arrival, burst))             # dodanie do listy procesu z jego danymi [index, arrival, burst]

    return procesy

# generator do wykonania eksperymentu ze stałą wartością burst_time
def generator_burst(process_number, burst_time):
    procesy = []
    for i in range(1, process_number + 1):
        arrival = random.randint(0, 10)
        burst = burst_time
        procesy.append((i, arrival, burst))

    return procesy

# generator do wykonania eksperymentu ze stałą wartością arrival_time
def generator_arrival(process_number, arrival_time):
    procesy = []
    for i in range(1, process_number + 1):
        arrival = arrival_time
        burst = random.randint(1, 10)
        procesy.append((i, arrival, burst))

    return procesy

# funkcja przeprowadzająca eksperyment ze stałą wartością burst time
def experiment_burst(processes_number):
    results_fcfs = []
    results_lcfs = []

    for _ in processes_number:
        results_fcfs.append([0, 0])    # wypelnienie listy, listami z dwoma wartosciami ustawionymi na 0
        results_lcfs.append([0, 0])    # nastepnie zmieniamy wartosci na wyniki average_waiting_time
                                       # oraz average_turnaround_time i zwracamy do utworzenia wykresu

    for i, number_of_processes in enumerate(processes_number):
        print(f"\nEksperyment dla {number_of_processes} procesow, staly BURST TIME:")
        # generowanie okreslonej liczby procesow
        procesy = generator_burst(number_of_processes, 7)
        print("ALGORYTM FCFS:")
        avg_wt_fcfs, avg_tt_fcfs = fcfs(procesy)
        print("ALGORYTM LCFS:")
        avg_wt_lcfs, avg_tt_lcfs = lcfs(procesy)
        # dla indexu danego eksperymentu o danej ilości procesów nadaje wartości uzyskane po przeprowadzeniu eksperymentów
        results_fcfs[i] = [avg_wt_fcfs, avg_tt_fcfs]
        results_lcfs[i] = [avg_wt_lcfs, avg_tt_lcfs]

    return results_fcfs, results_lcfs

# funkcja przeprowadzająca eksperyment ze stałą wartością arrival time
def experiment_arrival(processes_number):
    results_fcfs = []
    results_lcfs = []

    for _ in processes_number:
        results_fcfs.append([0, 0])
        results_lcfs.append([0, 0])

    for i, number_of_processes in enumerate(processes_number):
        print(f"\nEksperyment dla {number_of_processes} procesow, staly ARRIVAL TIME:")
        # generowanie okreslonej liczby procesow
        procesy = generator_arrival(number_of_processes, 2)
        print("ALGORYTM FCFS:")
        avg_wt_fcfs, avg_tt_fcfs = fcfs(procesy)
        print("ALGORYTM LCFS:")
        avg_wt_lcfs, avg_tt_lcfs = lcfs(procesy)
        # dla indexu danego eksperymentu o danej ilosci procesow nadaje wartosci uzyskane po przeprowadzeniu eksperymentow
        results_fcfs[i] = [avg_wt_fcfs, avg_tt_fcfs]
        results_lcfs[i] = [avg_wt_lcfs, avg_tt_lcfs]

    return results_fcfs, results_lcfs

# funkcja odpowiadajaca za sporzadzenie wykresow z wynikow uzyskanych po przeprowadzeniu eksperymentow
def plot_results(process_counts, results_fcfs, results_lcfs):
    bar_width = 0.35  # Szerokosc slupkow
    index = np.arange(len(process_counts))  # Indeksy na osi x

    plt.figure(figsize=(12, 12))

    # Wykresy slupkowe dla average waiting time
    plt.subplot(2, 2, 1)
    plt.bar(index - bar_width/2, [result[0] for result in results_fcfs], width=bar_width, label='FCFS')
    plt.bar(index + bar_width/2, [result[0] for result in results_lcfs], width=bar_width, label='LCFS')
    plt.title("Average Waiting Time Comparison")
    plt.xlabel("Number of Processes")
    plt.ylabel("Average Waiting Time")
    plt.xticks(index, process_counts)  # Ustawienie etykiet na osi x
    plt.legend()

    # Wykresy slupkowe dla average turnaround time
    plt.subplot(2, 2, 2)
    plt.bar(index - bar_width/2, [result[1] for result in results_fcfs], width=bar_width, label='FCFS')
    plt.bar(index + bar_width/2, [result[1] for result in results_lcfs], width=bar_width, label='LCFS')
    plt.title("Average Turnaround Time Comparison")
    plt.xlabel("Number of Processes")
    plt.ylabel("Average Turnaround Time")
    plt.xticks(index, process_counts)  # Ustawienie etykiet na osi x
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
