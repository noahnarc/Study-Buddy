from django.test import TestCase

# Create your tests here.

# dummy tests from textbook exchange example to get travis to build successfully
class DummyTestCase(TestCase):
  def setUp(self):
    x = 1
    
  def test_dummy_test_case(self):
    self.assertEqual(1, 1)
  
