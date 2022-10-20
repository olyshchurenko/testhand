import pytest
from uno_live.cardlist import Hand
from random import seed

RANDOM_SEED = 10

def test_hand_playable_list():
    top = Card('r', 1)

    f = Card('r', 9)
    s = Card('r', 2)
    t = Card('r', 3)
    h = Hand([f, s, t])
    assert(h.playable_list(top) == [f, s, t])

    f = Card('y', 1)
    s = Card('g', 1)
    t = Card('b', 1)
    h = Hand([f, s, t])
    assert (h.playable_list(top) == [f, s, t])

    f = Card('r', 2)
    s = Card('y', 1)
    t = Card('g', 9)
    h = Hand([f, s, t])
    assert (h.playable_list(top) == [f, s])
# я, к сожалению не поняла как импортировать ваш код UNO с гитхаба к себе в проект, поэтому присылаю так отдельным репозиторием, извините

