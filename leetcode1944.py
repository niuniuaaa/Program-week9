heights=[10,6,8,5,11,9]
def canSeePersonsCount(heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        s = list()

        for i in range(n - 1, -1, -1):
            while s:
                ans[i] += 1
                if heights[i] > heights[s[-1]]:
                    s.pop()
                else:
                    break
            s.append(i)

        return ans

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
