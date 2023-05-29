import pytest
from src import Elephant, Lion, Crocodile, Snake


def test_vocalise():
    
    assert Elephant().vocalise() == "Trumpet!"
    assert Lion().vocalise() == "Roar!"
    assert Crocodile().vocalise() == "Hiss!"
    assert Snake().vocalise() == "Hiss!"


def test_shedding():

    assert Elephant().shed() == "It sheds hair"
    assert Lion().shed() == "It sheds hair"
    assert Crocodile().shed() == "It sheds scales"
    assert Snake().shed() == "It sheds skin"

