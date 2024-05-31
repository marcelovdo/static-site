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

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text_type, text_type_code)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_bold(self):
        node = TextNode("Text *bold* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[0].text, "Text ")
        self.assertEqual(new_nodes[1].text_type, text_type_bold)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_italic(self):
        node = TextNode("Text **italic** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_italic)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[0].text, "Text ")
        self.assertEqual(new_nodes[1].text_type, text_type_italic)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[2].text, " word")

    def test_split_exception(self):
        with self.assertRaises(Exception) as context:
            node = TextNode("Text `code word", text_type_text)
            split_nodes_delimiter([node], "`", text_type_code)
        
        self.assertTrue("Closing \'`\' delimiter not found")

if __name__ == "__main__":
    unittest.main()
