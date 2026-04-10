class Twitter:
    
    def __init__(self):
        self.ID=0
        self.user= {}
        self.tweet={}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ID+=1
        if userId not in self.tweet:
            self.tweet[userId]=set()
        if userId not in self.user:
            self.user[userId]=set()
        self.tweet[userId].add((-self.ID,tweetId))    
        
    
    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.user:
            return []
        h=[]
        self.user[userId].add(userId)
        for follower in self.user[userId]:
            if follower in self.tweet and len(self.tweet[follower]):
                for tweet in self.tweet[follower]:
                    h.append(tweet)

        heapq.heapify(h)
        feed=[]
        while len(feed)<10 and h:
            feed.append(heapq.heappop(h)[1])    
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user:
            self.user[followerId]=set()
        self.user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user:
            if followeeId in self.user[followerId]:
                self.user[followerId].remove(followeeId)    
