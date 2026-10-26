import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_reference_batch_unchanged(self):
        x=np.ones((3,18));np.testing.assert_allclose(correct(x,np.zeros(3,int),np.ones((5,18))),x)
    def test_batch_removal(self):
        w=np.zeros((5,2));w[2]=[2,3];np.testing.assert_allclose(correct(np.array([[3.,4.]]),np.array([1]),w),[[1,1]])
    def test_design_shape(self):self.assertEqual(design(np.array([0,1]),np.array([0,3])).shape,(2,5))
