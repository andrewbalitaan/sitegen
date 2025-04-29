import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()



# import unittest

# from htmlnode import HTMLNode, LeafNode


# class TestHTMLNode(unittest.TestCase):
#     def test_not_eq(self):
#         node = HTMLNode("p", "hello", props={"href": "https://www.google.com"})
#         node2 = HTMLNode("a", "hello", props={"href": "https://www.google.com"})
#         self.assertNotEqual(node, node2)
        
#     def test_props_to_html(self):
#         node = HTMLNode("a", "hello", props={"href": "https://www.google.com"})
#         node2 = 'href="https://www.google.com"'
#         self.assertEqual(node.props_to_html(), node2)
        
#     def test_values(self):
#         node = HTMLNode(
#             "div",
#             "I wish I could read",
#         )
#         self.assertEqual(
#             node.tag,
#             "div",
#         )
#         self.assertEqual(
#             node.value,
#             "I wish I could read",
#         )
#         self.assertEqual(
#             node.children,
#             None,
#         )
#         self.assertEqual(
#             node.props,
#             None,
#         )

# # class TestLeafNode(unittest.TestCase):
# #     def test_leaf_to_html_p(self):
# #         node = LeafNode("p", "Hello, world!")
# #         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


# # Created with help

# class TestLeafNode(unittest.TestCase):

#     # ─── Positive cases ──────────────────────────────────────────────────────

#     def test_plain_text_no_tag(self):
#         node = LeafNode(None, "Just text")
#         self.assertEqual(node.to_html(), "Just text")

#     def test_tag_without_props(self):
#         node = LeafNode("p", "Hello, world!")
#         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#     def test_tag_with_single_prop(self):
#         node = LeafNode("a", "Google", {"href": "https://google.com"})
#         self.assertEqual(
#             node.to_html(),
#             '<a href="https://google.com">Google</a>'
#         )

#     def test_tag_with_multiple_props_order_agnostic(self):
#         props = {"id": "logo", "class": "center"}
#         node  = LeafNode("img", "ignored-alt", props)          # value still required
#         html  = node.to_html()
#         # Order of attributes isn’t guaranteed, so check presence, not sequence
#         self.assertTrue(html.startswith("<img"))
#         self.assertIn('id="logo"',   html)
#         self.assertIn('class="center"', html)
#         self.assertTrue(html.endswith("</img>"))   # closing tag present

#     # ─── Negative / validation cases ────────────────────────────────────────

#     def test_constructor_requires_value(self):
#         with self.assertRaises(ValueError):
#             LeafNode("p", None)

#         with self.assertRaises(ValueError):
#             LeafNode()                         # tag & value both None

#     # ─── HTMLNode helper coverage ───────────────────────────────────────────

#     def test_props_to_html_none(self):
#         node = HTMLNode("div", "x")
#         self.assertEqual(node.props_to_html(), "")

#     def test_props_to_html_trailing_space_stripped(self):
#         node = HTMLNode("div", "x", props={"data-id": "7"})
#         self.assertEqual(node.props_to_html(), 'data-id="7"')  # no trailing space

# if __name__ == "__main__":
#     unittest.main()