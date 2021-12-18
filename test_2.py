from unittest import TestCase, main
from main import over,position,ball_koord

class TestMain(TestCase):
    def test_main(self):
        self.assertEqual(position(1,-1,602,574,656,600,197,225,216,160), (-1,-1))

    def test_main1(self):
        self.assertEqual(position(1,-1,600,572,611,555,199,227,201,145), (1,1))

    def test_main2(self):
        self.assertEqual(position(-1,1,218,190,191,135,693,721,764,708), (1,1))

    def test_main3(self):
        self.assertEqual(position(-1,1,248,220,221,165,275,303,351,295), (1,-1))

    def test_main4(self):
        self.assertEqual(position(1,-1,496,468,551,495,27,55,81,25), (-1,-1))

    def test_main5(self):
        self.assertEqual(position(1,1,222,194,251,195,637,665,719,663), (1,-1))

    def test_main6(self):
        self.assertEqual(position(1,-1,530,502,566,510,329,357,336,280), (1,1))

    def test_main7(self):
        self.assertEqual(ball_koord(1,-1,642,20,660,157,883), (-1,-1))

    def test_main8(self):
        self.assertEqual(ball_koord(-1,1,18,20,660,505,883), (1,1))

    def test_main9(self):
        self.assertEqual(ball_koord(-1,-1,18,20,660,521,883), (1, -1))

    def test_main10(self):
        self.assertEqual(ball_koord(-1,-1,504,20,660,19,883), (-1, 1))

    def test_main11(self):
        self.assertEqual(ball_koord(-1,1,138,20,660,865,883), (-1, -1))



if __name__ == '__main__':
    main()