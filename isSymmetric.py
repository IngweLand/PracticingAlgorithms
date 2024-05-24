# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_nodes = [root.left]
        right_nodes = [root.right]
        while True:
            if len(left_nodes) != len(right_nodes):
                return False
            if not left_nodes and not right_nodes:
                return True
            left_values = [node.val if node is not None else None for node in (
                    left_nodes)]
            right_values = [node.val if node is not None else None for node in
                            right_nodes][::-1]
            if left_values != right_values:
                return False
            lns = []
            rns = []
            for node in left_nodes:
                if node is not None:
                    lns.append(node.left)
                    lns.append(node.right)
            for node in right_nodes:
                if node is not None:
                    rns.append(node.left)
                    rns.append(node.right)
            left_nodes = lns
            right_nodes = rns



