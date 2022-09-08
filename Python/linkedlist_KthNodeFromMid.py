# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:31:39 2022

@author: mingt
"""
# Problem Description
# Given a linked list A of length N and an integer B.
# You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.
# If no such element exists, then return -1.
# NOTE:
# Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.
# Problem Constraints
# 1 <= N <= 105
# 1<= Value in Each Link List Node <= 103
# 1 <= B <= 105
# Input Format
# First argument is the head pointer of the linkedlist A.
# Second argument is an integer B.
# Output Format
# Return an integer denoting the value of the Bth from the middle towards the head of the linked list A. If no such element exists, then return -1.
# Example Input
# Input 1:
#  Input 2:
#  A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
#  B = 2
#  Input 3:
#  A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
#  B = 10
# Example Output
# Output 1:
#  4
#  Output 2:
#  14
#  Output 3:
#  -1

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null

        
# class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    # def solve(self, A, B):
# def solve(A, B):
#     def solve(self, A, B):
    def solve(A, B):
        def countNode(node_1):
            count = 0
            temp_node = node_1            
            while (temp_node):
                # print(temp_node.val, temp_node.next)
                count += 1
                temp_node = temp_node.next
                # try:
                    # print('Now next point to ', temp_node.next)
                # except:
                    # print('stop at count = ', count)
            return count
        n_A = countNode(A)
        mid_A = int(n_A / 2 + 1)
        steps = mid_A - B
        
        if steps <= 0:
            return -1
        
        temp_node = A
        result = 1
        while (result != steps):
            result += 1
            temp_node = temp_node.next
        return temp_node.val

# # test case:
# node_1a = Node(3)    
# node_1b = Node(4)
# node_1c = Node(7)
# node_1d = Node(5) 
# node_1e = Node(6)
# node_1f = Node(16)
# node_1g = Node(15)
# node_1h = Node(61)
# node_1i = Node(16)
# node_1a.next = node_1b
# node_1b.next = node_1c
# node_1c.next = node_1d
# node_1d.next = node_1e
# node_1e.next = node_1f
# node_1f.next = node_1g
# node_1g.next = node_1h
# node_1h.next = node_1i

# # char_list_1 = "abcdefghi"
# # name_list_1 = ["node_1" + char_list_1[i] for i in range(len(char_list_1))]
# #  A = 3 -> 4 -> 7 -> 5 -> 6 -> 1 6 -> 15 -> 61 -> 16
# #  B = 3
# solve(node_1a, 3)      

# Scala:

#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }

# class Solution {
#     def solve(A: ListNode, B: Int): Int  = {
        
#         val head1 = A
#         val K = B
        
#         var slow = head1
#         var fast = head1
#         var midPosition = 0
        
#         while(fast != null && fast.next != null) {
#             slow = slow.next
#             fast = fast.next.next
#             midPosition = midPosition + 1
#         }
        
#         var reqPosition = midPosition - K
        
#         if(reqPosition < 0) return -1
        
#         var result = -1
#         var currPosition = 0
#         var currNode = head1
#         while(currNode != null && currPosition < reqPosition) {
#             currPosition = currPosition + 1
#             currNode = currNode.next
#         }
        
#         if(currNode != null) result = currNode.value
        
#         result
#     }
# }

# c++

#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };

# int Solution::solve(ListNode* A, int B) {

#     ListNode*p=A;
#     int s=0;
#     while(p)
#     {
#         s++;p=p->next;
#     }

#     B=B+((s+1)/2);

#     B=s-B;

#     if(B<0) return -1;

#     p=A;

#     while(B--)
#     {
#         p=p->next;
#     }

#     return p->val;
# }
