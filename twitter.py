from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followM = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int):
        minHeap = []
        self.followM[userId].add(userId)
        for usr in self.followM[userId]:
            if self.tweets[usr]:
                t, tId = self.tweets[usr][-1]
                minHeap.append([t, tId, usr, len(self.tweets[usr]) - 2])
        
        heapq.heapify(minHeap)
        res = []
        while minHeap and len(res) < 10:
            t, tId, usr, index = heapq.heappop(minHeap)
            res.append(tId)
            if index >= 0:
                t, tId = self.tweets[usr][index]
                heapq.heappush(minHeap, [t, tId, usr, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followM[followerId]:
            self.followM[followerId].remove(followeeId)