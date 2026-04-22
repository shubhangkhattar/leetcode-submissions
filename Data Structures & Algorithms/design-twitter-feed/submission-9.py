class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        for user in set(self.followers[userId] + [userId]):
            for tweet in self.tweets[user]:
                heapq.heappush(result,tweet)
                if len(result) > 10:
                    heapq.heappop(result)
        
        return [tweetId for _, tweetId in sorted(result, reverse=True)]

    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



