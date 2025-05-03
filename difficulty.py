from enum import Enum
class Difficulty(Enum):
    EASY = "easy"
    INTERMEDIATE = "intermediate"
    HARD = "difficult"
    @classmethod
    def get_next_level(cls, current_level):
        levels = [level.value for level in cls]
        try:
            index = levels.index(current_level)
            return Difficulty.LEVELS.index[index + 1]
        except(ValueError,IndexError):
            return None
