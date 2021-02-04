from random import randrange, choices
from string import ascii_letters


def random_user(prefix, maxlen):
    return prefix + "".join(choices(ascii_letters, k=randrange(maxlen)))


def test_signup_new_account(app):
    user = random_user("user_", 10)
    email = user + "@localhost"
    password = "test"
    app.james.ensure_user_exists(user, password)
    app.signup.new_user(user, email, password)
    app.session.login(user, password)
    assert app.session.is_logged_in_as(user)
    app.session.logout()