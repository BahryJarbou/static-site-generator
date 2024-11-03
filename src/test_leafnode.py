import unittest
from unittest import TestCase
from htmlnode import LeafNode

class testLeafNode(TestCase):
    
    def test_to_html(self):
        leaf = LeafNode(tag="p",value="here we are", props={"font-size": 14})
        leaf.to_html()
        
    def test_to_html2(self):
        leaf = LeafNode("a", "google", {"href": "https://www.google.com"})
        leaf.to_html()
    
    



if __name__ == "__main__":
    unittest.main()