import unittest
from flask_api import app


class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_receive_alarm(self):
        response = self.app.get("/alarm")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Alarm received successfully")


if __name__ == "__main__":
    unittest.main()
