import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_single_parent_with_leaves(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_with_parents(self):
        node = ParentNode("p", [
            ParentNode("p", [
                LeafNode("b", "Bold text")
            ]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ])
        self.assertEqual(node.to_html(), "<p><p><b>Bold text</b></p>Normal text<i>italic text</i>Normal text</p>")
    
    def test_parent_with_parents_and_props(self):
        node = ParentNode("p", [
            ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "normal")
            ], {
                "href": "http",
                "alt": "alttext"
            }),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ])
        self.assertEqual(node.to_html(), "<p><p href=\"http\" alt=\"alttext\"><b>Bold text</b>normal</p>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()
