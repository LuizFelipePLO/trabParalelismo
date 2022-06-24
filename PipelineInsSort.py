import multiprocessing
from random import randint

# função de envio de mensagens para o final do pipe


def sender(conn, array):
    for msg in insertion_sort(array):
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()

# função de impressão as mensagens recebidas do outro lado do pipe


def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))


def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


if __name__ == "__main__":

    array = [randint(0, 10) for i in range(5)]

    print("Initial array: ")
    print(*array, sep=", ")
    print()

    # criação do início e do fim do pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # criação de processos de envio e recebimento de informação
    p1 = multiprocessing.Process(target=sender, args=(
        parent_conn, insertion_sort(array)))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # executa processos
    p1.start()
    p2.start()

    # espera os processos acabarem
    p1.join()
    p2.join()
