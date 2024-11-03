import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = TextNode("This is the first text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is the first text node", TextType.NORMAL_TEXT)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("this is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("this is a text node", TextType.NORMAL_TEXT)
        self.assertEqual(node, node2)
    
    def test_uneq2(self):
        node = TextNode("```This is a code node```", TextType.CODE_TEXT)
        node2 = TextNode("```This is a code node```", TextType.CODE_TEXT)
        self.assertEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("this is a text node", TextType.CODE_TEXT, url = "https//www.boot.dev")
        node2 = TextNode("this is a text node", TextType.CODE_TEXT, url = "https//www.boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()