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
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
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
    union_set = set()
    current_node = llist_1.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    result = LinkedList()
    for value in union_set:
        result.append(value)

    return result

def intersection(llist_1, llist_2):
    set1 = set()
    set2 = set()

    current_node = llist_1.head
    while current_node:
        set1.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        set2.add(current_node.value)
        current_node = current_node.next

    intersect_set = set1.intersection(set2)

    result = LinkedList()
    for value in intersect_set:
        result.append(value)

    return result

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1 - Edge Case: Both lists are empty
linked_list_11 = LinkedList()
linked_list_12 = LinkedList()

expected_union_1 = ""
expected_intersection_1 = ""

print("\nTest case 1 - Edge Case: Both lists are empty")
result_union_1 = union(linked_list_11, linked_list_12)
result_intersection_1 = intersection(linked_list_11, linked_list_12)

if str(result_union_1) == expected_union_1 and str(result_intersection_1) == expected_intersection_1:
    print("Test case 1 passed")
else:
    print("Union:", result_union_1)
    print("Intersection:", result_intersection_1)

# Test Case 2 - Edge Case: One list is empty, the other contains duplicate elements
linked_list_13 = LinkedList()
linked_list_14 = LinkedList()

element_6 = [7, 7, 7, 7, 7]

for i in element_6:
    linked_list_14.append(i)

expected_union_2 = "7 -> "
expected_intersection_2 = ""

print("\nTest case 2 - Edge Case: One list is empty, the other contains duplicate elements")
result_union_2 = union(linked_list_13, linked_list_14)
result_intersection_2 = intersection(linked_list_13, linked_list_14)

if str(result_union_2) == expected_union_2 and str(result_intersection_2) == expected_intersection_2:
    print("Test case 2 passed")
else:
    print("Union:", result_union_2)
    print("Intersection:", result_intersection_2)

# Test Case 3 - Simple Test Case
linked_list_17 = LinkedList()
linked_list_18 = LinkedList()

element_9 = [1, 2, 3, 4]
element_10 = [3, 4, 5, 6]

for i in element_9:
    linked_list_17.append(i)

for i in element_10:
    linked_list_18.append(i)

expected_union_3 = "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> "
expected_intersection_3 = "3 -> 4 -> "

print("\nTest case 3 - Simple Test Case")
result_union_3 = union(linked_list_17, linked_list_18)
result_intersection_3 = intersection(linked_list_17, linked_list_18)

if str(result_union_3) == expected_union_3 and str(result_intersection_3) == expected_intersection_3:
    print("Test case 3 passed")
else:
    print("Union:", result_union_3)
    print("Intersection:", result_intersection_3)
