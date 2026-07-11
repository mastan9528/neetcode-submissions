from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_dict=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([value , timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        x = self.time_dict[key]
        i = 0
        j = len(x)-1
        st = ""
        while i <= j:
            mid = (i+j)//2

            if x[mid][1] <= timestamp:
                st = x[mid][0]
                i = mid+1
            else:
                j = mid-1

        return st



        
