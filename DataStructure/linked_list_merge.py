from linked_list import LinkedList

def merge_sort(linkedlist):
    """
    Sorts a linked list in ascending 
    """

    if linked_list.size() == 1:
        return linkedlist
    elif linkedlist.head is None:
        return linkedlist