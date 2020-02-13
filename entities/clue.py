class Clue:
    def __init__(self, clue_id: int, clue_type: str, name: str, prob: float = 0):
        self._name = name
        self._clue_type = clue_type
        self._clue_id = clue_id
        self._prob = prob
        self._owner = None

    def calculate_prob(self, **kargs) -> float:
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self._name

    @property
    def prob(self) -> float:
        return self._prob

    def set_prob(self, prob: float):
        self._prob = prob

    def to_dict(self) -> dict:
        return {
            'id': self._clue_id,
            'name': self._name,
            'type': self._clue_type,
            'prob': self._prob,
        }

    def __hash__(self):
        return f'{self._name}{self._clue_id}'.__hash__()

    def __eq__(self, other):
        if isinstance(other, Clue):
            return self.__hash__() == other.__hash__()
