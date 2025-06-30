# This is an Interator example
## This code defines a custom iterator class `MyIterator` that can iterate over a given data structure.
# It includes methods for initialization, iteration, and fetching the next item.
# If the end of the data is reached, it raises a `StopIteration` exception.

class MyIterator: # Custom iterator class
    
    def _init_(self, data): #function difinfe for initialization
        self.DATA = data
        
    def _iter_(self): # This method initializes the iterator
        self,index = self.DATA, 0
        return self
    
    def _next_(self): # This method returns the next item in the data structure
        if self.index <len(self.DATA): # Check if there are more items to iterate over
            result = self.DATA[self.index]
            self.index += 1
            return