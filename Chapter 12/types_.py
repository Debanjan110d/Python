from typing import List, Union, Tuple 

n : int = 5

name: str = "Harry"


def  sum(a: int, b: int) -> int:
    return a+b


# Lists
names: List[str] = ["Harry", "Ron", "Hermione"]

# Tuples
is_magician: Tuple[bool, int] = (True, 42)

# Unions
is_int: Union[int, float] = 5
