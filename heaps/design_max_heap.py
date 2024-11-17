class MaxHeap:
    """
    MaxHeap implementation where the root node is the maximum value.

    This class has basic insertion(add), and heapify-up method.
    """
    
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1
    # END OF HEAP HELPER METHODS
    
    def add(self, element):
        self.count += 1
        print(f"Adding: {element} to {self.heap_list}")
        self.heap_list.append(element)
        self.heapify_up()
        
    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print(f"Heap Restored {self.heap_list}")
