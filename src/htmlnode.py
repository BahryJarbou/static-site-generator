class HTMLNode():
    def __init__(self, tag=None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        result = " "
        for key,value in self.props.items():
            result += f'{key}="{value}" '
        return result[:-1]
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self,node):
         if self.tag == node.tag and self.children == node.children and self.props == node.props:
            return True
         else:
            return False




class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)
        
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")
        if self.tag == None:
            return self.value
        
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag,None,children,props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag of a parent node can't be None")
        if self.children == None:
            raise ValueError("Parent's children can't be None")
        
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(lambda x: x.to_html(), self.children)))}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(lambda x: x.to_html(), self.children)))}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"