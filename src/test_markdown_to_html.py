import unittest

from markdown_to_html import (
    paragraph_block_to_html,
    quote_block_to_html,
    heading_block_to_html,
    code_block_to_html,
    unordered_list_block_to_html,
    ordered_list_block_to_html,
    markdown_to_html
)
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
       markdown = """Paragraph with some `code` and
       a **bold** word"""
       html = paragraph_block_to_html(markdown)
       self.assertEqual(html.to_html(), "<p>Paragraph with some <code>code</code> and a <b>bold</b> word</p>")

    def test_quote(self):
        markdown = """> Markdown test
        > **bolded** word
        > This is a *quote*"""
        html = quote_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<blockquote>Markdown test <b>bolded</b> word This is a <i>quote</i></blockquote>")

    def test_heading(self):
        markdown = """# Heading 1"""
        html = heading_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<h1>Heading 1</h1>")

        markdown = """### Heading 3"""
        html = heading_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<h3>Heading 3</h3>")

        markdown = """###### Heading 6"""
        html = heading_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<h6>Heading 6</h6>")
    
    def test_code(self):
        markdown = """```
int x = 10;
char y = 'a';
```"""
        html = code_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<pre><code>int x = 10;\nchar y = 'a';\n</code></pre>")

    def test_unordered_list(self):
        markdown = """* item
* item
* item"""
        html = unordered_list_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<ul><li>item</li><li>item</li><li>item</li></ul>")

    def test_ordered_list(self):
        markdown = """1. item 1
2. item 2
3. item 3"""
        html = ordered_list_block_to_html(markdown)
        self.assertEqual(html.to_html(), "<ol><li>item 1</li><li>item 2</li><li>item 3</li></ol>")

    def test_full_markdown(self):
        markdown = """Paragraph

* unordered 1
* unordered 2

```
coding
```

# Heading 1

1. ordered 1
2. ordered 2

> quote 1
"""
        html = markdown_to_html(markdown)
        self.assertEqual(html.to_html(), "<div><p>Paragraph</p><ul><li>unordered 1</li><li>unordered 2</li></ul><pre><code>coding\n</code></pre><h1>Heading 1</h1><ol><li>ordered 1</li><li>ordered 2</li></ol><blockquote>quote 1</blockquote></div>")

if __name__ == "__main__":
    unittest.main()