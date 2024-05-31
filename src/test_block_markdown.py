import unittest

from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    def test_split_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(text)
        self.assertListEqual(blocks, [
            "\nThis is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ])

if __name__ == "__main__":
    unittest.main()