from typer import _click


def test_detect_program_name_reports_top_level_module() -> None:
    """When running a top-level module with ``python -m foo``, the module
    has an empty ``__package__`` but also has a ``__spec__``. The
    implementation should return ``python -m foo`` rather than ``foo.py``.
    """

    class MainModule:
        __package__ = ""
        __spec__ = object()

    program_name = _click.utils._detect_program_name(
        path="/tmp/foo.py",
        _main=MainModule(),
    )

    assert program_name == "python -m foo"


def test_detect_program_name_reports_script() -> None:
    """Running a script ``python foo.py`` means no package and no spec, so
    the bare filename is returned.
    """

    class MainModule:
        __package__ = None
        __spec__ = None

    program_name = _click.utils._detect_program_name(
        path="/tmp/foo.py",
        _main=MainModule(),
    )

    assert program_name == "foo.py"
