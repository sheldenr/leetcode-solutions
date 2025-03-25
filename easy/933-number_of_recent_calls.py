class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        self.req.append(t)

        lower, upper = 0, 0
        count = 0

        if len(self.req) < 3:
            lower = -3000 + self.req[-1]
        else:
            for ping in self.req:
                if self.req[-1] - ping <= 3000:
                    lower = self.req[-1] - 3000

        for ping in self.req:
            if ping >= lower and ping <= self.req[-1]:
                count += 1

        return count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)




# Bad solution, time limit exceed, something to do with queues but idk the properly implementation
