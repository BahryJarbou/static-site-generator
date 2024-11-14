from textnode import TextNode, TextType
from htmlnode import LeafNode
print("hello world")

def main():
    dummy_node = TextNode("this is a dummy text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    # print(dummy_node.text_type)
    print(text_node_to_html_node(dummy_node).to_html())

    
def text_node_to_html_node(text_node):
    # if isinstance(text_node.text_type,TextType):
    #     raise Exception("Not a valid text type")
    match text_node.text_type:
        case "Normal text":
            return LeafNode(value = text_node.text)
        case "Bold text":
            return LeafNode("b", text_node.text)
        case "Italic text":
            return LeafNode("i", text_node.text)
        case "Code text":
            return LeafNode("code", text_node.text)
        case "Link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "Image":
            return LeafNode("img", "", {"src":text_node.url,
                                        "alt": text_node.text})
        case _:
             raise Exception("Not a valid text type")
main()