from io import StringIO
from path import main

def test_cycle(monkeypatch, capsys):
    user_input = StringIO("""10
    0 1 0 0 0 0 0 0 0 0
    1 0 0 1 1 0 1 0 0 0
    0 0 0 0 1 0 0 0 1 0
    0 1 0 0 0 0 1 0 0 0
    0 1 1 0 0 0 0 0 0 1
    0 0 0 0 0 0 1 0 0 1
    0 1 0 1 0 1 0 0 0 0
    0 0 0 0 0 0 0 0 1 0
    0 0 1 0 0 0 0 1 0 0
    0 0 0 0 1 1 0 0 0 0
    5 4
    """)
    monkeypatch.setattr('sys.stdin', user_input)

    main()

    output = capsys.readouterr()
    assert output.out.strip() == '2\n5 2 4'