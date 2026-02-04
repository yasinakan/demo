from database import Database

def test_polluter():
    # This test pollutes global state
    db = Database()
    assert db is not None