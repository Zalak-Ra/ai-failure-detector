from app import service

def test_add():
    assert service.add(5, 3)==8

def test_mul():
    assert service.mul(3, 2)==6

def test_div():
    assert service.div(4, 2)==2