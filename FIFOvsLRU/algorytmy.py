from queue import Queue
import time

# funkcja fifo przyjmująca argumenty pojemnosc - maksymalna liczba stron w pamięci, argument strony - lista stron
def fifo(pojemnosc, strony):
    pamiec = []                           # lista jako pamięć przechowująca użyte strony
    kolejka = Queue(maxsize=len(strony))  # kolejka do śledzenia kolejności użycia strony z ustawioną wielkością na długość listy ze stronami
    page_faults = 0                       # ustawienie wartości page fault oraz page hit na 0 na początku działania algorytmu
    page_hit = 0

    print("FIFO")
    start = time.perf_counter()          # przypisanie stanu obecnego czasu do zmiennej start przed rozpoczęciem algorytmu
    for strona in strony:
        if strona not in pamiec:         # jeśli strona nie jest jeszcze w pamięci stron, zostaje dodana
            if len(pamiec) < pojemnosc:  # jeśli wielkość pamięci nie przekroczyła limitu stron, strona zostaje dodana
                pamiec.append(strona)
                kolejka.put(strona)      # dodaj stronę do kolejki
                page_faults += 1         # zwiększamy page fault o jeden, ponieważ strona została dodana do pamięci
            else:
                strona_do_zmiany = kolejka.get()                    # pobierz najwcześniej dodaną stronę z kolejki
                pamiec[pamiec.index(strona_do_zmiany)] = strona     # zamień najwcześniej dodaną stronę na nową
                kolejka.put(strona)
                print(f"Strona {strona_do_zmiany} zostala zastpiona na {strona}")
                page_faults += 1        # zwiększanie page fault o jeden, ponieważ nowa strona została dodana do pamięci
        else:
            print(f"Strona {strona} juz istnieje w pamieci")        # w innym przypadku strona istnieje w pamięci przez co
            page_hit += 1                                           # nic się nie zmienia i zwiększamy wartość page hit o 1
        print(f"Aktualny stan: {pamiec}")                           # wyświetlenie aktualnego stanu pamięci
    total_time = time.perf_counter() - start                        # total_time to róznica obcenego czasu po wykonaniu wszystkich operacji minus czas startowy

    print(f"TOTAL PAGE FAULTS: {page_faults}")                      # końcowa ilość page faults oraz page hit
    print(f"TOTAL PAGE HITS: {page_hit}")                            # suma tych dwóch wartości powinna być równa ilości stron
    print(f"TOTAL TIME: {total_time:.5f} ms\n")
    page_fault_ratio = page_faults / (page_hit + page_faults)
    page_hit_ratio = page_hit / (page_hit + page_fault_ratio)

    with open("wyniki_fifo_lru.txt", 'a') as file:
        file.write(f"FIFO, pamięć: {len(pamiec)}, liczba stron: {len(strony)}\n")
        file.write(f"TOTAL PAGE FAULTS: {page_faults}\n")
        file.write(f"TOTAL PAGE HITS: {page_hit}\n")
        file.write(f"TOTAL TIME: {total_time:.5f} ms\n")

    return page_fault_ratio, page_hit_ratio, total_time

def lru(pojemnosc, strony):
    pamiec = []                              # utworzenie listy pamięci przechowującej ostatnio użyte strony
    ostatnie_uzycie = {}                     # utworzenie słownika przechowującego czas ostatniego użycia dla każdej strony
    aktualny_czas = 0                        # utworzenie zmiennej "aktualny_czas" przechowującą ostatni czas użycia danej zmiennej
    page_faults = 0                          # ustawienie wartości page fault oraz page hit na 0 na początku działania algorytmu
    page_hit = 0

    print("LRU")
    start = time.perf_counter()             # przypisanie stanu obecnego czasu do zmiennej start przed rozpoczęciem algorytmu
    for strona in strony:
        if strona not in ostatnie_uzycie:                            # jeśli strona nie istnieje jeszcze w pamięci to aktualizujemy jej czas ostatniego użycia na aktualny czas
            ostatnie_uzycie[strona] = aktualny_czas
        if strona not in pamiec:
            if len(pamiec) < pojemnosc:                              # jeśli ilość pamięci nie jest przekroczona, strona zostaje dodana do pamięci użytych stron
                pamiec.append(strona)
                page_faults += 1
            else:
                usun_strone = min(pamiec, key=lambda x: ostatnie_uzycie[x])  # sortowanie czasów ostatniego użycia stron,
                indeks_usunietej_strony = pamiec.index(usun_strone)          # pobranie indeksu zastepowanej strony
                pamiec[indeks_usunietej_strony] = strona                     # zastąpienie najstarszej stron nową stroną
                print(f"Strona {usun_strone} zostala zastepiona na {strona}")
                ostatnie_uzycie[strona] = aktualny_czas                      # Aktualizacja słownika zawierającego czasy ostatniego użycia dla danej strony
                page_faults += 1
        else:
            ostatnie_uzycie[strona] = aktualny_czas                          # Jeśli strona była już w pamięci, aktualizujemy czas jej ostatniego użycia
            page_hit += 1
        aktualny_czas += 1                                                   # inkrementacja ostatniej ilości użycia strony po jej użyciu
        print(f"Aktualny stan: {pamiec}")
    total_time = time.perf_counter() - start                                 # total_time to róznica obcenego czasu po wykonaniu wszystkich operacji minus czas startowy

    print(f"TOTAL PAGE FAULTS: {page_faults}")                               # końcowa ilość page faults oraz page hit
    print(f"TOTAL PAGE HITS: {page_hit}")                                    # suma tych dwóch wartości powinna być równa ilości stron
    print(f"TOTAL TIME: {total_time:.5f} ms")
    page_fault_ratio = page_faults / (page_hit + page_faults)
    page_hit_ratio = page_hit / (page_hit + page_fault_ratio)

    with open("wyniki_fifo_lru.txt", 'a') as file:
        file.write(f"LRU, pamięć: {len(pamiec)}, liczba stron: {len(strony)}\n")
        file.write(f"TOTAL PAGE FAULTS: {page_faults}\n")
        file.write(f"TOTAL PAGE HITS: {page_hit}\n")
        file.write(f"TOTAL TIME: {total_time:.5f} ms\n\n")

    return page_fault_ratio, page_hit_ratio, total_time
