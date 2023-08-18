def palindrome(word, index):
    #     if word == word[::-1]:
    #         return f"{word} is a palindrome"
    #     else:
    #         return f"{word} is not a palindrome"

    # advanced algo
    return False if not word == word[::-1] else True

    # advanced algo for nums
    # return False if x < 0 else x == int(str(x)[::-1])

    # algo for linked lists
    #class ListNode:

    # def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    #     class Solution:
#         def isPalindrome(self, head: Optional[ListNode]) -> bool:
#             values = []
#             current_node = head
#             while current_node is not None:
#                 values.append(current_node.val)
#                 current_node = current_node.next
#             return values == values[::-1]

print(palindrome("abcba", 0))
print(palindrome("peter", 0))