
def markdown_to_blocks(markdown):
    return list(filter(lambda block: block != "", markdown.split("\n\n")))