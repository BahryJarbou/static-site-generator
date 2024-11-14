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

    # def test_props_to_html2(self):
    #     child_node = ParentNode(tag="a", value = "My Link", props = {"href": "https://www.google.com", "target":"_blank"})
    #     child_node2 = ParentNode(tag="a", value = "My Link", props = {"href": "https://www.google.com", "target":"_blank"})
    #     node = ParentNode(tag="h1", value = "My Big Header", children = [child_node,child_node2], props = {"font": 14})
    #     node.props_to_html()
    #     child_node.props_to_html()
    #     print(node)
        
    # def test_props_to_html2(self):
    #     node = ParentNode(tag="h3", value = "My regular medium header", props= {})
    #     node_2 = ParentNode(tag= "div", value = "AAYYOO", props={"hieght":120,
    #                                                             "width": 150,
    #                                                             "align-items": "center"})
    #     node.props_to_html()
    #     node_2.props_to_html()
        
        

if __name__ == "__main__":
    unittest.main()