import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="hello", props = {"color" : "red"})
        node.props_to_html()


    def test_props_to_html2(self):
        child_node = HTMLNode(tag="a", value = "My Link", props = {"href": "https://www.google.com", "target":"_blank"})
        child_node2 = HTMLNode(tag="a", value = "My Link", props = {"href": "https://www.google.com", "target":"_blank"})
        node = HTMLNode(tag="h1", value = "My Big Header", children = [child_node,child_node2], props = {"font": 14})
        node.props_to_html()
        child_node.props_to_html()
        print(node)
        
    def test_props_to_html2(self):
        node = HTMLNode(tag="h3", value = "My regular medium header", props= {})
        node_2 = HTMLNode(tag= "div", value = "AAYYOO", props={"hieght":120,
                                                                "width": 150,
                                                                "align-items": "center"})
        node.props_to_html()
        node_2.props_to_html()
        
        

if __name__ == "__main__":
    unittest.main()