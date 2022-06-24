import multiprocessing
from random import randint
import time

# função de envio de mensagens para o final do pipe


def sender(conn, array):
    for msg in primeIdentifier(array):
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()


# função de impressão as mensagens recebidas do outro lado do pipe


def receiver(conn):
    print()
    start_time = time.perf_counter_ns()
    while 1:
        msg = conn.recv()
        if msg == "END":
            break

        print("Received the message: {}".format(msg))
        end_time = time.perf_counter_ns()
        print("Process time: ", end_time - start_time, "nanoseconds")


def primeIdentifier(array):
    prime = []
    for i in array:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            prime.append(i)

    return prime


if __name__ == "__main__":

    array = [randint(0, 100000) for i in range(5)]

    print("Initial array: ")
    print(*array, sep=", ")
    print()

    # criação do início e do fim do pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # criação de processos de envio e recebimento de informação
    p1 = multiprocessing.Process(target=sender, args=(
        parent_conn, primeIdentifier(array)))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # executa processos e o cronômetro
    p1.start()
    p2.start()

    # espera os processos acabarem e termina o cronômetro
    p1.join()
    p2.join()
