import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_all(self):
        node = TextNode("This is a text node", "bold", "http://localhost")
        node2 = TextNode("This is a text node", "bold", "http://localhost")
        self.assertEqual(node, node2)
    
    def test_neq_text(self):
        node = TextNode("This is a text node", "bold", "http://localhost")
        node2 = TextNode("This is a text node2", "bold", "http://localhost")
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", "bold", "http://localhost")
        node2 = TextNode("This is a text node", "italic", "http://localhost")
        self.assertNotEqual(node, node2)
    
    def test_neq_url(self):
        node = TextNode("This is a text node", "bold", "http://localhost")
        node2 = TextNode("This is a text node", "bold", "http://localhost:3000")
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", "bold", "http://localhost")
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold, http://localhost)")


if __name__ == "__main__":
    unittest.main()
