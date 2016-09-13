"""
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user and is able to see the 10 most recent 
tweets in the user's news feed. Your design should support the 
following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the 
user's news feed. Each item in the news feed must be posted by users 
who the user followed or by the user herself. Tweets must be ordered 
from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Global timestamp
        self.timestamp = 1  
        # Users table
        self.user_data = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_data:         
            # Each userId has a tweets list (10 items at most) and
            # a set of followees (include itself)
            self.user_data[userId] = collections.deque(), {userId} 
    
        # Discard outdated tweet    
        if len(self.user_data[userId][0]) == 10:
            self.user_data[userId][0].pop()
        
        self.user_data[userId][0].appendleft((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user 
        followed or by the user herself. Tweets must be ordered from 
        most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # Use a heap to store all tweets from followees and pick the 10 most recent ones
        if userId not in self.user_data:
            return []
        
        heap = []
        for uid in self.user_data[userId][1]:
            if uid in self.user_data:
                for tweet in self.user_data[uid][0]:
                    heapq.heappush(heap, tweet)
                
        res = []
        while len(res) < 10 and heap:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, 
        it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.user_data:
            self.user_data[followerId] = collections.deque(), {followerId} 
        
        self.user_data[followerId][1].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, 
        it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.user_data:
            return
    
        if followerId != followeeId:
            self.user_data[followerId][1].discard(followeeId)
