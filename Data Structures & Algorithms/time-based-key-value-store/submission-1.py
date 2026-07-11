class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([value , timestamp])
        else:
            self.dic[key] = [[value , timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        ls = self.dic[key]

        i = 0
        j = len(ls)-1
        ans =""
        if ls[-1][1] <= timestamp:
            return ls[-1][0]
        while i <= j:
            mid = int((i+j)/2)
            if ls[mid][1] == timestamp:
                return ls[mid][0]
            elif ls[mid][1] < timestamp:
                ans = ls[mid][0]
                i = mid+1
            else:
                j = mid-1
        return ans
        
