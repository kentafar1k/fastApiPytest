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
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (5, -1, 4),
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res