import pytest
from website.calculations import calculate_bmi
def test_calculate_bmi():
    assert calculate_bmi(1, 1) == 10000.0
    assert 22.2 <= calculate_bmi(150, 50) <= 22.3