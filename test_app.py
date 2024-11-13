from app import app

def test_get_habits():
    client = app.test_client()
    response = client.get('/habits')
    assert response.status_code == 200

def test_add_habit():
    client = app.test_client()
    response = client.post('/habits', json={'habit': 'Read a book'})
    assert response.status_code == 201
    assert b'Habit added successfully' in response.data
