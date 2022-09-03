# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:05:02 2022

@author: mingt
"""

# Problem Description
# Given a Linked List A consisting of N nodes.
# The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.
# You need to sort the linked list and return the new linked list.
# NOTE:
# Try to do it in constant space.
# Problem Constraints
#  1 <= N <= 105
#  A.val = 0 or A.val = 1
# Input Format
# First and only argument is the head pointer of the linkedlist A.

# Output Format
# Return the head pointer of the new sorted linked list.

    # def solve(self, A):
    def solve(A):
        if ((A.val == None) or (A.next == None)):
            return A
        zeros = 0
        ones = 0
        
        temp = A        
        while (temp != None):    
            if (temp.val == 0):
                zeros += 1
            else:
                ones += 1
            temp = temp.next
        
        temp = A # reset temp to head node of A again 
        while (zeros > 0):
            temp.val = 0
            temp = temp.next
            zeros -= 1
        while (ones > 0):
            temp.val = 1;
            temp = temp.next;
            ones -= 1;
        
        return A

# Editorial Scala:
#     /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def solve(A: ListNode): ListNode  = {
#         if(A==null){
#             A
#         }else{
#             var h = A
#             var head:ListNode=null
#             var tail:ListNode=null
            
#             while(h!=null){
#                 if(head==null){
#                     head=h
#                     tail=h
#                     h=h.next
#                 }else if(h.value==0){
#                     val t=h.next
#                     h.next=head
#                     head=h
#                     h=t
#                 }else{
#                     tail.next=h
#                     tail=h
#                     h=h.next
#                     tail.next=null
#                 }
#             }
            
#             head
#         }
#     }
# }
                    
# Editorial C++
# **
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
#  int countZero(ListNode *A)
#  {
#      int z=0;
#      while(A!=NULL)
#      {
#          if(A->val==0)
#          z++;
#          A=A->next;
#      }
#      return z;
#  }
#  void setValues(ListNode*A,int z)
#  {
#      while(z!=0)
#      {
#          z--;
#          A->val=0;
#          A=A->next;
#      }
#      while(A!=NULL)
#      {
#          A->val=1;
#          A=A->next;
#      }
#  }
# ListNode* Solution::solve(ListNode* A) {
#     int z=countZero(A); // count number of zeroes
#     setValues(A,z); // set first 'z' values to zero and remaining to one
#     return A;
# }
# Editorial C
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     struct ListNode *next;
#  * };
#  * 
#  * typedef struct ListNode listnode;
#  * 
#  * listnode* listnode_new(int val) {
#  *     listnode* node = (listnode *) malloc(sizeof(listnode));
#  *     node->val = val;
#  *     node->next = NULL;
#  *     return node;
#  * }
#  */
# /**
#  * @input A : Head pointer of linked list 
#  * 
#  * @Output head pointer of list.
#  */
# listnode* solve(listnode* A) {
#     listnode *temp=A;
#     int count[2]={0,0};
#     if(A==NULL){
#         return A;
#     }
#     while(temp){
#         count[temp->val]+=1;
#         temp=temp->next;
#     }
    
#     temp=A;
#     int i=0;
    
#     while(temp){
#         if(count[i]==0)
#         i++;
#         else{
#             temp->val = i;
#             --count[i];
#             temp=temp->next;
#         }
#     }
    
#     return A;
# }


# Editorial GO
# /**
#  * Definition for singly-linked list.
#  * type listNode struct {
#  *     value int
#  *     next *listNode
#  * }
#  * 
#  * func listNode_new(val int) *listNode{
#  *     var node *listNode = new(listNode)
#  *     node.value = val
#  *     node.next = nil
#  *     return node
#  * }
#  */
# /**
#  * @input A : Head pointer of linked list 
#  * 
#  * @Output head pointer of list.
#  */
# func solve(A *listNode) *listNode {

#     if A == nil {
#         return A
#     }
#     zeroCount := 0
#     oneCount := 0
#     curr := A

#     for curr != nil {

#         if curr.value == 0 {
#             zeroCount++
#         } else {
#             oneCount++
#         }
#         curr = curr.next
#     }

#     curr = A
#     for curr != nil {
#         if zeroCount == 0 {
#             curr.value = 1
#         } else {
#             curr.value = 0
#             zeroCount--
#         }
#         curr = curr.next

#     }
#     return A
# }
