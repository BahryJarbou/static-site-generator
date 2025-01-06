import unittest

from helper_functions import *



class TestDelimiter(unittest.TestCase):
    
    
    def test_(self):
        node = TextNode("**This** is text with a `code block` word", TextType.NORMAL_TEXT)
        split_nodes_delimiter(split_nodes_delimiter([node], "`", TextType.CODE_TEXT),"**", TextType.BOLD_TEXT)
        
    def test__2(self):
        node1 = TextNode("This is a **bold** text", TextType.NORMAL_TEXT)
        node2 = TextNode("This is an *italic* text", TextType.NORMAL_TEXT)
        split_nodes_delimiter([node1, node2], "*", TextType.ITALIC_TEXT)
        
    def test__3(self):
        node = TextNode("This is a mix of *italic* and **bold** texts" ,TextType.NORMAL_TEXT)
        split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)
        
    def test_4(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extract_markdown_images(text)
    
    def test_5(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extract_markdown_links(text)
        
    def test_6(self):
        text = "![](https://www.github.com) and ![steam](https://www.steampowered.com)"
        extract_markdown_links(text)
if __name__ == "__main__":
    unittest.main()