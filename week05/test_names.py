from names import make_full_name, extract_given_name, extract_family_name
import pytest

def test_make_full_name ():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Johnson") == "Johnson; John"
    assert make_full_name("","") == "; " 

def test_extract_family_name (): 
    assert extract_family_name("Sally", "Brown") == "Brown"
    assert extract_family_name("John", "Johnson") == "Johnson"
    assert extract_family_name("","") == ""

def test_extract_given_name (): 
    assert extract_given_name("Sally", "Brown") == "Sally"
    assert extract_given_name("John", "Johnson") == "John"
    assert extract_given_name("","") == ""

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])