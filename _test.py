from pathlib import Path
import io
import pytest
from main import average_rating_report, draw_table, get_args
import sys


def test_single_file(monkeypatch, capsys):
    test_file_1 = str(Path(__file__).parent / "test" / "products1.csv")
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "--files", test_file_1, "--report", "average", "rating"],
    )
    get_args()
    captured = capsys.readouterr()
    assert "apple" in captured.out
    assert "4.8" in captured.out


def test_mult_files(monkeypatch, capsys):
    test_file_1 = str(Path(__file__).parent / "test" / "products1.csv")
    test_file_2 = str(Path(__file__).parent / "test" / "products2.csv")
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "--files", test_file_1, test_file_2, "--report", "average", "rating"],
    )
    get_args()
    captured = capsys.readouterr()
    assert "apple" in captured.out
    assert "4.55" in captured.out


def test_invalid_file(monkeypatch):
    test_file = str(Path(__file__).parent / "test" / "products.csv")
    monkeypatch.setattr(
        sys, "argv", ["prog", "--files", test_file, "--report", "average", "rating"]
    )
    with pytest.raises(SystemExit):
        get_args()


def test_invalid_report_type(monkeypatch):
    test_file = str(Path(__file__).parent / "test" / "products1.csv")
    monkeypatch.setattr(
        sys, "argv", ["prog", "--files", test_file, "--report", "average"]
    )
    with pytest.raises(SystemExit):
        get_args()
