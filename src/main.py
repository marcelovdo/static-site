import os
import shutil

from textnode import TextNode

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
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_dir(static_dir, public_dir)

main()
