from kmy.kmy import Kmy


def test_read_name(mm_simple: Kmy) -> None:
    assert "Your name" == mm_simple.user.name


def test_read_email(mm_simple: Kmy) -> None:
    assert "Email" == mm_simple.user.email
