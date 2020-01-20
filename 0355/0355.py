class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_followed = collections.defaultdict(list)
        self.user_post = collections.defaultdict(list)
        self.users = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.users.add(userId)
        self.user_post[userId].append((tweetId, self.time))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = []
        for posts in self.user_post[userId]:
            news.append(posts)
        for users in self.user_followed[userId]:
            news += self.user_post[users]
        news.sort(key=lambda x: -x[1])
        res = []
        for i, j in news:
            if i not in set(res):
                res.append(i)
        return res[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_followed[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        following = self.user_followed[followerId]
        if followeeId in following:
            following.remove(followeeId)
        self.user_followed[followerId] = following


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
