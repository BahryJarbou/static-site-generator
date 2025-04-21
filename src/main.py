from textnode import TextNode, TextType
from htmlnode import LeafNode
from creation_functions import copy_content, generate_pages_recursive
import sys
def main():
    basepath = sys.argv
    # print("base path:",basepath[0])
    copy_content("./static/","./public/")
    generate_pages_recursive("./content/","template.html","./public/",basepath)
    

main()