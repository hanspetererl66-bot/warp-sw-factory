import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import HTTPServer

from quote_service.server import Handler


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = HTTPServer(("127.0.0.1", 0), Handler)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_port}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()

    def post(self, role, pct):
        headers = {"Content-Type": "application/json"}
        if role:
            headers["X-Role"] = role
        req = urllib.request.Request(f"{self.base}/quotes/Q-1001", method="POST",
                                     data=json.dumps({"discount_pct": pct}).encode(), headers=headers)
        try:
            return urllib.request.urlopen(req).status
        except urllib.error.HTTPError as e:
            return e.code

    def test_health(self):
        self.assertEqual(urllib.request.urlopen(f"{self.base}/health").status, 200)

    def test_discount_without_role_is_forbidden(self):
        self.assertEqual(self.post(None, 10), 403)

    def test_sales_can_apply_small_discount(self):
        self.assertEqual(self.post("sales", 5), 200)


if __name__ == "__main__":
    unittest.main()
