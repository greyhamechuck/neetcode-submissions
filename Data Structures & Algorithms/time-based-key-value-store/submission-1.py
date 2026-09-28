class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        combo = self.store[key]
        l=0
        r=len(combo)-1
        result = ""
        while l<=r:
            mid = (l+r)//2
            if combo[mid][0]<= timestamp:
                result = combo[mid][1]
                l=mid+1
            else:
                r = mid-1
        return result