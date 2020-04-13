# Given a list of n numbers, determine if it contains any duplicate numbers.
# Quesitons
    # What's the return value? (Total number of duplicate numbers, list of numbers that are duplicates, true or false?)
# Assumptions
    # Return true or false
# Psuedocode
""" 
function duplicates, params arr
	create an empty set 
	for each element in the array
		check if the element is in the set
			if not, add element to the set
			else, return false
	return true
"""

# Solution
def duplicates(arr):
    duplicates = set()
    for num in arr:
        if num not in duplicates:
            duplicates.add(num)
        else:
            return True
    return False


a = [1, 2, 3, 4, 6]
b = [1, 2, 3, 4, 6, 6]
c = []
print(duplicates(b))

# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.
# Questions
    # Is the linked list sorted?
    # Do we know the length of the list? Can we access it? 
    # What do we return if the list is 2 items or less?
# Assumptions
    # List is not sorted
    # Do not have access to the length
# Pseudocode - brute force
"""
function mid_item, params linked_list
    create counter variable and set it to 0
    create an empty array to store the middle-values in
    loop through linked list and increment counter until we reach the end of the list
    calculate "index" of middle item (counter // 2)
    loop through linked list until counter is 0
        if counter is less than 2, then append to middle-values array
        decrement counter by 1
    if counter is divisible by 2, return array
    else, return first item of array
    
"""

# Solution
def middle(lst):
    counter = 0
    mid = list()
    head = lst
    while lst is not None:
        counter += 1
        lst = lst.next
    mid_index = counter // 2
    lst = head
    while lst is not None and mid_index >= 0:
        if mid_index <= 1:
            mid.append(lst.val)
        mid_index -= 1
        lst = lst.next
    return mid if counter % 2 == 0 else mid[1]


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def to_linked_list(lst):
    head = ListNode(lst[0])
    next_node = head
    for i in range(1, len(lst)):
        next_node.next = ListNode(lst[i])
        next_node = next_node.next
    next_node = next_node.next
    return head


def print_linked_list(lst):
    current = lst
    while current is not None:
        print(current.val)
        current = current.next

a = [1, 2, 3, 4, 5]
a_ll = to_linked_list(a)
b = to_linked_list([1, 2, 3, 4, 5, 6])
# print_linked_list(a_ll)
print(middle(b))
