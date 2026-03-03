# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        if temp.next == None:
            head=None
            return head
        #find total Count
        tc=1
        while temp.next != None:
            tc+=1
            temp=temp.next
        print(tc)
        temp=head
        tempCount=1
        prev=head

        ## for delete front case:- 
        print(tc,n)
        if tc-n == 0:
            prev=head
            head=prev.next
            #head.next=head.next
            return head
        while temp.next != None and tempCount <= tc-n:
            print("value ",temp.val) 
            tempCount+=1
            prev=temp
            temp=temp.next

        print(prev.val)
        prev.next=temp.next
        #temp.next=temp.next

        return head
        
        #return head