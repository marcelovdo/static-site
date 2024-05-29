import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_str(self):
        node = HTMLNode("p", "value", [], {})
        self.assertEqual(node.__repr__(), "HTMLNode(tag=p, value=value, children=[], props={})")

    def test_props_to_html(self):
        node = HTMLNode("p", "value", [], {"href": "http", "alt": "alttext"})
        self.assertEqual(node.props_to_html(), " href=\"http\" alt=\"alttext\"")

if __name__ == "__main__":
    unittest.main()
