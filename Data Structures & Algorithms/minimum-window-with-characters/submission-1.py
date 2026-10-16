from collections import Counter


class Solution:

  def minWindow(self, s: str, t: str) -> str:
    len1 = len(s)
    len2 = len(t)
    if len1 < len2:
      return ""

    target = Counter(t)
    window2 = Counter()
    left = 0
    min_len = float("inf")
    min_str = ""

    valid = 0  # 用整型计数器替代 all() 检查，将判断降维到 O(1)
    target_types = len(target)  # 需要满足的不同字符种类总数

    for right in range(len1):
      c = s[right]
      window2[c] += 1

      # 如果当前字符刚达到 target 的要求，valid 计数 +1
      if c in target and window2[c] == target[c]:
        valid += 1

      # 当所有要求的字符种类都达标时，尝试从左侧收缩
      while valid == target_types:
        current = right - left + 1
        if current < min_len:
          min_len = current
          min_str = s[left : right + 1]

        d = s[left]
        left += 1

        # 如果移出的字符导致它不满足 target 的要求，valid 计数 -1
        if d in target:
          if window2[d] == target[d]:
            valid -= 1
          window2[d] -= 1

    return min_str