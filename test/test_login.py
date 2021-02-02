import pytest


@pytest.mark.skip(reason="logging in occurs in fixture")
def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
