#pyreverse -o png ./demo_for_pyreverse/
class Student:
    def __init__(self,name:str):
        self._age=12
        self._name=name


class Classroom:
    def __init__(self,number_of_students:int):
        self._students=[Student(name=str(index)) for index in range(number_of_students)]

    @property
    def number_of_students_in_class(self)->int:
        return len(self._students)

class School:
    def __init__(self,number_of_classes:int):
        self._class_rooms=[Classroom(number_of_students=index*10) for index in range(number_of_classes)]

    @property
    def number_of_students(self)->int:
        return sum([class_room.number_of_students_in_class for class_room in self._class_rooms])
