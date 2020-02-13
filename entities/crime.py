from entities.room import Room
from entities.weapon import Weapon
from entities.suspicious import Suspicious


class Crime:
    def __init__(self, suspicious: Suspicious, weapon: Weapon, room: Room):
        self._suspicious = suspicious
        self._weapon = weapon
        self._room = room

    def to_dict(self, verbose: bool = False) -> dict:
        return {
            'suspicious': self._suspicious if not verbose else self._suspicious.name,
            'weapon': self._weapon if not verbose else self._weapon.name,
            'room': self._room if not verbose else self._room.name,
        }

    @property
    def suspicious(self) -> Suspicious:
        return self._suspicious

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def room(self) -> Room:
        return self._room

    def list_clues(self) -> list:
        return list(self.to_dict().values())
