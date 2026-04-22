class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        followee_set = self.users[userId]
        followee_set.add(userId)

        for followee in followee_set:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count, tweet = self.tweets[followee][index]
                heapq.heappush(heap,[count,tweet,followee,index-1])

        heapq.heapify(heap)
        tweets = []
        while heap and len(tweets) < 10:
            count,tweet,followee,index = heapq.heappop(heap)
            tweets.append(tweet)

            if index >= 0:
                count,tweet = self.tweets[followee][index]
                heapq.heappush(heap,[count,tweet,followee,index-1])
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.users[followerId].discard(followeeId)
        
