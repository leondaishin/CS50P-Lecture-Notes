# this code is to TEST calculator.py

from calculator import square

def main():
    test_square()

# assert means that it SHOULD be the number (obligating)
# assertionerror is the error of the assertion
# using try and except because of trial and error. 
# a testing function if the square function works out or not
def test_square(): 
    try: 
        assert square(2) == 4
    except AssertionError: 
        print("2 squared was not 4")
    try: 
        assert square(3) == 9
    except AssertionError: 
        print("3 squared was not 9")


if __name__ == "__main__": 
    main()
    