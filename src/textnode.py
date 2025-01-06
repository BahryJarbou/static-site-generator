from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "Normal text"
	BOLD_TEXT = "Bold text"
	ITALIC_TEXT = "Italic text"
	CODE_TEXT = "Code text"
	LINK = "Link"
	IMAGE = "Image"

class TextNode():
	def __init__(self, text, text_type, url = None):
		self.text = text
		self.text_type = text_type
		self.url = url
	def __eq__(self,node):
		if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
			return True
		else:
			return False

	def __repr__(self):
		if self.url != None:
			return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"
		else:
			return f"TextNode(\"{self.text}\", {self.text_type})"
