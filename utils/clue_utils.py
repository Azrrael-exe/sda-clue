from typing import List

from entities.clue import Clue

from entities.room import Room
from entities.weapon import Weapon
from entities.suspicious import Suspicious


def classify_clues(clues: List[Clue]) -> [List, List, List]:
    weapons, suspicious, rooms = [], [], []

    for clue in clues:
        if isinstance(clue, Weapon):
            weapons.append(clue)
        elif isinstance(clue, Room):
            rooms.append(clue)
        elif isinstance(clue, Suspicious):
            suspicious.append(clue)
    return weapons, rooms, suspicious
