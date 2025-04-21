from textnode import *
from htmlnode import *
import re
from enum import Enum
from itertools import pairwise

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def text_node_to_html_node(text_node):
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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        result = []
        if node.text_type == TextType.NORMAL_TEXT:
            texts = node.text.split(delimiter)
            for i, text in enumerate(texts):
                if i%2 != 0 and text !="":
                    result.append(TextNode(text,text_type))
                elif text !="":
                    result.append(TextNode(text,TextType.NORMAL_TEXT))
            new_nodes.extend(result)
        else:
            new_nodes.append(node)
    return new_nodes



def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return links



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
        else:
            result = []
            for i,image in enumerate(images):
                pretext = current_text.split(f"![{image[0]}]({image[1]})",1)[0]
                if pretext !="":
                    result.append(TextNode(pretext,TextType.NORMAL_TEXT))
                result.append(TextNode(image[0],TextType.IMAGE, image[1]))
                if i !=len(images)-1:
                    current_text = current_text.split(f"![{image[0]}]({image[1]})",1)[1]
                elif current_text.split(f"[{image[0]}]({image[1]})",1)[1] != "":
                    result.append(TextNode(current_text.split(f"[{image[0]}]({image[1]})",1)[1],TextType.NORMAL_TEXT))
            new_nodes.extend(result)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
        else:
            result = []
            for i, link in enumerate(links):    
                pretext = current_text.split(f"[{link[0]}]({link[1]})",1)[0]
                if pretext !="":
                    result.append(TextNode(pretext,TextType.NORMAL_TEXT))
                result.append(TextNode(link[0],TextType.LINK, link[1]))
                if i != len(links)-1:
                    current_text = current_text.split(f"[{link[0]}]({link[1]})",1)[1]
                elif current_text.split(f"[{link[0]}]({link[1]})",1)[1] != "":
                    result.append(TextNode(current_text.split(f"[{link[0]}]({link[1]})",1)[1],TextType.NORMAL_TEXT))
            new_nodes.extend(result)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL_TEXT)]
    delimiters = ["**", "_", "`"]
    text_types = {
        "**": TextType.BOLD_TEXT,
        "_": TextType.ITALIC_TEXT,
        "`": TextType.CODE_TEXT
    }
    for delimiter in delimiters:
       nodes = split_nodes_delimiter(nodes, delimiter=delimiter,text_type=text_types[delimiter])
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(str.strip, blocks))
    blocks = list(filter(lambda x: x!="",blocks))
    return blocks


def block_to_block_type(markdown):
    if re.match(r"#{1,6} ",markdown) != None:
        return BlockType.HEADING
    elif re.match(r"```((?s:.)*?)```",markdown):
        return BlockType.CODE
    elif re.match(r"(>(.*?))",markdown) and len(re.findall(r"(>(.*?))",markdown)) == len(markdown.split("\n")):
        return BlockType.QUOTE
    elif re.match(r"(- (.*?))",markdown) and len(re.findall(r"(- (.*?))",markdown)) == len(markdown.split("\n")):
        return BlockType.UNORDERED_LIST
    elif re.match(r"(1\. (.*?))",markdown) and len(re.findall(r"([0-9]+\. (.*?))",markdown)) == len(markdown.split("\n")) and all(int(x) == int(y) - 1 for x,y in pairwise(re.findall(r"[0-9]+",markdown))):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_nodes = text_to_children(block)
                nodes.append(ParentNode("p",block_nodes))
            case BlockType.HEADING:
                heading_size = len(re.match(r"#*",block).group(0))
                block_nodes = text_to_children(block.strip(r"#* "))
                nodes.append(ParentNode(f"h{heading_size}",block_nodes))
            case BlockType.QUOTE:
                cleaned_block = block.replace("> ", "").replace(">","")
                block_nodes = text_to_children(cleaned_block)
                nodes.append(ParentNode("blockquote",block_nodes))
            case BlockType.ORDERED_LIST:
                list_items = list(filter(lambda y: y !="",[x.strip("\n") for x in re.split(r"\d\. ",block)]))
                list_items_inlines = list(map(text_to_children,list_items))
                list_items_html = [ParentNode("li",x) for x in list_items_inlines]
                nodes.append(ParentNode("ol",list_items_html))
            case BlockType.UNORDERED_LIST:
                list_items = list(filter(lambda y: y !="",[x.strip("\n") for x in block.split("- ")]))
                list_items_inlines = list(map(text_to_children,list_items))
                list_items_html = [ParentNode("li",x) for x in list_items_inlines]
                nodes.append(ParentNode("ul",list_items_html))
            case BlockType.CODE:
                code_node = TextNode(block.strip("```").lstrip("\n"), TextType.CODE_TEXT)
                nodes.append(ParentNode("pre",[text_node_to_html_node(code_node)]))
    return ParentNode("div",nodes)