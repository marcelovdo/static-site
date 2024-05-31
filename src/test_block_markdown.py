import unittest

from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    def test_split_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        blocks = markdown_to_blocks(text)
        self.assertListEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ])

    def test_get_type_heading(self):
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "#### Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "###### Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "####### Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_get_type_code(self):
        block = "```Some code\nother code```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_code)

        block = "```Some code\nother code"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_get_type_quote(self):
        block = ">Some quote\n>other quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_quote)

        block = ">Some quote\nother quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_get_type_unordered_list(self):
        block = "* Some item\n* other item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_unordered_list)

        block = "- Some item\n- other item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_unordered_list)

        block = "* Some item\nother item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_get_type_ordered_list(self):
        block = "1. Some item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ordered_list)

        block = "1. Some item\n2. other item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ordered_list)

        block = "1. a\n2. b\n3. c\n4. d\n5. e\n6. f\n7. g\n8. h\n9. i\n10. j"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ordered_list)

        block = "1. Some item\nother item\n3. last item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

if __name__ == "__main__":
    unittest.main()