class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node.value) + " -> "
            node = node.next

        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    new_list = LinkedList()
    new_set = set()
    node1 = llist_1.head
    node2 = llist_2.head

    while node1:
        new_set.add(node1.value)
        node1 = node1.next

    while node2:
        new_set.add(node2.value)
        node2 = node2.next

    for item in new_set:
        new_list.append(item)

    return new_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    new_set = set()
    node1 = llist_1.head
    node2 = llist_2.head

    while node1:
        while node2:
            if node1.value == node2.value:
                new_set.add(node1.value)
            node2 = node2.next
        node1 = node1.next
        node2 = llist_2.head

    for i in new_set:
        new_list.append(i)

    return new_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


test1_result = union(linked_list_1, linked_list_2)
test1_answer = "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "

test2_result = intersection(linked_list_1, linked_list_2)
test2_answer = "4 -> 21 -> 6 -> "

print ("Pass" if (str(test1_result) == test1_answer) else "Fail")
print ("Pass" if (str(test2_result) == test2_answer) else "Fail")

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test3_result = union(linked_list_3, linked_list_4)
test3_answer = "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "

test4_result = intersection(linked_list_3, linked_list_4)

print ("Pass" if (str(test3_result) == test3_answer) else "Fail")
print ("Pass" if (str(test4_result) == "") else "Fail")


# Big O Notation
# The `union` function has two while loops, one for each linked list.
# Therefor its performance is Big O of N times 2: O(2n) or O(n).

# The `intersection` function has a loop within a loop, checking for
# identical values in either list. It's performance is thus a bit worse
# at Big O of N squared: O(n**2).

# In both functions I use Python's `set` function to create a unique cache list
# of either the union or intersection of the items in both lists. This adds another
# loop for iterating thru the final set, but it's effect on performance is minimal.
