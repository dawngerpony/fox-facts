""" Tests for api.py. """

from fox_facts.main import FoxFacts


def test_hello_should_return_hello_world():
    """ Testing the get() method should return hello world. """
    fox_facts = FoxFacts()
    assert fox_facts.get() == {"hello": "world"}
