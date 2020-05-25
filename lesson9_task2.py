class Stack:
    def __init__(self):
        self.elements = []

    # проверяет стек на пустоту
    def isEmpty(self):
        return self.elements == []

    # добавляет новый элемент на вершину стека
    def push(self, element):
        self.elements.append(element)

    # удаляет верхний элемент из стека
    def pop(self):
        return self.elements.pop()

    # возвращает верхний элемент стека, но не удаляет его
    def peek(self):
        return self.elements[len(self.elements) -1]

    # возвращает количество элементов в стеке
    def size(self):
        return len(self.elements)



