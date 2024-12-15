# 트리 순회(재귀)
# preorder : self left right
# inorder : left self right
# postorder : left right self
# 이진검색트리 성질 -> inorder -> 오름차순으로 정렬

def solution():

    init = False
    min = 0
    prev = 0
    INF = 1e9

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        # self처리
        if not init:
            init = True
        else:
            min = min(min, root.val - prev)

        prev = root.val
        inorder(root.right)

    def getMinimumDifference(root):
        init = False
        min = INF
        inorder(root)
        return min
