class Solution:
    # O(nlgn) using heap
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        mostOccur,maxOccurences = 0, 0
        for task in tasks:
            dic[task] = 1+dic[task] if task in dic else 1
            if dic[task] > maxOccurences:
                mostOccue = task
                maxOccurences = dic[task]

        heap = []

        for k in dic:
            heappush(heap,(-dic[k],k))

        cnt = 0
        while(heap):
            interval = n+1
            tempList = []

            while(interval >0 and heap):
                val,task = heappop(heap)
                tempList.append((val+1,task))
                interval -=1
                cnt+=1

            for val in tempList:
                if val[0] <0:
                    heappush(heap,val)

            if heap:
                cnt+=interval

        return cnt


    # O(n)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        mostOccur,maxOccurences = 0, 0
        for task in tasks:
            dic[task] = 1+dic[task] if task in dic else 1
            if dic[task] > maxOccurences:
                mostOccue = task
                maxOccurences = dic[task]



        return