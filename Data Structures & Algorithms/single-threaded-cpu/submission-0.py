class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        myTask = [] #enque,processingtime,index

        for i,task in enumerate(tasks):
            myTask.append((task[0],task[1],i))
        myTask.sort() 
        
        time,i = 0,0
        minHeap,res = [],[]

        while minHeap or i < len(myTask):
            
            while i < len(myTask) and time >= myTask[i][0]:
                processingtime,index = myTask[i][1], myTask[i][2]
                heapq.heappush(minHeap,(processingtime,index))
                i += 1



            if not minHeap:
                time = myTask[i][0]
            else:
                processingtime,index = heapq.heappop(minHeap)
                time += processingtime
                res.append(index)
    
        return res
            


