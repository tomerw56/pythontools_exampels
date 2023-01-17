
#mypy mypy_demo.py  --disallow-untyped-defs


def greeting(name:str)->str:
    return 'Hello ' + name


def greeting_untyped(name):
    return 'Hello ' + name

# These calls will fail when the program run, but mypy does not report an error
# because "greeting" does not have type annotations.
greeting(123)
greeting(b"Alice")


from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push('x')        # Type error