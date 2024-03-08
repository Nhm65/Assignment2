#Run test cases
import pytest
from mainFile import HeightFeet
from mainFile import HeightInches
from mainFile import Weight
from mainFile import OverallHeightInches
from mainFile import weightMeter
from mainFile import heightMeter
from mainFile import inches
from mainFile import convertHeight
from mainFile import convertWeight
from mainFile import calculateBmi
from mainFile import checkBmi

def test_inches():
    assert inches() == ((HeightFeet * 12) + HeightInches)

def test_convertHeight():
    assert convertHeight() == (OverallHeightInches * .025)

def test_convertWeight():
    assert convertWeight() == (Weight * .45)

def test_calculateBmi():
    assert calculateBmi() == (round(weightMeter/(heightMeter * heightMeter),1))
