
import unittest

from textnode import *
from inline_markdown import *


class TestInlineMarkdown(unittest.TestCase):
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

    def test_extract_markdown_image(self):
        images = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
        self.assertEqual(images, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_markdown_link(self):
        links = extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
        self.assertEqual(links, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_image(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[1].text_type, text_type_image)
        self.assertEqual(new_nodes[1].text, "image")
        self.assertEqual(new_nodes[1].url, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[2].text, " and another ")
        self.assertEqual(new_nodes[3].text_type, text_type_image)
        self.assertEqual(new_nodes[3].text, "second image")
        self.assertEqual(new_nodes[3].url, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")

    def test_split_link(self):
        node = TextNode("This is text with an [link](https://www.example.com) and another [another](https://www.example.com/another)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[0].text, "This is text with an ")
        self.assertEqual(new_nodes[1].text_type, text_type_link)
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].url, "https://www.example.com")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[2].text, " and another ")
        self.assertEqual(new_nodes[3].text_type, text_type_link)
        self.assertEqual(new_nodes[3].text, "another")
        self.assertEqual(new_nodes[3].url, "https://www.example.com/another")

    def test_split_full_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        # TODO: use assertListEqual
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text_type, text_type_text)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text_type, text_type_bold)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[2].text_type, text_type_text)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[3].text_type, text_type_italic)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[4].text_type, text_type_text)
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[5].text_type, text_type_code)
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[6].text_type, text_type_text)
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[7].text_type, text_type_image)
        self.assertEqual(nodes[7].text, "image")
        self.assertEqual(nodes[7].url, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        self.assertEqual(nodes[8].text_type, text_type_text)
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[9].text_type, text_type_link)
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].url, "https://boot.dev")

if __name__ == "__main__":
    unittest.main()
