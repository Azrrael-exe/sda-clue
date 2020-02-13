from typing import List

from entities.clue import Clue
from entities.crime import Crime

from entities.room import Room
from entities.weapon import Weapon
from entities.suspicious import Suspicious

from utils.clue_utils import classify_clues


class Agent:
    def __init__(self, name: str, clues: List[Clue], own_clues: List[Clue]):
        self._name = name

        for clue in own_clues:
            clues[clues.index(clue)].set_prob(prob=1)

        self._own_clues = own_clues
        self._weapons, self._rooms, self._suspicious = classify_clues(clues=clues)

    def update_prob(self, clue: Clue, value: float = 1.0):
        if isinstance(clue, Room):
            self._rooms[self._rooms.index(clue)].set_prob(prob=value)
        if isinstance(clue, Weapon):
            self._weapons[self._weapons.index(clue)].set_prob(prob=value)
        if isinstance(clue, Suspicious):
            self._suspicious[self._suspicious.index(clue)].set_prob(prob=value)

    def response(self, question: Crime):
        return {
            clue: 1 for clue in question.list_clues() if clue in self._own_clues
        }

    def guess(self) -> Crime:
        weapon = sorted(self._weapons, key=lambda x: x.prob, reverse=False)[0]
        room = sorted(self._rooms, key=lambda x: x.prob, reverse=False)[0]
        suspicious = sorted(self._suspicious, key=lambda x: x.prob, reverse=False)[0]
        return Crime(weapon=weapon,
                     room=room,
                     suspicious=suspicious)

    def process_response(self, response: dict):
        for clue, value in response.items():
            self.update_prob(clue=clue, value=value)

    def report(self) -> dict:
        return {
            clue.name: clue.prob for clue in (self._rooms + self._weapons + self._suspicious)
        }
