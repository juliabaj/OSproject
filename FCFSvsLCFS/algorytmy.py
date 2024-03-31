
#funckja "fcfs" zawierająca algorytm FCFS
def fcfs(procesy):
    # sortowanie procesów na podstawie ich arrival_time przy użyciu funkcji lambda, od najmniejszego do największego
    procesy = sorted(procesy, key=lambda x: x[1])
    total_waiting_time = 0              # całkowity czas oczekiwania, aż procesor przejdzie przez każdy proces
    total_turnaround_time = 0           # całkowity turnaround_time, czyli suma czasów oczekiwania i wykonania dla każdego procesu
    completion_time = procesy[0][1]     # completion_time ustawione jako arrival time procesu z najmniejszą jego wartością
    first_completion_time = procesy[0][1] + procesy[0][2]   # czas zakończenia wykonywania pierwszego procesu

    for proces in procesy:
        proces_num, arrival_time, burst_time = proces

        if procesy.index(proces) == 0:   # dla pierwszego procesu ustawiamy completion time jako jego arrival + burst time
            completion_time = first_completion_time
        elif first_completion_time >= procesy[procesy.index(proces)][1]:   # dla reszty procesów sprawdzamy czy nie ma tak zwanej
            completion_time = first_completion_time + burst_time           # dziury w czasie przyjścia pomiędzy procesami
            first_completion_time = completion_time                        # tak, aby waiting time nie wychodziło ujemne
        elif first_completion_time < procesy[procesy.index(proces)][1]:
            completion_time = procesy[procesy.index(proces)][1] + procesy[procesy.index(proces)][2]
            first_completion_time = completion_time

        turnaround_time = completion_time - arrival_time  # turnaround_time - czas oczekiwania i wykonania dla danego procesu
        waiting_time = turnaround_time - burst_time       # waiting_time - czas oczekiwania jednego procesu do bycia gotowym do wykonania -> turnaround_time - burst_time
        total_waiting_time += waiting_time                # całkowity czas oczekiwania jest zwiększany z każdym kolejnym procesem i jego czasem oczekiwania
        total_turnaround_time += turnaround_time

        print(f"Proces ID {proces_num} | Arrival Time {arrival_time} | Burst Time {burst_time} | Waiting Time  {waiting_time} | Turnaround Time {turnaround_time} | Completion Time {completion_time}")
        print(f"Total waiting time {total_waiting_time}")

    average_waiting_time = total_waiting_time / len(procesy)        # średni czas oczekiwania na rozpoczęcie wykonywania procesu
    average_turnaround_time = total_turnaround_time / len(procesy)  # średni czas oczekiwania i wykonania procesu
    print(f"Average waiting time: {average_waiting_time} | Average turnaround time: {average_turnaround_time}"
          f" | Total waiting time: {total_waiting_time}")

    with open("wyniki_fcfs_lcfs.txt", "a") as file:
        file.write(f"FCFS, ilość procesów: {len(procesy)}\n")
        file.write(f"AVG. WAITING TIME: {average_waiting_time}\n")
        file.write(f"AVG. TURNAROUND TIME: {average_turnaround_time}\n")

    return average_waiting_time, average_turnaround_time

def lcfs(procesy):
    # sortowanie procesów na podstawie ich arrival_time przy użyciu funkcji lambda, od największego do najmniejszego
    procesy = sorted(procesy, key=lambda x: x[1], reverse=True)
    total_waiting_time = 0              # całkowity czas oczekiwania, aż procesor przejdzie przez każdy proces
    total_turnaround_time = 0           # całkowity turnaround_time, czyli suma czasów oczekiwania i wykonania dla każdego procesu
    completion_time = procesy[0][1]     # completion_time ustawione jako arrival time procesu z największą jego wartością
    first_completion_time = procesy[0][1] + procesy[0][2]  # czas zakończenia wykonywania pierwszego procesu

    for proces in procesy:
        proces_num, arrival_time, burst_time = proces

        if procesy.index(proces) == 0:  # dla pierwszego procesu ustawiamy completion time jako jego arrival + burst time
            completion_time = first_completion_time
        elif first_completion_time >= procesy[procesy.index(proces)][1]:  # dla reszty procesów sprawdzamy czy nie ma tak zwanej
            completion_time = first_completion_time + burst_time          # dziury w czasie przyjścia pomiędzy procesami
            first_completion_time = completion_time                       # tak, aby waiting time nie wychodziło ujemne
        elif first_completion_time < procesy[procesy.index(proces)][1]:
            completion_time = procesy[procesy.index(proces)][1] + procesy[procesy.index(proces)][2]
            first_completion_time = completion_time

        turnaround_time = completion_time - arrival_time    # turnaround_time - czas oczekiwania i wykonania dla danego procesu
        waiting_time = turnaround_time - burst_time         # waiting_time - czas oczekiwania jednego procesu do bycia gotowym do wykonania -> turnaround_time - burst_time
        total_waiting_time += waiting_time                  # całkowity czas oczekiwania jest zwiększany z każdym kolejnym procesem i jego czasem oczekiwania
        total_turnaround_time += turnaround_time

        print(f"Proces ID {proces_num} | Arrival Time {arrival_time} | Burst Time {burst_time} | Waiting Time  {waiting_time} | Turnaround Time {turnaround_time} | Completion Time {completion_time}")
        print(f"Total waiting time {total_waiting_time}")

    average_waiting_time = total_waiting_time / len(procesy)        # średni czas oczekiwania na rozpoczęcie wykonywania procesu
    average_turnaround_time = total_turnaround_time / len(procesy)  # średni czas oczekiwania i wykonania procesu
    print(f"Average waiting time: {average_waiting_time} | Average turnaround time: {average_turnaround_time}"
          f" | Total waiting time: {total_waiting_time}")

    with open("wyniki_fcfs_lcfs.txt", "a") as file:
        file.write(f"LCFS, ilość procesów: {len(procesy)}\n")
        file.write(f"AVG. WAITING TIME: {average_waiting_time}\n")
        file.write(f"AVG. TURNAROUND TIME: {average_turnaround_time}\n\n")

    return average_waiting_time, average_turnaround_time
