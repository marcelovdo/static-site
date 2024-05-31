import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        splitted_text = node.text.split(delimiter)
        if len(splitted_text) % 2 == 0:
            raise Exception(f"Closing \'{delimiter}\'' delimiter not found")
        splitted_nodes = []
        for i in range(len(splitted_text)):
            if splitted_text[i] == "":
                continue
            node_type = text_type if i % 2 != 0 else text_type_text
            splitted_nodes.append(TextNode(splitted_text[i], node_type))
        new_nodes.extend(splitted_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if images == []:
            new_nodes.append(old_node)
            continue
        splitted_nodes = []
        text = old_node.text
        for image in images:
            splitted_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if splitted_text[0] != "":
                splitted_nodes.append(TextNode(splitted_text[0], text_type_text))
            splitted_nodes.append(TextNode(image[0], text_type_image, image[1]))
            text = splitted_text[1]
        if text != "":
            splitted_nodes.append(TextNode(text, text_type_text))
        new_nodes.extend(splitted_nodes)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if links == []:
            new_nodes.append(old_node)
            continue
        splitted_nodes = []
        text = old_node.text
        for link in links:
            splitted_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if splitted_text[0] != "":
                splitted_nodes.append(TextNode(splitted_text[0], text_type_text))
            splitted_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = splitted_text[1]
        if text != "":
            splitted_nodes.append(TextNode(text, text_type_text))
        new_nodes.extend(splitted_nodes)

    return new_nodes

def text_to_textnodes(text):
    new_nodes = split_nodes_delimiter([TextNode(text, text_type_text)], "`", text_type_code)
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes