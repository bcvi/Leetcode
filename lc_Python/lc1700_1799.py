from typing import List
import heapq, collections, itertools, functools, math


# 1705 - Maximum Number of Eaten Apples - MEDIUM
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples) or pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if i < len(apples) and apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                ans += 1
                if not pq[0][1]:
                    heapq.heappop(pq)
            i += 1
        return ans

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                if not pq[0][1]:
                    heapq.heappop(pq)
                ans += 1
            i += 1
        while pq:
            cur = heapq.heappop(pq)
            d = min(cur[0] - i, cur[1])
            i += d
            ans += d
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
        return ans


# 1706 - Where Will the Ball Fall - MEDIUM
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(grid), len(grid[0])
        for b in range(n):
            i = 0
            j = b
            succ = True
            while i < m:
                if grid[i][j] == 1 and j + 1 < n and grid[i][j + 1] == 1:
                    j += 1
                    i += 1
                elif grid[i][j] == -1 and j - 1 >= 0 and grid[i][j - 1] == -1:
                    j -= 1
                    i += 1
                else:
                    succ = False
                    break
            if succ:
                ans.append(j)
            else:
                ans.append(-1)
        return ans

    # for-else
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            col = j
            for row in grid:
                dir = row[col]
                col += dir
                if col < 0 or col == n or row[col] != dir:
                    break
            else:
                ans[j] = col
        return ans


# 1716 - Calculate Money in Leetcode Bank - EASY
class Solution:
    def totalMoney(self, n: int) -> int:
        div, mod = divmod(n, 7)
        ans = 0
        for i in range(mod):
            ans += i + 1 + div
        while div:
            ans += 28 + (div - 1) * 7
            div -= 1
        return ans

    def totalMoney(self, n: int) -> int:
        div, mod = divmod(n, 7)
        ans = 0
        for i in range(mod):
            ans += i + 1 + div
        ans += div * 28 + (div - 1) * div * 7 // 2 if div else 0
        return ans


# 1725 - Number Of Rectangles That Can Form The Largest Square - EASY
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = pre = 0
        for l, w in rectangles:
            sq = min(l, w)
            if sq > pre:
                count = 1
                pre = sq
            elif sq == pre:
                count += 1
        return count


# 1748 - Sum of Unique Elements - EASY
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = [0] * 100
        for n in nums:
            freq[n - 1] += 1
        ans = 0
        for i in range(len(freq)):
            ans += i + 1 if freq[i] == 1 else 0
        return ans

    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in collections.Counter(nums).items() if v == 1)


# 1762 - Buildings With an Ocean View - MEDIUM
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans, maxH = [], 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxH:
                ans.append(i)
                maxH = heights[i]
        ans.reverse()
        return ans


# 1763 - Longest Nice Substring - EASY
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i + 1 :])
                return max(s0, s1, key=len)
        return s


# 1765 - Map of Highest Peak - MEDIUM
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = collections.deque([])
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                isWater[i][j] -= 1
        while dq:
            x, y = dq.popleft()
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n and isWater[nx][ny] == -1:
                    dq.append((nx, ny))
                    isWater[nx][ny] = isWater[x][y] + 1
        return isWater


# 1768 - Merge Strings Alternately - EASY
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(
            a + b for a, b in itertools.zip_longest(word1, word2, fillvalue="")
        )


# 1770 - Maximum Score from Performing Multiplication Operations - MEDIUM
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        f = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            f[i][0] = f[i - 1][0] + nums[i - 1] * multipliers[i - 1]
        for j in range(1, m + 1):
            f[0][j] = f[0][j - 1] + nums[n - j] * multipliers[j - 1]
        ans = f[0][m] if f[0][m] > f[m][0] else f[m][0]
        # i: 左边拿走数量, j: 右边拿走数量
        for i in range(1, m + 1):
            for j in range(1, m - i + 1):
                left = f[i - 1][j] + nums[i - 1] * multipliers[i + j - 1]
                right = f[i][j - 1] + nums[n - j] * multipliers[i + j - 1]
                f[i][j] = max(left, right)
            ans = max(ans, f[i][m - i])
        return ans

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        # l, r 是左右下标, i 是 mul 里的下标
        f = [[0] * (m + 1) for _ in range(m + 1)]
        for l in range(m - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                r = n - (i - l) - 1
                if r < 0 or r >= n:
                    break
                a = f[l + 1][i + 1] + nums[l] * multipliers[i]
                b = f[l][i + 1] + nums[r] * multipliers[i]
                f[l][i] = max(a, b)
        return f[0][0]

    # cache maxsize is set to None will TLE
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @functools.lru_cache(len(multipliers))
        def dfs(l: int, r: int, k: int) -> int:
            if k == len(multipliers):
                return 0
            a = nums[l] * multipliers[k] + dfs(l + 1, r, k + 1)
            b = nums[r] * multipliers[k] + dfs(l, r - 1, k + 1)
            return max(a, b)
            dfs.cache_clear()

        return dfs(0, len(nums) - 1, 0)


# 1775 - Equal Sum Arrays With Minimum Number of Operations - MEDIUM
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0
        if s1 < s2:
            return self.minOperations(nums2, nums1)
        diff = s1 - s2
        cnt = collections.Counter(v - 1 for v in nums1) + collections.Counter(
            6 - v for v in nums2
        )
        ans = 0
        for k in range(5, 0, -1):
            if diff >= cnt[k] * k:
                diff -= cnt[k] * k
                ans += cnt[k]
            else:
                ans += (diff + k - 1) // k
                diff = 0
                break
        return ans if diff == 0 else -1


# 1779 - Find Nearest Point That Has the Same X or Y Coordinate - EASY
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        mi = float("inf")
        for i, (xx, yy) in enumerate(points):
            if xx == x or yy == y:
                d = abs(xx - x) + abs(yy - y)
                if d < mi:
                    ans = i
                    mi = d
        return ans


# 1784 - Check if Binary String Has at Most One Segment of Ones - EASY
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(list(v for v in s.split("0") if v != "")) <= 1
        return "01" not in s


# 1790 - Check if One String Swap Can Make Strings Equal - EASY
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2)
        if cnt1 != cnt2:
            return False
        diff = 0
        for x, y in zip(s1, s2):
            if x != y:
                diff += 1
        if diff == 0 or diff == 2:
            return True
        return False

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        px = py = ""
        for x, y in zip(s1, s2):
            if x != y:
                if px == "used":
                    return False
                if px == "":
                    px = x
                    py = y
                elif px != y or py != x:
                    return False
                else:
                    px = "used"
        return True if px in "used" else False

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        px = py = ""
        for x, y in zip(s1, s2):
            if x != y:
                if px == y and py == x:
                    px = "used"
                elif px == "":
                    px = x
                    py = y
                else:
                    return False
        return True if px in "used" else False

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = j = -1
        for idx, (x, y) in enumerate(zip(s1, s2)):
            if x != y:
                if i < 0:
                    i = idx
                elif j < 0:
                    j = idx
                else:
                    return False
        return i < 0 or j >= 0 and s1[i] == s2[j] and s1[j] == s2[i]

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        arr = []
        for x, y in zip(s1, s2):
            if x != y:
                arr.append(x)
                arr.append(y)
        return len(arr) <= 4 and arr == arr[::-1]


# 1791 - Find Center of Star Graph - EASY
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        d = [0] * (n + 1)
        for o, i in edges:
            d[o - 1] += 1
            d[i - 1] += 1
        for i in range(len(d)):
            if d[i] == n:
                return i + 1
        return -1

    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
