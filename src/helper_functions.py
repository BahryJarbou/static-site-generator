from textnode import *
import re
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

def text_to_textnodes(nodes):
    delimiters = ["**", "*", "`"]
    text_types = {
        "**": TextType.BOLD_TEXT,
        "*": TextType.ITALIC_TEXT,
        "`": TextType.CODE_TEXT
    }
    for delimiter in delimiters:
       nodes = split_nodes_delimiter(nodes, delimiter=delimiter,text_type=text_types[delimiter])
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes





node = TextNode(
    "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
    TextType.NORMAL_TEXT,
)
new_nodes = text_to_textnodes([node])

for node in new_nodes:
    print(node)