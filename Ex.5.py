"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class StackClass:
    def __init__(self):
        self.elems = []
        self.stacks = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) == 6:
            self.stacks.append(self.elems)
            self.elems = []
            self.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == "__main__":

    SM_OBJ = StackClass()

    print(SM_OBJ.is_empty())

    SM_OBJ.push_in(1)
    SM_OBJ.push_in(1)
    SM_OBJ.push_in(1)
    SM_OBJ.push_in(1)
    SM_OBJ.push_in(1)
    SM_OBJ.push_in(1)
    SM_OBJ.push_in(3)
    SM_OBJ.push_in(3)
    print(SM_OBJ.elems)
    SM_OBJ.push_in(3)
    SM_OBJ.push_in(3)
    SM_OBJ.push_in(3)
    SM_OBJ.push_in(3)
    SM_OBJ.push_in(3)

    print(SM_OBJ.stacks)
