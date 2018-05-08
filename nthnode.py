class Node(object):

  def __init__(self, data=None, next_node=None):
      self.data = data
      self.next = next_node

def InsertNth(head, data, position):
    import pdb; pdb.set_trace()
    temp_posi=0
    temp_head=head
    if position == 0:
        return Node(data,head)
    while temp_posi < position-1:
        temp_head=temp_head.next
        temp_posi=temp_posi+1
    temp_head.next= Node(data,temp_head.next)
    return head
    
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.next=b
b.next=c
c.next=d
print InsertNth(a, 9, 3)
