import pytest
import json
import os.path
import importlib
#import jsonpickle
from fixture.application import Application
#from fixture.db import DbFixture
#from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web_address"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    return fixture


# @pytest.fixture(scope="session")
# def db(request):
#     db_config = load_config(request.config.getoption("--target"))["db"]
#     db_fixture = DbFixture(host=db_config["host"], dbname=db_config["dbname"],
#                            user=db_config["user"], password=db_config["password"])
#
#     def fin():
#         db_fixture.destroy()
#     request.addfinalizer(fin)
#     return db_fixture
#
#
# @pytest.fixture(scope="session")
# def orm(request):
#     db_config = load_config(request.config.getoption("--target"))["db"]
#     orm_fixture = ORMFixture(host=db_config["host"], dbname=db_config["dbname"],
#                              user=db_config["user"], password=db_config["password"])
#     return orm_fixture


@pytest.fixture(scope="session", autouse=True)
def stop():
    yield fixture
    fixture.session.ensure_logout()
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata = load_from_module(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])
#         elif fixture.startswith("json_"):
#             testdata = load_from_json(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


# def load_from_json(filename):
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % filename)) as f:
#         return jsonpickle.decode(f.read())
