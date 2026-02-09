from basic_operations import add
from advanced_operations import power
from scientific import sine, log10

def test_complex_expression():
    # 10 + sin(30) + log10(100) + 2^3
    result = add(
        add(add(10, sine(30)), log10(100)),
        power(2, 3)
    )
    assert round(result, 2) == 20.5
