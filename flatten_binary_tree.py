# from lintcode import (
#     TreeNode,
# )

from collections import deque
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing

    description: Flatten a binary tree to a fake "linked list" in pre-order traversal.
    Here we use the right pointer in TreeNode as the next pointer in ListNode.

    Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
    """
    def flatten(self, root: TreeNode):
        # write your code here
        # we can use bfs to traverse the binary tree 
        # use queue to store the node from root, left, to right. 

        if not root:
            return root

        stack = []  # in python, stack is a list(). 
        visited = set()
        linked_list = deque()
        # print(linked_list)
        stack.append(root)
        
        while stack:

            for _ in range(len(stack)):

                node = stack.pop()
                print(node.val)
                linked_list.append(node)
                
                if node not in visited:
                    
                    visited.add(node)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)
        # print(linked_list)

        # stack.append(root)
        # print(stack)

        # new_root = TreeNode(root.val)

        queue = deque([root])
        print(linked_list)
        new_node = linked_list.popleft()
        # while len(linked_list) > 1:
            # new_node = linked_list.popleft()
        while len(linked_list) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node.val)

                next_node = linked_list.popleft()
                node.left = None
                node.right = next_node
                queue.append(next_node)


# example = {1,2,5,3,4,#,6}, {1,2}