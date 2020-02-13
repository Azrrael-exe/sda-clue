from entities.clue import Clue


class Suspicious(Clue):
    def __init__(self, name: str, clue_id: int):
        super().__init__(clue_id=clue_id, clue_type='Suspicious', name=name)
        self._prob = 1.0 / 6.0

    def calculate_prob(self, **kargs) -> float:
        return 0.0