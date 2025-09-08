from app import app

def test_home():
    # Create a test client
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json == {"message": "Hello, KSW Capstone!"}
