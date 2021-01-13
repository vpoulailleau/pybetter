import pytest

from pybetter.cli import process_file
from pybetter.improvements import FixTrivialFmtStringCreation

NO_CHANGES_MADE = None

TRIVIAL_FSTRING = (
    """
    f"Hello, world!"
    """,
    """
    "Hello, world!"
    """,
)


TRIVIAL_FSTRING_IN_TRIPLE_QUOTES = (
    '''
    f"""Hello, world!"""
    ''',
    '''
    """Hello, world!"""
    ''',
)


FSTRING_WITH_ARGUMENTS = (
    """
    f"Hello, {username}"
    """,
    NO_CHANGES_MADE,
)

EMPTY_FSTRING = (
    """
    f""
    """,
    NO_CHANGES_MADE,
)


@pytest.mark.wip
@pytest.mark.parametrize(
    "original,expected",
    [
        TRIVIAL_FSTRING,
        TRIVIAL_FSTRING_IN_TRIPLE_QUOTES,
        FSTRING_WITH_ARGUMENTS,
        EMPTY_FSTRING,
    ],
    ids=[
        "trivial f-string",
        "trivial f-string in triple quotes",
        "f-string with arguments",
        "empty f-string",
    ],
)
def test_trivial_fmt_string_conversion(original, expected):
    processed, _ = process_file(original.strip(), [FixTrivialFmtStringCreation])

    assert processed.strip() == (expected or original).strip()
