from io import StringIO
from topsort import main

def test_topsort(monkeypatch, capsys):
    user_input = StringIO('6 6\n1 2\n3 2\n4 2\n2 5\n6 5\n4 6')
    monkeypatch.setattr('sys.stdin', user_input)

    main()

    output = capsys.readouterr()
    assert output.out.strip() == '4 6 3 1 2 5'