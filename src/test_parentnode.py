import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html(self):
        node = ParentNode(tag="p",
                          children=[
                              ParentNode(
                                  tag="i",
                                  children=[
                                  LeafNode("b",value="1. hi",props={"font":"italic"}),
                                  LeafNode("a", value="2. hello", props= {"size": 14})
                                  ]),
                              LeafNode("i", "3. hey you")
                              ],
                         props = {"color" : "red"}
                         )
        node.to_html()

    
    def test_equal(self):
        node = ParentNode(tag="p",
                          children=[
                              ParentNode(
                                  tag="i",
                                  children=[
                                  LeafNode("b",value="1. hi",props={"font":"italic"}),
                                  LeafNode("a", value="2. hello", props= {"size": 14})
                                  ]),
                              LeafNode("i", "3. hey you")
                              ],
                         props = {"color" : "red"}
                         )

        node2 = ParentNode(tag="p",
                          children=[
                              ParentNode(
                                  tag="i",
                                  children=[
                                  LeafNode("b",value="1. hi",props={"font":"italic"}),
                                  LeafNode("a", value="2. hello", props= {"size": 14})
                                  ]),
                              LeafNode("i", "3. hey you")
                              ],
                         props = {"color" : "red"}
                         )
        self.assertEqual(node,node2)
        

if __name__ == "__main__":
    unittest.main()