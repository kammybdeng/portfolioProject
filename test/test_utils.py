import pytest
from myPortfolio import formulas


def test_calTotalVal():
    assert formulas.calTotalVal(2, 123) == 246