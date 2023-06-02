import pytest
from src import Elephant, Lion, Crocodile, Snake, Gorilla, Lizard


def test_vocalise():
    
    assert Elephant().vocalise() == "Trumpet!"
    assert Lion().vocalise() == "Roar!"
    assert Crocodile().vocalise() == "Hiss!"
    assert Snake().vocalise() == "Hiss!"
    with pytest.raises(Exception, match="No sound"):
        Lizard().vocalise()
    assert Gorilla().vocalise() == "Umm-umm!"


def test_shedding():
    
    assert Elephant().shed() == "It sheds hair"
    assert Lion().shed() == "It sheds hair"
    assert Crocodile().shed() == "It sheds scales"
    assert Snake().shed() == "It sheds scales"
    assert Gorilla().shed() == "It sheds hair"
    assert Lizard().shed() == "It sheds scales"

