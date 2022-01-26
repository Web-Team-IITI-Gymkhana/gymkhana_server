from uuid import uuid4

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
        assert response.status_code == 200, f"Received {response.status_code}"

    def test_create(self):
        response = client.post("/hostel/", json=self.record)
        assert response.status_code == 201, f"Received {response.status_code}"
        response_record = response.json()
        self.record["id"] = response_record["id"]
        assert response_record["name"] == "Devi Ahilya"
        assert (
            response_record["description"]
            == "The hereditary noble Queen of the Maratha Empire, India"
        )

    def test_get_one(self):
        response = client.get(f"/hostel/{self.record['id']}")
        assert response.status_code == 200, f"Received {response.status_code}"
        assert response.json() == self.record

    def test_get_non_existing(self):
        response = client.get(f"/hostel/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Hostel not found"}

    def test_patch(self):
        response = client.patch(
            f"/hostel/{self.record['id']}", json=self.updated_record
        )
        assert response.status_code == 202, f"Received {response.status_code}"
        assert response.json() == self.updated_record

    def test_delete(self):
        response = client.delete(f"/hostel/{self.record['id']}")
        assert response.status_code == 204, f"Received {response.status_code}"

    def test_delete_non_existing(self):
        response = client.get(f"/hostel/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Hostel not found"}
