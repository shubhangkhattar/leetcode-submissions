class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(set)
        self.users = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].add((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        followee_set = self.users[userId]
        followee_set.add(userId)

        for followee in followee_set:
            for tweet in self.tweets[followee]:
                print(tweet)
                heapq.heappush(heap,tweet)

        tweets = []
        while heap:
            tweets.append(heapq.heappop(heap)[1])
            if len(tweets) == 10:
                return tweets
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.users[followerId].discard(followeeId)
        
