import unittest
import auth


class TestDemo(unittest.TestCase):
    def setUp(self):
        print "this is done before a test"
    def tearDown(self):
        print "This is done after a test"
    def test_short(self):
        r = auth.legal_password("11")
        self.assertEqual(r,False)
    def test_long(self):
        r = auth.legal_password("1234567789011")
        self.assertEqual(r,False)
    def test_goodlength(self):
        r = auth.legal_password("123456")
        self.assertEqual(r,True)
    def test_ucase_good(self):
        r = auth.legal_password("Hello");
        self.assertEqual(r,True)
    def test_ucase_bad(self):
        r = auth.legal_password("hello");
        self.assertEqual(r,False)

if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
