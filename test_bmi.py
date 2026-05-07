import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(57,1.73) == 0)

def test_bmi_over_weight():
    assert(bmi.calculate_bmi(100,1.73) == 1)

def test_bmi_under_weight():
    assert(bmi.calculate_bmi(30,1.73) == -1)
