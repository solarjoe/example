import unittest
from app.my_lambda_function import handler
import uuid

class SomeTestCases(unittest.TestCase):

    def setUp(self):

        # let's mock the context
        # uuuh, some dulicate code, the FakeAWSContext already in routes.py
        # TODO: maybe a context manager?
        class FakeAWSContext():
            
            aws_request_id = str(uuid.uuid4())

        self.mock_context = FakeAWSContext()
        self.response = handler(None, FakeAWSContext())

    def tearDown(self):
        pass

    def test_response_1(self):

        self.assertTrue("result" in self.response)

    def test_response_2(self):

        self.assertEqual(self.response["status"], "success")

    def test_response_3(self):

        self.assertEqual(self.response["result"], 42)

    def test_response_4(self):

        self.assertEqual(self.response["aws_request_id"], self.mock_context.aws_request_id)

    def test_response_5(self):

        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()