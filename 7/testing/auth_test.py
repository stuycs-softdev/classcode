import unittest
import auth

class TestDemo(unittest.TestCase):
    def setUp(self):
        print "Before a test"
    def tearDown(self):
        print "after a test"
    def test_short(self):
        r = auth.legal_password("123")
        self.assertEqual(r,False)
    def test_long(self):
        r = auth.legal_password("1234567890")
        self.assertFalse(r)
    def test_justright(self):
        r = auth.legal_password("123456")
        self.assertTrue(r)

if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
