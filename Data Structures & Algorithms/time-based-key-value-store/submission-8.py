class TimeMap:

    def __init__(self):
        self.people = {} # {'alice': {1: 'happy'}, 'alice': {3: 'sad'}} 

    def set(self, key:str, value: str, timestamp: int) -> None:
        # we want to get the mood out the person, but we want to filter out based on the key
        # this is to create private timelines for each new key 
        if key not in self.people: 
            # self.people[key] = {}
            self.people[key] = []

        self.people[key].append((timestamp,value)) 
        # self.people[key] = {timestamp : value}
        
    def get(self, key:str, timestamp:int) -> str:
        if key not in self.people:
            return ""
    
        timeline = self.people[key]
        print(timeline) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

        l, r = 0, len(timeline)
        if timestamp > timeline[r - 1][0]:
            # if the time is beyond the last item
            return timeline[r - 1][1]

        if timestamp < timeline[l][0]:
            return ""

        while l < r:
            mid = (l + r) // 2
            # print(f"l: {l} r: {r} mid: {mid}")
            # print(f"timestamp: {timestamp} < {timeline[mid][0]}")

            if timestamp < timeline[mid][0]:
                print("1")
                r = mid
            else:
                print("2")
                l = mid + 1

        return timeline[l-1][1]
        

