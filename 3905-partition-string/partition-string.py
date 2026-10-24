
from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        result = []
        seen = set()
        k = ""

        for ch in s:
            k += ch

            if k not in seen:
                result.append(k)
                seen.add(k)
                k = ""

        return result
