
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    return list(map(lambda block: block.strip("\n "), filter(lambda block: block != "", markdown.split("\n\n"))))

def block_to_block_type(block):
    for i in range(6):
        if len(block) > i+2 and ("#"*(i+1)) + " " == block[:i+2]:
            return block_type_heading
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    lines = block.split("\n")
    if all([line[0] == ">" for line in lines]):
        return block_type_quote
    if all([line[:2] == "* " or line[:2] == "- " for line in lines]):
        return block_type_unordered_list
    if all([lines[i][:2+len(str(i+1))] == f"{i+1}. " for i in range(len(lines))]):
        return block_type_ordered_list
    return block_type_paragraph