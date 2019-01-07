from sample import inc

def test_wrong_answer():
    assert not inc(3) == 4

def test_right_answer():
    assert inc(3) == 4
