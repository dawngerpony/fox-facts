from fox_facts.api import FoxFacts

def test_hello_should_return_hello_world():
    fox_facts = FoxFacts()
    assert fox_facts.get() == {'hello': 'banana'}
