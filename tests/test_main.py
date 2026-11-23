import runpy

from app.main import calculate_discount, calculate_total, main


def test_script_execution(capsys):
    runpy.run_path("app/main.py", run_name="__main__")

    captured = capsys.readouterr()

    assert captured.out.strip() == "270.0"


def test_calculate_total():
    assert calculate_total(100, 3) == 300


def test_calculate_discount():
    assert calculate_discount(300, 10) == 270


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "270.0"
