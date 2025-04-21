from textnode import TextNode, TextType
from htmlnode import LeafNode
from creation_functions import copy_content, generate_pages_recursive
import sys
def main():
    try:
        basepath = sys.argv[1]
    except:
        basepath ="/"
    print(basepath)
    # print("base path:",basepath[0])
    copy_content("./static/","./docs/")
    generate_pages_recursive("./content/","template.html","./docs/",basepath)
    

main()