import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_default_url(self):
        node3 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node3.url, None)
        
    def test_different_text(self):
        node4 = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node4, node5)
    
    def test_another(self):
        node6 = TextNode("This is a text node", TextType.ITALIC)
        node7 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node6, node7)

if __name__ == "__main__":
    unittest.main()