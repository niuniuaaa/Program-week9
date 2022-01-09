S="baaca"
def orderlyQueue( S: str, K: int) -> str:
        if K>1:
            return "".join(sorted(S))
        n = len(S)
        minS = S
        for i in range(n):
            S = S[1:]+S[0]
            if S<minS:
                minS = S
        return minS

# Press the green button in the gutter to run the script.
word=orderlyQueue(S,3)
print(word)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
