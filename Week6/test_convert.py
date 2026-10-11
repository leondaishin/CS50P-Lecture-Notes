import pytest 

from convert import convert


def test_conversion(): 
    # writing out the conversion that this is the answer for the inputs
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000



def test_error(): 
    # if "1" is writtewn, raise a typeerror becasue it is "1" not 1 : 
    with pytest.raises(TypeError): 
        convert("1")