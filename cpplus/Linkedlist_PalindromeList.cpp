//============================================================================
// Name        : Linkedlist_PalindromeList.cpp
// Author      : dmtwong
// Version     :
// Copyright   : List 2 pointer Q1
// Description : Hello World in C++, Ansi-style
//============================================================================
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.
// Notes:
// Expected solution is linear in time and constant in space.
// For example,
// List 1-->2-->1 is a palindrome.
// List 1-->2-->3 is not a palindrome.

#include <iostream>
#include <vector>
using namespace std;
//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int getVal(ListNode *A){
	int curr_val;
	if (A != NULL){
		curr_val = A->val;
		A = A->next;
	}
	return curr_val;
}
//int Solution::lPalin(ListNode* A) {
int lPalin(ListNode* A) {
	vector <int> val_list;
	int temp_val;
	int n_list;
    ListNode *temp = A;
    while (temp != NULL){
		temp_val = getVal(temp);
		val_list.push_back(temp_val);
        temp = temp->next;
	}
	n_list = val_list.size();
	int i = 0, j = n_list - 1;
	bool tag = true;
	while ((i < j) and tag){
		if (val_list[i] == val_list[j]){
			i += 1;
			j -= 1;
		} else {
			tag = false;
		}
	}
	return int(tag);
}

//Editorial:

//ListNode*reverse(ListNode*head)
//{
//    ListNode*prev=NULL;
//    ListNode*curr=head;
//    ListNode*n;
//    while(curr!=NULL)
//    {
//        n = curr->next;
//        curr->next = prev;
//        prev = curr;
//        curr = n;
//    }
//    return prev;
//}
//int Solution::lPalin(ListNode* A) {
//    ListNode*slow = A;
//    ListNode*fast = A;
//    if(A==NULL || A->next==NULL) return 1;  // returning true if num of nodes are 0 or 1
//    if(A->next->next==NULL)
//    {
//        if(A->val == A->next->val) return 1;  //if num of nodes are 2 checking palindrom or not
//        else return 0;
//    }
//    while(fast->next!=NULL && fast->next->next!=NULL) //finding middile node of linkedlist
//    {
//        slow = slow->next;
//        fast = fast->next->next;
//    }
//    ListNode*temp = reverse(slow->next); //reversing linked list after midpoint
//    while(A!=NULL && temp!=NULL)
//    {
//        if(A->val != temp->val) return 0;
//        A = A->next;
//        temp=temp->next;
//    }
//    return 1;
//}

//C:
//
// * Definition for singly-linked list.
// * struct ListNode {
// *     int val;
// *     struct ListNode *next;
// * };
// *
// * typedef struct ListNode listnode;
// *
// * listnode* listnode_new(int val) {
// *     listnode* node = (listnode *) malloc(sizeof(listnode));
// *     node->val = val;
// *     node->next = NULL;
// *     return node;
// * }
//
//
// * @input A : Head pointer of linked list
// *
// * @Output Integer
//
//int reverse(listnode **left,listnode *right){
//    if(right==NULL)
//        return 1;
//    int i=reverse(left,right->next);
//
//    if(i==0)
//        return 0;
//
//    int p = (right->val==(*left)->val);
//    (*left)=(*left)->next;
//
//    return p;
//
//}
//int lPalin(listnode* A) {
//
//    return reverse(&A,A);
//
//}
//
//Scala:
///*
// * Definition for singly-linked list
// * class ListNode(val xc: Int){
// *     var value: Int = xc
// *     var next: ListNode = null
// * }
//*/
//class Solution {
//    def lPalin(A: ListNode): Int  = {
//        import scala.collection.mutable.ArrayBuffer
//
//    var len = 0
//    var n = A
//    while (n != null) {
//      len += 1
//      n = n.next
//    }
//
//    val fh = (len / 2) - 1
//    val sh = len - 1 - fh
//
//    n = A
//    var i  = 0
//    val secHalf: ArrayBuffer[Int] = ArrayBuffer()
//    while (n != null) {
//      if (i >= sh) secHalf += n.value
//      i += 1
//      n = n.next
//    }
//
//    var res = 1
//    n = A
//    for (i <- secHalf.length - 1 to 0 by - 1 if res == 1) {
//      if (secHalf(i) != n.value) res = 0
//      else n = n.next
//    }
//
//    res
//  }
//
//}
//
//GO:
///**
// * Definition for singly-linked list.
// * type listNode struct {
// *     value int
// *     next *listNode
// * }
// *
// * func listNode_new(val int) *listNode{
// *     var node *listNode = new(listNode)
// *     node.value = val
// *     node.next = nil
// *     return node
// * }
// */
///**
// * @input A : Head pointer of linked list
// *
// * @Output Integer
// */
//
// //Compare twoLists
//func compareTwoLists(first, second *listNode) int {
//    temp1 := first
//    temp2 := second
//    for temp1 != nil && temp2 != nil {
//        if temp1.value == temp2.value {
//            temp1 = temp1.next
//            temp2 = temp2.next
//        } else {
//            return 0
//        }
//    }
//
//    if temp1 == nil && temp2 == nil {
//        return 1
//    }
//
//    return 0
//}
//
///* Helper Function to Reverse LinkedList */
//func Reverse(root *listNode) *listNode {
//    if root == nil || root.next == nil {
//        return root
//    }
//    // Reach till end of list and start recursion
//    rest := Reverse(root.next)
//    root.next.next = root
//    root.next = nil
//    return rest
//}
//
//func lPalin(root *listNode )  (int) {
//    var first, second *listNode
//    fast := root
//    slow := root
//    var middleNode *listNode
//
//    var prev *listNode
//    if root == nil || root.next == nil{
//        return 1
//    }
//    for fast != nil && fast.next != nil {
//        fast = fast.next.next
//        prev = slow
//        slow = slow.next
//
//    }
//
//    //In case of even, fast will be non nil.
//    if fast != nil {
//        middleNode = slow
//        second = slow.next
//        prev.next = nil
//    } else {
//        second = slow
//        prev.next = nil
//    }
//
//    first = root
//    secondreversed := Reverse(second)
//    result := compareTwoLists(first, secondreversed)
//    second = Reverse(secondreversed)
//
//
//    // Recreate the list
//    if middleNode != nil {
//        prev.next = middleNode
//        middleNode.next = second
//    } else {
//        prev.next = second
//    }
//
//    return result
//
//}


