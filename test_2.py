from unittest import TestCase, main
from main import pole,position

class TestMain(TestCase):
    def test_main(self):
        global ball,paddle2, paddle
        self.assertEqual(position(1,-1,ball,paddle2), (1,1))

    def test_main2(self):
        self.assertEqual(position(-1,1,ball,paddle), (-1,-1))

    def test_main3(self):
        self.assertEqual(pole('RED'), print('поле_нарисовано'))


if __name__ == '__main__':
    main()