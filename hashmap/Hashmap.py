import pandas as pd
Names = pd.read_csv('FirstName,LastName.csv')

class HashMap:
        def __init__(self, size=100):
            self.size = size
            self.buckets = [[]for _ in range(size)]
        
        def Hash_Function(self,key):
              pass
