import os
import shutil

from textnode import TextNode
from generate_page import generate_pages_recursive

def copy_dir(source, dest):
    if os.path.isfile(source):
        shutil.copy(source, dest)
        return
    if not os.path.exists(dest):
        os.mkdir(dest)
    elems = os.listdir(source)
    for elem in elems:
        copy_dir(os.path.join(source, elem), os.path.join(dest, elem))

def main():
    static_dir = "static"
    public_dir = "public"
    content_dir = "content"
    template_file = "template.html"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_dir(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_file, public_dir)

main()
