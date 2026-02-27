from io import StringIO
from cycle import main

def test_cycle(monkeypatch, capsys):
    user_input = StringIO('3 \n0 1 1\n1 0 1\n1 1 0')
    monkeypatch.setattr('sys.stdin', user_input)

    main()

    output = capsys.readouterr()
    assert output.out.strip() == 'YES\n3\n2 3 1'