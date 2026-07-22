from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)
        maxi = 0
        for x in tasks:
            dic[x] += 1
            maxi = max(maxi , dic[x])
        count = 0
        for key , value in dic.items():
            if value == maxi:
                count +=1

        time = (maxi - 1) * (n+1) + count

        return max(len(tasks), time)


        