import unittest
import auth

class TestDemo(unittest.TestCase):
    def setUp(self):
        print "Setting up stuff"
    def tearDown(self):
        print "Tests are done"

    def test_short(self):
        r = auth.legal_password("123")
        self.assertFalse(r)
    def test_long(self):
        r = auth.legal_password("123123123")
        self.assertFalse(r)
    def test_goodlength(self):
        r = auth.legal_password("123123")
        self.assertTrue(r)


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
