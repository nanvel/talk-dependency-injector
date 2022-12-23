from naive import main


def test_naive(capfd):
    shelf = {}

    main(["print"], shelf)
    out, err = capfd.readouterr()
    assert out == ""

    main(["create", "Test"], shelf)
    main(["print"], shelf)
    out, err = capfd.readouterr()
    assert "{'id': 0," in out

    main(["edit", "0", "Test2"], shelf)
    main(["print"], shelf)
    out, err = capfd.readouterr()
    assert "Test2" in out

    main(["set-priority", "0", "100"], shelf)
    main(["print"], shelf)
    out, err = capfd.readouterr()
    assert "100" in out

    main(["delete", "0"], shelf)
    main(["print"], shelf)
    out, err = capfd.readouterr()
    assert out == ""
