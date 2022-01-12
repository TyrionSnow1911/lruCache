import requests
import unittest

BASE_URL = "http://localhost:8080"


class TestRoutes(unittest.TestCase):
    def test_get_endpoint(self):
        url = "{}//get".format(BASE_URL)
        success = None
        payload = {"key": 0}
        response = requests.get(url, params=payload)
        success = response.json()["success"]
        data = response.json()["data"]
        code = response.status_code
        self.assertTrue(data == None)
        self.assertTrue(code == 200, "Correct status code received.")
        self.assertTrue(success == True, "Success equals true.")

    def test_put_endpoint(self):
        url = "{}//put".format(BASE_URL)
        success = None
        payload = {"key": 0, "value": 1}
        response = requests.put(url, params=payload)
        success = response.json()["success"]
        code = response.status_code
        self.assertTrue(code == 200, "Correct status code received.")
        self.assertTrue(success == True, "Success equals true.")

    def test_delete_endpoint(self):
        url = "{}//delete".format(BASE_URL)
        success = None
        payload = {"key": 0}
        response = requests.delete(url, params=payload)
        success = response.json()["success"]
        code = response.status_code
        self.assertTrue(code == 200, "Correct status code received.")
        self.assertTrue(success == True, "Success equals true.")

    def test_reset_endpoint(self):
        url = "{}//reset".format(BASE_URL)
        success = None
        response = requests.post(url)
        success = response.json()["success"]
        code = response.status_code
        self.assertTrue(code == 200, "Correct status code received.")
        self.assertTrue(success == True, "Success equals true.")


if __name__ == "__main__":
    unittest.main()
