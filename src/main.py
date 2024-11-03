from textnode import TextNode, TextType
print("hello world")

def main():
    dummy_node = TextNode("this is a dummy text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(dummy_node)
    

main()