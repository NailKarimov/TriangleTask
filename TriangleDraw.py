# test_example.py
import pytest

# Validity of Triangle given sides

def triangle_type(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        if a==b and b==c:
            return 'Triangle is Equilateral.'
        elif a==b or b==c or a==c:
            return 'Triangle is Isosceles.'
        else:
            return 'Triangle is Scalane'
    else:
        return 'Triangle is not possible from given sides.'

@pytest.mark.parametrize("test_input,expected", [
    ('"' + triangle_type(3,4,5) + '"' , 'Triangle is Scalane'),
    ('"' + triangle_type(3,5,5) + '"' , 'Triangle is Isosceles.'),
    ('"' + triangle_type(3,3,3) + '"' , 'Triangle is Equilateral.'),

    ('"' + triangle_type(3,4,0) + '"' , 'Triangle is not possible from given sides.'),
    ('"' + triangle_type('a','b','c') + '"' , 'Triangle is not possible from given sides.'),
    ('"' + triangle_type('%$%%','":?:""','@#$@#$') + '"' , 'Triangle is not possible from given sides.'),
    ('"' + triangle_type(-1,-5,3) + '"' , 'Triangle is not possible from given sides.'),
    ('"' + triangle_type(5464564,456445645,456456456) + '"' , 'Triangle is Scalane'),

    ('"' + triangle_type(0.5,0.5,0.5) + '"' , 'Triangle is Equilateral.'),
    ('"' + triangle_type(5464564,456445645,456456456) + '"' , 'Triangle is Scalane'),

])

def test_eval(test_input, expected):
    assert eval(test_input) == expected