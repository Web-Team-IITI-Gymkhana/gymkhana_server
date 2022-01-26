from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


class Test_Hostel:
    record = {
        "name": "Devi Ahilya",
        "description": "The hereditary noble Queen of the Maratha Empire, India",
    }
    updated_record = {
        "name": "Shivaji Maharaj",
        "description": "The legendary King of the Maratha Empire, India",
    }

    def test_get_all(self):
        response = client.get("/hostel/")
        assert response.status_code == 200

    def test_create(self):
        response = client.post("/hostel/", json=self.record)
        assert response.status_code == 200
        response_record = response.json()
        self.record["id"] = response_record["id"]
        assert response_record["name"] == "Devi Ahilya"
        assert (
            response_record["description"]
            == "The hereditary noble Queen of the Maratha Empire, India"
        )

    def test_get_one(self):
        response = client.get(f"/hostel/{self.record['id']}")
        assert response.status_code == 200
        assert response.json() == self.record

    def test_delete(self):
        response = client.delete(f"/hostel/{self.record['id']}")
        assert response.status_code == 204
