
# Polluting test that modifies global state
import os

def test_polluter():
    os.environ['POLLUTED'] = 'true'
    assert True
