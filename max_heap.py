# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# ERIN O'CONNELL

class MaxHeap:
   
   def __init__(self):
      self._data = []
      self.size = 0

   def _size(self):
      return len(self._data)

   def _is_empty(self):
      return len(self._data) == 0   

   def _last_index(self):
      return len(self._data) -1   

   def _value_at(self, index):
      return self._data[index]   


