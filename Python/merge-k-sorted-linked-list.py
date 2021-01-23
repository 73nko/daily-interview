class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    new_head = current = Node(-1)
    while any(lst is not None for lst in lists):
        # Get min of all non-None lists
        current_min, i = min((lst.val, i)
                             for i, lst in enumerate(lists) if lst is not None)
        lists[i] = lists[i].next
        current.next = Node(current_min)
        current = current.next
    return new_head.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
