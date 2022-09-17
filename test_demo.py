import pytest as pytest



@pytest.mark.sanity
def test_one():
    a = 35
    b = 50
    assert a+b == 85


@pytest.mark.smoke
def test_two():
    a = 45
    b = 55
    assert a+b == 105

@pytest.mark.sanity
@pytest.mark.regression
def test_sample():
    aa = [1,5,6,8,9,10]
    b = []
    for i in aa:
        b.append(i)
    print(b)

@pytest.mark.Amol
@pytest.mark.skipif(40+60 == 100, reason= 'skip test')
def test_str():
    a = 'sangharsha'
    b = ''
    for i in a:
        b = i+b
    print(b)



@pytest.mark.xfail
@pytest.mark.regression
def test_failing():
    a = 'amol'
    b = 'akash'
    assert a != b


















