from database import Database

def test_database_singleton():
    db1 = Database()
    db2 = Database.get_instance()
    assert db1 == db2