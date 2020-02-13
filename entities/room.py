from entities.clue import Clue


class Room(Clue):
    def __init__(self, name: str, clue_id: int):
        super().__init__(clue_id=clue_id, clue_type='Room', name=name)
        self._prob = 1.0 / 9.0

    def calculate_prob(self, **kargs) -> float:
        return 0.0
