from interest_calculator import calculate_interest

def test_interest_calculation():
    assert calculate_interest(1000, 5) == 50
