from Add_Subfunction import add
def main():
    test_add()
 
#assert function    
def test_add():
    assert add(5,5) == 10
    assert add(10,10) == 20

if __name__ == "__main__":   
    main()