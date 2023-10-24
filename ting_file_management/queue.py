from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, value):
        for i in self.__queue:
            if i == value:
                raise ValueError("Arquivo já adicionado")
        self.__queue.append(value)

    def dequeue(self):
        if not self.__queue:
            raise IndexError("A fila está vazia")
        return self.__queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.__queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__queue[index]
