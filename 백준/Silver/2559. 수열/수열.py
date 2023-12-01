N, K = map(int, input().split())
nList = list(map(int, input().split()))

maxSum = sum(nList[:K])
windowSum = maxSum

for i in range(K, N):
    prevIndex = i - K

    windowSum -= nList[prevIndex]
    windowSum += nList[i]

    maxSum = max(windowSum, maxSum)

print(maxSum)