import pytest

from lab2.solver.task2 import Container

_container = Container("Test")


@pytest.fixture
def container():
    return _container


def test_set_find_1(container):
    assert container.find("2") == False


def test_set_find_2(container):
    _container.add("2")
    assert container.find("2") == True


def test_set_list_1(container):
    assert container.list() == []


def test_set_list2(container):
    _container.add("Hello")
    _container.add("4")
    assert container.list() == ["Hello", "4"]


def test_set_grep1(container):
    assert _container.grep('[^0-9]') == []


def test_set_grep2(container):
    _container.add("0")
    _container.add("qwerty")
    assert _container.grep('[^0-9]') == ["qwerty"]
