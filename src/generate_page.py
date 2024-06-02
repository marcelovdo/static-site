import os
import pathlib

from markdown_to_html import markdown_to_html

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.split(" ", 1)[1]
    raise Exception("Files need to have one h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path, "r")
    markdown = f.read()
    f.close()

    f = open(template_path, "r")
    template = f.read()
    f.close()

    html = markdown_to_html(markdown)

    title = extract_title(markdown)

    new_html = template.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html.to_html())

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    f = open(dest_path, "w")
    f.write(new_html)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        dest_path = pathlib.Path(dest_dir_path)
        generate_page(dir_path_content, template_path, str(dest_path.with_suffix(".html")))
        return
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    elems = os.listdir(dir_path_content)
    for elem in elems:
        generate_pages_recursive(os.path.join(dir_path_content, elem), template_path, os.path.join(dest_dir_path, elem))
    
