import unittest
import widget


class WidgetClassTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = widget.Widget()

    def tearDown(self):
        self.widget.dispose()

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50, 50))

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150))
