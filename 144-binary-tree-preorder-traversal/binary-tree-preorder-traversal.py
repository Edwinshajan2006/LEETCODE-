
class Solution:
    def preorderTraversal(self, root):
        preorder_result = []

        if root is None:
            return preorder_result

        node_stack = [root]

        while len(node_stack) > 0:
            current_node = node_stack.pop()
            preorder_result.append(current_node.val)

            if current_node.right is not None:
                node_stack.append(current_node.right)

            if current_node.left is not None:
                node_stack.append(current_node.left)

        return preorder_result
