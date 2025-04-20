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

    def test_7(self):
        text = "!(https://www.github.com) and ![steam](https://www.steampowered.com)"
        extract_markdown_links(text)

    def test_8(self):
        text = "(https://www.github.com) and ![steam](https://www.steampowered.com)"
        extract_markdown_links(text)
    
    def test_9(self):
        node = TextNode("![github](https://www.github.com) and ![steam](https://www.steampowered.com)",TextType.NORMAL_TEXT)
        split_nodes_image([node])

    def test_10(self):
        node = TextNode("!(https://www.github.com) and ![steam](https://www.steampowered.com)",TextType.NORMAL_TEXT)
        split_nodes_image([node])

    def test_11(self):
        node = TextNode("[github](https://www.github.com) and [steam](https://www.steampowered.com)",TextType.NORMAL_TEXT)
        split_nodes_link([node])
    
    def test_12(self):
        node = TextNode("(https://www.github.com) and [steam](https://www.steampowered.com)",TextType.NORMAL_TEXT)
        split_nodes_link([node])
        
        
    def test_13(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_to_textnodes(text)

    def test_14(self):
        text = "**This** is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a (https://boot.dev)"
        text_to_textnodes(text)

    def test_15(self):
        text = "*This* is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_to_textnodes([text])
        
        
    def test_15(self):
        text = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.










                * This is the first list item in a list block
                * This is a list item
                * This is another list item"""
        markdown_to_blocks(text)
        
    
    def test_16(self):
        text = """
        
        
        
        
        
        
        
        """
        markdown_to_blocks(text)
        
    
    def test_17(self):
        text = """
        one liner
        fake second line
        """
        
    def test_18(self):
        text = """
        one liner

        wohooo
        """
        markdown_to_blocks(text)
        
        
    def test_19(self):
        heading = "### heading"
        block_to_block_type(heading)
    
    
    def test_20(self):
        code = "```print('hello world')```"
        block_to_block_type(code)
        
        
    def test_21(self):
        quote = ">this is\n>a multiline quote"
        block_to_block_type(quote)
    
    
    def test_22(self):
        unordered_list = "- this is\n- an unordered\n- list"
        block_to_block_type(unordered_list)
        
        
    def test_23(self):
        ordered_list = "1. this is\n-2. an ordered\n-3. list"
        block_to_block_type(ordered_list)
        
    def test_24(self):
        paragraph = "this is a normal paragraph\nwith two lines of text"
        block_to_block_type(paragraph)
        
        
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )


    def test_unordered_list(self):
        md = """
- First item
- Second item
- Third item
- Fourth item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><ul><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ul></div>",
    )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
4. Fourth item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><ol><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ol></div>",
    )
    
        
if __name__ == "__main__":
    unittest.main()