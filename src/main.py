from textnode import TextNode, TextType
from htmlnode import LeafNode
from content_copier import copy_content

def main():
    dummy_node = TextNode("this is a dummy text node", TextType.LINK, "https://www.boot.dev")
    copy_content("./static","./public")
    # print(dummy_node.text_type)
    # print(text_node_to_html_node(dummy_node).to_html())

    
def text_node_to_html_node(text_node):
    # if isinstance(text_node.text_type,TextType):
    #     raise Exception("Not a valid text type")
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, value = text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url,
                                        "alt": text_node.text})
        case _:
             raise Exception("Not a valid text type")


main()