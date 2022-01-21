"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.main_desc = []
        self.modification = []
        self.solved = []

    def is_empty_desc(self):
        return self.main_desc == []

    def is_empty_modify(self):
        return self.modification == []

    def is_empty_solved(self):
        return self.solved == []

    def to_queue(self, item):
        self.main_desc.insert(0, item)

    def to_modify(self):
        self.modification.insert(0, self.main_desc.pop())

    def from_modify(self):
        self.solved.insert(0, self.modification.pop())

    def to_solved(self):
        self.solved.insert(0, self.main_desc.pop())

    def size_desc(self):
        return len(self.main_desc)

    def size_modify(self):
        return len(self.modification)

    def size_solved(self):
        return len(self.solved)


if __name__ == "__main__":

    desc1 = QueueClass()

    desc1.to_queue('Lorem que re')
    desc1.to_queue('hiro mai ga to sao')
    desc1.to_queue('Sara ger na ma vio la')
    print(desc1.main_desc)

    desc1.to_modify()
    print(desc1.modification)

    desc1.to_solved()
    print(desc1.solved)

    print(desc1.main_desc)

