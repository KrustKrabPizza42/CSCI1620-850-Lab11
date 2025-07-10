import unittest
import area

class AreaTestCases(unittest.TestCase):

    d_v = .01

    def test_string(self):

        with self.assertRaises(ValueError):

            area.circle('one')

            area.square('one')

            area.rectangle('one', 'one')
            area.rectangle('one', 1)
            area.rectangle(1, 'one')

            area.triangle('one', 'one')
            area.triangle('one', 1)
            area.triangle(1, 'one')

    def test_negative(self):
        
        with self.assertRaises(TypeError):

            area.circle(-1)

            area.square(-1)

            area.rectangle(-1, -1)
            area.rectangle(1, -1)
            area.rectangle(-1, 1)

            area.triangle(-1, -1)
            area.triangle(1, -1)
            area.triangle(-1, 1)

    def test_zero(self):
        
        with self.assertRaises(TypeError):

            area.circle(0)

            area.square(0)

            area.rectangle(0, 0)
            area.rectangle(1, 0)
            area.rectangle(0, 1)

            area.triangle(0, 0)
            area.triangle(1, 0)
            area.triangle(0, 1)

    def test_positive(self):
        
        self.assertAlmostEqual(area.circle(1), 3.14, delta=self.d_v)
        self.assertAlmostEqual(area.circle(1.1), 3.80, delta=self.d_v)

        self.assertAlmostEqual(area.square(1), 1, delta=self.d_v)
        self.assertAlmostEqual(area.square(1.1), 1.21, delta=self.d_v)

        self.assertAlmostEqual(area.rectangle(.1, .2), .02, delta=self.d_v)
        self.assertAlmostEqual(area.rectangle(1.1, 2), 2.2, delta=self.d_v)
        self.assertAlmostEqual(area.rectangle(2, 1.1), 2.2, delta=self.d_v)
        self.assertAlmostEqual(area.rectangle(2, 2), 4, delta=self.d_v)
        
        self.assertAlmostEqual(area.triangle(.1, .2), .01, delta=self.d_v)
        self.assertAlmostEqual(area.triangle(1.1, 2), 1.1, delta=self.d_v)
        self.assertAlmostEqual(area.triangle(2, 1.1), 1.1, delta=self.d_v)
        self.assertAlmostEqual(area.triangle(2, 2), 2, delta=self.d_v)



if __name__ == '__main__':
    unittest.main()