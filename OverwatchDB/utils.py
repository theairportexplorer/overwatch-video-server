from enum import Enum, auto
import datetime
from sys import version_info


def datetime_fromisoformat(date: str) -> datetime.date:
    # patch because .fromisoformat was only came with Python3.7+
    if version_info.minor <= 6:
        yyyy, mm, dd = date.split("-")
        return datetime.date(year=int(yyyy), month=int(mm), day=int(dd))
    return datetime.date.fromisoformat(date)


class OverwatchHeroes(Enum):
    Ana = auto()
    Ashe = auto()
    Baptise = auto()
    Bastion = auto()
    Brigitte = auto()
    DVa = auto()
    Doomfist = auto()
    Echo = auto()
    Genji = auto()
    Hanzo = auto()
    Junkrat = auto()
    Lucio = auto()
    McCree = auto()
    Mei = auto()
    Mercy = auto()
    Moira = auto()
    Orisa = auto()
    Pharah = auto()
    Reaper = auto()
    Reinhardt = auto()
    Roadhog = auto()
    Soldier76 = auto()
    Sombra = auto()
    Symmetra = auto()
    Torbjorn = auto()
    Widowmaker = auto()
    Winston = auto()
    WreckingBall = auto()
    Zarya = auto()
    Zenyatta = auto()

    def __str__(self):
        return f"{self.name.lower()}"

OWHeroesList = [name.lower() for name, _ in OverwatchHeroes.__members__.items()]
OWHeroesMap = {name.lower(): hero  for name, hero in OverwatchHeroes.__members__.items()}

TODAY = datetime.date.today()
OWRELEASEDATE = datetime_fromisoformat("2016-05-24")


def get_overwatch_hero(hero_name: str) -> OverwatchHeroes:
    if hero_name is None:
        return None
    if hero_name not in OWHeroesList:
        return None
    return OWHeroesMap[hero_name]
    