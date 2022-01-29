from uuid import uuid4

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


class Test_Event:
    record = {
        "name": "Winter of CP",
        "description": "It is a coding event held in the month of Decemeber by Programming Club",
        "created_on": "2022-01-28T21:33:50.795775",
        "last_update": "2021-01-28T12:33:52.795775",
        "start_time": "2022-02-19T19:33:10.895775",
        "end_time": "2022-02-19T21:00:10.895775",
        "image": "https://www.google.com/search?q=P",
        "website": "",
        "notify": True,
        "is_online": False,
        "meet_link": "",
        "venue": "Carbon Building",
    }

    updated_record = {
        "name": "Winter of CP",
        "description": "It is a coding event held in the month of Decemeber by Programming Club",
        "created_on": "2022-01-28T21:33:50.795775",
        "last_update": "2021-01-28T12:33:52.795775",
        "start_time": "2022-02-19T19:33:10.895775",
        "end_time": "2022-02-19T21:00:10.895775",
        "image": "https://www.google.com/search?",
        "website": "",
        "notify": False,
        "is_online": True,
        "meet_link": "https://meet.google.com/abc-defg-hij",
        "venue": "",
    }

    def test_create(self):
        response = client.post("/event/", json=self.record)
        assert response.status_code == 201, f"Received {response.status_code}"
        response_record = response.json()
        self.record["id"] = response_record["id"]
        print(self.record)
        for key in response_record.keys():
            assert self.record[key] == response_record[key]

    def test_get_one(self):
        response = client.get(f"/event/{self.record['id']}")
        assert response.status_code == 200, f"Received {response.status_code}"
        assert response.json() == self.record

    def test_get_non_existing(self):
        response = client.get(f"/event/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Event not found"}

    def test_patch(self):
        response = client.patch(
            f"/event/{self.record['id']}", json=self.updated_record
        )
        assert response.status_code == 202, f"Received {response.status_code}"
        assert response.json() == self.updated_record

    def test_get_all(self):
        response = client.get("/event/")
        assert response.status_code == 200, f"Received {response.status_code}"

    def test_delete(self):
        response = client.delete(f"/event/{self.record['id']}")
        assert response.status_code == 204, f"Received {response.status_code}"

    def test_delete_non_existing(self):
        response = client.get(f"/event/{uuid4()}")
        assert response.status_code == 404, f"Received {response.status_code}"
        assert response.json() == {"detail": "Event not found"}

