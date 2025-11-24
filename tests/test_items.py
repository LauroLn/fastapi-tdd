from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_item_sucesso():
    """Teste que deve retornar 200 ao buscar item existente."""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "nome": "Item 1"}


def test_get_item_inexistente():
    """Teste que deve retornar 404 ao buscar item inexistente."""
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não existe"}
