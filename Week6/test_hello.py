# from hello.py import hello the function 
# testing code if anything is wrong 
# if nothing is wrong after python test_hello.py it means the hello.py works perfectly
from hello import hello

def test_default(): 
    # this test doesnt work because it doesnt return a value 
    # hello("David") == "hello, David"
    
    assert hello() == "hello, world"


def test_argument(): 
    for name in ["Hermione", "Harry", "Ron", "leon", "ferdinand", "chikako", "ralf", "arne"]]
        assert hello("leon") == f"hello, {name}"
