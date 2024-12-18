class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        returns k closest points from origin


        Test Cases:
            points = [[1,3],[-2,2]], k = 1 -> [[-2,2]]
        """

        # Approach 1: min_heap. Store all N points in heap Time O(n) Space O(n)

        heap = []
        # Calc euc distance for all points and push to heap
        for pt in points:
            proxy_dist = pt[0] ** 2 + pt[1]**2 # not taking the sqrt to keep it simple
            heapq.heappush(heap,[proxy_dist, pt[0],pt[1]])


        # Pop k points from the heap
        return [heapq.heappop(heap)[1:] for i in range(k)]


        # # Approac 2: max_heap. Only store k points in heap. Time O(n) Space O(k)

        # # store all distances in array
        # max_heap = []
        # for pt in points:
        #     dist = -(pt[0]**2+pt[1]**2) # keeping negative since we are using a default min_heap to store a max_heap. Also not doing sqrt since we will get the same answer anyways
            
        #     if len(max_heap) < k:
        #         heapq.heappush(max_heap, [dist,pt[0],pt[1]])
        #     else:
        #         if max_heap[0][0] < dist:
        #             heapq.heappop(max_heap)
        #             heapq.heappush(max_heap, [dist,pt[0],pt[1]])
            
        #     # heapq.heapify(max_heap)

        # # return everything from array
        # return [node[1:] for node in max_heap]















        # """
        # return the k points closest to 0,0

        # [[1,3],[-2,2]] k=1 ->  [[-2,-2]]
        # """
        # if k == len(points):
        #     return points

        # # Approach 1: Time O(n*k) Space O(k) Can make time O(n*logk) if we sort.

        # res = [] #[[x,y,distance]] # [[-2,10,10.something,],[-4,-8,8.9,],[10,7,12.2]]

        # # [[-2,10],[-4,-8],[10,7],[-4,-7]] k = 3

        # # iterare thru points, comparing and creating res on the way
        # for pt in points: # [-4,-7]
        #     dist = math.sqrt(pt[0]*pt[0] + pt[1]*pt[1]) # 8.0
        #     if len(res) < k:
        #         res.append([pt[0],pt[1],dist])
        #     else:
        #         for r in res: #[-2,10,10.]
        #             if r[2] > dist:
        #                 r[0] = pt[0]
        #                 r[1] = pt[1]
        #                 r[2] = dist
        #                 break
        # final_res = []
        # for r in res:
        #     final_res.append([r[0],r[1]])
        # return final_res
            


        # # remove distance from res

