class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) #[time, tweet]
        self.followerMap = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append([self.time, tweetId]) #[time, tweet]

    def getNewsFeed(self, userId: int) -> List[int]:

        minHeap = []
        res = []

        self.followerMap[userId].add(userId)
        
        for followeeId in self.followerMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append((time, tweetId, followeeId, index)) #[time, tweetId, followeeId, index]
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:

            time, tweetId, followeeId, index = heapq.heappop(minHeap)

            res.append(tweetId)

            if index > 0:
                index -= 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,(time, tweetId, followeeId, index))


        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        
