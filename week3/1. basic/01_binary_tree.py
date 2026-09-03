class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):

    result = []

    if root == None:
        return result

    result.append(root.value)
    result += preorder(root.left)
    result += preorder(root.right)

    return result


def inorder(root):

    result = []

    if root == None:
        return result    

    result += inorder(root.left)
    result.append(root.value)
    result += inorder(root.right)

    return result


def postorder(root):

    result = []

    if root == None:
        return result    

    result += postorder(root.left)
    result += postorder(root.right)
    result.append(root.value)

    return result



# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")
