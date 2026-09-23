from src.auth.login import login
from src.auth.register import register


def test_login():
  assert login("admin", "password")


def test_register():
  assert register("user", "password")