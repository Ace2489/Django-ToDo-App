from django.test import TestCase

class TestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('Setup Test Data: Run once to set up non-modified data for all class methods.')
        pass
        
    def setUp(self) -> None:
        print('Setup: Run once for every test method to clean data')
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)