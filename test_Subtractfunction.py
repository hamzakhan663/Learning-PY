from Add_Subfunction import subtract

def main(): 
    test_subtract()
    
def test_subtract():
    assert subtract(100, 50) == 50
    assert subtract(-5, 5) == -10
    assert subtract(50, -20) == 70
    assert subtract(50, 100) == -50
    assert subtract(-10, -10) == 0
    
if __name__ == '__main__':
    main()