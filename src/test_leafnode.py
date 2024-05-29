import unittest

from leafnode import LeafNode

class TestLeafNone(unittest.TestCase):
    def test_raw_text(self):
        node = LeafNode(None, "This is text")
        self.assertEqual(node.to_html(), "This is text")

    def test_p(self):
        node = LeafNode("p", "Text")
        self.assertEqual(node.to_html(), "<p>Text</p>")

    def test_p_att(self):
        node = LeafNode("p", "Text", {"href": "http", "alt": "alttext"})
        self.assertEqual(node.to_html(), "<p href=\"http\" alt=\"alttext\">Text</p>")


if __name__ == "__main__":
    unittest.main()
