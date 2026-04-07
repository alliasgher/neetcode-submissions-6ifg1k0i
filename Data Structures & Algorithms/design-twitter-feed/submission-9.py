class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId] = self.followMap.get(userId, set())
        self.followMap[userId].add(userId)
        minheap = []
        for following in self.followMap[userId]:
            if following in self.tweetMap and len(self.tweetMap[following]) > 0:
                time, tweetId = self.tweetMap[following][-1]
                minheap.append([time, tweetId, following, -2])
        
        heapq.heapify(minheap)
        res = []

        while minheap and len(res) < 10:
            time, tweetId, following, index = heapq.heappop(minheap)
            res.append(tweetId)

            index *= -1
            if len(self.tweetMap[following]) >= index:
                time, tweetId = self.tweetMap[following][-index]
                index *= -1
                heapq.heappush(minheap, [time, tweetId, following, index-1])

        return res






        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap or followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)
        
