def reverseList(self , head):
	current =head
	prev =none
	while current:
		nex=current.next
		current.next=prev
		prev=current
		current=nex
	return prev
  
