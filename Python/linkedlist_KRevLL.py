# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:26:46 2022

@author: mingt
"""

# Given a singly linked list and an integer K, reverses the nodes of the
# list K at a time and returns modified linked list.
# NOTE : The length of the list is divisible by K
# Example :
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
# Try to solve the problem using constant extra space.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
# class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
# 	def reverseList(self, A, B):
def reverseList(A, B):
    if not A or B == 1:
        return A
    temp = ListNode(999)
    temp.next = A
    # print(temp, temp.val, temp.next)
    curr_node, next_node, last_node = temp, temp, temp
    n_A, interval_step = 0, 0
 
    while curr_node != None:
        curr_node = curr_node.next
        n_A += 1
    
    while next_node:
        # print('Start at', next_node.val)
        curr_node = last_node.next  
        next_node = curr_node.next 
        interval_step = (n_A > B and B) or (n_A - 1) 
        # print('before while', curr_node.val, next_node.val, interval_step)
        for i in range(1, interval_step):
            # print('at i = ', i, curr_node.val, next_node.val, last_node.val)
            curr_node.next = next_node.next
            next_node.next = last_node.next
            last_node.next = next_node
            next_node = curr_node.next
        # print('out the for loop', curr_node.val, next_node.val, last_node.val)     
        last_node = curr_node
        n_A -= B
        # print(next_node, next_node.next)
    return temp.next

# testing case
# node_1a = ListNode(1)    
# node_1b = ListNode(2)
# node_1c = ListNode(3)
# node_1d = ListNode(4) 
# node_1e = ListNode(5)
# node_1f = ListNode(6)

# node_1a.next = node_1b
# node_1b.next = node_1c
# node_1c.next = node_1d
# node_1d.next = node_1e
# node_1e.next = node_1f
# reverseList(node_1a, 2)
# A : [ 6 -> 10 -> 0 -> 3 -> 4 -> 8 ]
# B : 3

# Editorial:
#     class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return the head node in the linked list
#     def reverseList(self, A, B):
#         if B == 1:
#             return A
#         l=None
#         prev,curr=None,A
#         while curr!=None:
#             k=B
#             head=curr
#             p,n=None,curr.next
#             while curr!=None and k>1:
#                 curr.next=p
#                 p=curr
#                 curr=n
#                 n=n.next if n else None
#                 k-=1
#             head.next=curr.next
#             curr.next=p
#             if prev:
#                 prev.next=curr
#             else:
#                 l=curr
#             prev=head
#             curr=head.next
#         return l

#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }

# class Solution {
#     def reverseList(A: ListNode, B: Int): ListNode  = {
#     if (B < 2) A
#     else {

#       var n = A
#       var last = A
#       var acc: ListNode = null

#       while (n != null) {
#         var i = 0
#         var s: ListNode = null
#         val sLast = n

#         while (i < B) {
#           val t = n.next
#           n.next = s
#           s = n
#           n = t
#           i += 1
#         }

#         if (acc == null) acc = s
#         else last.next = s
#         last = sLast

#       }

#       acc
#     }
#   }
# }
