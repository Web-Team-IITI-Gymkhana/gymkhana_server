from uuid import uuid4

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


class Test_Eatery:
    record = {
        "name": "Grand Kitchen",
        "day": 0,
        "breakfast": "Poha and Milk",
        "lunch": "Sabzi Kachori and Shahi Paneer",
        "snacks": "Tea Pakoda",
        "dinner": "Dal Makhani and Aloo Naan",
    }

    updated_record = {
        "name": "Grand Kitchen",
        "day": 0,
        "breakfast": "Poha and Kheer",
        "lunch": "Aloo Sabzi, Kachori and Shahi Paneer",
        "snacks": "Tea and Pakodas",
        "dinner": "Dal Makhani and Paneer Naan",
    }

    def test_create(self):
        response = client.post("/eatery/", json=self.record)
        assert response.status_code == 201, f"Received {response.status_code}"
        response_record = response.json()
        self.record["id"] = response_record["id"]
        print(self.record)
        for key in response_record.keys():
            assert self.record[key] == response_record[key]

    def test_get_one(self):
        response = client.get(f"/eatery/{self.record['id']}")
        assert response.status_code == 200, f"Received {response.status_code}"
        assert response.json() == self.record

    def test_get_non_existing(self):
        response = client.get(f"/eatery/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Eatery not found"}

    def test_patch(self):
        response = client.patch(
            f"/eatery/{self.record['id']}", json=self.updated_record
        )
        assert response.status_code == 202, f"Received {response.status_code}"
        assert response.json() == self.updated_record

    def test_get_all(self):
        response = client.get("/eatery/")
        assert response.status_code == 200, f"Received {response.status_code}"

    def test_delete(self):
        response = client.delete(f"/eatery/{self.record['id']}")
        assert response.status_code == 204, f"Received {response.status_code}"

    def test_delete_non_existing(self):
        response = client.get(f"/eatery/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Eatery not found"}
