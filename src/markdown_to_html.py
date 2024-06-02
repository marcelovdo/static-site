
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_quote,
    block_type_heading,
    block_type_code,
    block_type_unordered_list,
    block_type_ordered_list
)
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(lambda node: text_node_to_html_node(node), text_nodes))

def paragraph_block_to_html(block):
    lines = block.split("\n")
    new_lines = list(map(lambda line: line.strip(), lines))
    children = text_to_children(" ".join(new_lines))
    return ParentNode("p", children)

def quote_block_to_html(block):
    lines = block.split("\n")
    new_lines = list(map(lambda line: line.strip().lstrip(">").strip(), lines))
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)

def heading_block_to_html(block):
    count = 0
    for char in block:
        if char != "#":
            break
        count += 1
    children = text_to_children(block[count+1:])
    return ParentNode(f"h{count}", children)

def code_block_to_html(block):
    children = text_to_children(block[4:-3])
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def unordered_list_block_to_html(block):
    children = []
    for line in block.split("\n"):
        list_item = ParentNode("li", text_to_children(line[2:]))
        children.append(list_item)
    return ParentNode("ul", children)

def ordered_list_block_to_html(block):
    children = []
    for line in block.split("\n"):
        line_trimmed = line.split(" ", 1)[1]
        list_item = ParentNode("li", text_to_children(line_trimmed))
        children.append(list_item)
    return ParentNode("ol", children)

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            children.append(paragraph_block_to_html(block))
        if block_type == block_type_quote:
            children.append(quote_block_to_html(block))
        if block_type == block_type_heading:
            children.append(heading_block_to_html(block))
        if block_type == block_type_code:
            children.append(code_block_to_html(block))
        if block_type == block_type_unordered_list:
            children.append(unordered_list_block_to_html(block))
        if block_type == block_type_ordered_list:
            children.append(ordered_list_block_to_html(block))
    return ParentNode("div", children)
