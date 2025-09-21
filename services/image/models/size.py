from typing import Tuple


class Size:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def to_tuple(self) -> Tuple[int, int]:
        return self.width, self.height

    def is_square(self) -> bool:
        return self.width == self.height