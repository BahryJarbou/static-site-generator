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
    alt_texts = re.findall(r"\[(.*?)\]",text)
    urls = re.findall(r"\((.*?)\)",text)
    results = list(zip(alt_texts,urls))
    return results



def extract_markdown_links(text):
    anchor_texts = re.findall(r"\[(.*?)\]",text)
    urls = re.findall(r"\((.*?)\)",text)
    results = list(zip(anchor_texts,urls))
    return results

print(extract_markdown_links("![](https://www.github.com) and ![steam](https://www.steampowered.com)"))