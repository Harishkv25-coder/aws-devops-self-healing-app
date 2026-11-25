import unittest
from app.app import app


class TestApplication(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "Running")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_version_endpoint(self):
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["version"], "1.0.0")


if __name__ == "__main__":
    unittest.main()
