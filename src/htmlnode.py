class HTMLNode():
    def __init__(self, tag=None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = " "
        for key,value in self.props.items():
            result = result + f'{key}="{value}" '
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"




class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)
        
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"