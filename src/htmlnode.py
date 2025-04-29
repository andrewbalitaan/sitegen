class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    

# class HTMLNode:
#     def __init__(self, tag=None, value=None, children=None, props=None):
#         self.tag = tag
#         self.value = value
#         self.children = children
#         self.props = props

#     def to_html(self):
#         raise NotImplementedError("to_html method not implemented")

#     def props_to_html(self):
#         if self.props is None:
#             return ""
#         props_html = ""
#         for prop, val in self.props.items():
#             props_html += f'{prop}="{val}" '      # keep the space
#         return props_html.strip()                 # ← trim it once

#     def __repr__(self):
#         return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


# class LeafNode(HTMLNode):
#     def __init__(self, tag=None, value=None, props=None):
#         """
#         A leaf node cannot have children and must carry a value.
#         If tag is None it renders as raw text.
#         """
#         if not value:
#             raise ValueError("LeafNode must be instantiated with a non-empty value")
#         super().__init__(tag=tag, value=value, children=None, props=props)

#     def to_html(self):
#         """Render this node to an HTML string."""
#         if self.tag is None:
#             return self.value

#         props_html = self.props_to_html().strip()
#         open_tag = f"<{self.tag}{(' ' + props_html) if props_html else ''}>"
#         return f"{open_tag}{self.value}</{self.tag}>"


# class ParentNode(HTMLNode):
#     def __init__(self, tag, children, props=None):
#         super().__init__(tag=tag, chilren=children, props=props)
        
#     def to_html(self):
#         if not self.tag:
#             raise ValueError("Tag required")
        
#         if not self.children:
#             raise ValueError("Children required")
        
#         leaf_nodes = 0
#         for item in self.children:
#             if isinstance(item, LeafNode):
#                 leaf_nodes += 1
                
#         if len(self.children) == leaf_nodes:
#             return_string = ""
#             for item in self.children:
#                 props_html = self.props_to_html().strip()
#                 open_tag = f"<{self.tag}{(' ' + props_html) if props_html else ''}>"
#                 return_string += f"{open_tag}{self.value}</{self.tag}>" 
#             return return_string
        
        
        

# class LeafNode(HTMLNode):
#     def __init__(self, tag=None, value=None, props=None):
#         if value is None:
#             raise ValueError
#         super().__init__(tag=tag, value=value, children=None, props=props)
        
#     def to_html(self):
        
        
#         if self.tag is None:
#             return self.value
        
#         props_html = self.props_to_html()
#         open_tag = f"<{self.tag}{(' ' + props_html) if props_html else ''}>"

#         return f"{open_tag}{self.value}</{self.tag}>"
    
        # return(f"<{self.tag>{self.value}</{self.tag}>")
        
        


# Original attempt

# class HTMLNode:
#     def __init__(self, tag=None, value=None, children=None, props=None):
#         self.tag = tag
#         self.value = value
#         self.children = children
#         self.props = props
        
#     def to_html(self):
#         raise NotImplementedError
    
#     def props_to_html(self):
#         prop_string = ""
#         for k,v in self.props.items():
#             prop_string += f'{k}="{v}" '
#         return prop_string
    
#     def __repr__(self):
#         return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"
    
#     def __eq__(self, other):
#         if not isinstance(other, HTMLNode):
#             return False
#         return (
#             self.tag == other.tag
#             and self.value == other.value
#             and self.props == other.props
#             and self.children == other.children
#         )