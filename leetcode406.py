people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
m=2
n=6
result=[]
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 贪心算法
        people.sort(key = lambda x : (-x[0],x[1]))
        queue = []
        for p in people:
            queue.insert(p[1],p)
        return queue
if __name__ == "__main__":
    s = Solution()
    result=s.reconstructQueue(people)
    for i in range(n-1,-1,-1):
        for j in range(0,m):
            print(result[i][j])
        print()
