import pytest
from contextlib import nullcontext as does_not_raise

from src.main import Calculator

# pytest tests/test_main.py::TestCalculator::test_divide -v
# pytest tests/test_main.py::TestCalculator -v

class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),  # типа не должно вызвать исключений, тогда тест пройдёт
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),  # типа должно вызвать TypeError
            (1, 0, '', pytest.raises(ZeroDivisionError)), # должно вызвать ZeroDivisionError
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (5, "-1", 4, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res