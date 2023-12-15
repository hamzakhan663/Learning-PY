from pytest import raises
from SquareFunction import squared

def main():
    test_square()

def test_square():
    assert squared(8) == 64
    assert squared(-10) == 100
    assert squared(0) == 0
    
def test_not_int():
    with raises(TypeError):
        squared("dog")
    
if __name__ == "__main__":
    main()


