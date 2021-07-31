import pytest

from src.example import dummy, import_extra_package


def test_dummy():
    assert dummy()


def test_import_extra_package():
    assert import_extra_package() == pytest.approx(0)
