import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_subscribe(self):
        _editor = Editor()
        self.assertRaises(TypeError, _editor.subscribe, None)
        listener_a = ListenerA()
        _editor.subscribe(listener_a)
        self.assertRaises(TypeError, _editor.subscribe, listener_a)
        listener_b = ListenerB()
        self.assertRaises(TypeError, _editor.unsubscribe, listener_b)

    def test_editor_action(self):
        _editor = Editor()
        k_save = _editor.k
        _editor.plus()
        self.assertEqual(_editor.k, k_save + 1)
        _editor.minus()
        self.assertEqual(_editor.k, k_save)
        _editor.minus()
        self.assertEqual(_editor.k, k_save - 1)

    def test_notify(self):
        _editor = Editor()

        _listener_a = ListenerA()  # +
        _editor.subscribe(_listener_a)

        _listener_b = ListenerB()  # -
        _editor.subscribe(_listener_b)

        _editor.plus()
        self.assertEqual(_editor.k, _listener_a.plus)
        _editor.minus()
        self.assertEqual(_editor.k, _listener_b.minus)


if __name__ == '__main__':
    unittest.main()
