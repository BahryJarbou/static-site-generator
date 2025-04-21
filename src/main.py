from textnode import TextNode, TextType
from htmlnode import LeafNode
from creation_functions import copy_content, generate_pages_recursive

def main():
    # dummy_node = TextNode("this is a dummy text node", TextType.LINK, "https://www.boot.dev")
    copy_content("./static/","./public/")
    generate_pages_recursive("./content/","template.html","./public/")
    # generate_page("./content/index.md","template.html","./public/")
    # generate_page("./content/blog/glorfindel/index.md","template.html","./public/")
    # generate_page("./content/blog/tom/index.md","template.html","./public/")
    # generate_page("./content/blog/majesty/index.md","template.html","./public/")
    # generate_page("./content/contact/index.md","template.html","./public/")
    # print(dummy_node.text_type)
    # print(text_node_to_html_node(dummy_node).to_html())


main()