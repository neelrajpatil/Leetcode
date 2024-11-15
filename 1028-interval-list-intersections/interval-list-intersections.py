class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        return the intersection of the two lists.
        
        """
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        firstPointer = 0
        secondPointer = 0
        intervals = []

        while firstPointer < len(firstList) and secondPointer < len(secondList):
            firstCurrStart, firstCurrEnd = firstList[firstPointer] # 0 ,4
            secondCurrStart, secondCurrEnd = secondList[secondPointer] # 0, 10
            currIntervalStart = None
            currIntervalEnd = None
            # if first is behind second:
            if firstCurrEnd < secondCurrStart:
                firstPointer += 1
            # if second is behind first:
            elif secondCurrEnd < firstCurrStart:
                secondPointer += 1
            
            # Interval START
            # check if secondStart overlaps with first
            if  firstCurrStart <= secondCurrStart <= firstCurrEnd:
                currIntervalStart = secondCurrStart
            # check if firstStart overlaps with first
            elif secondCurrStart <= firstCurrStart <= secondCurrEnd:
                currIntervalStart = firstCurrStart
            
            # Interval END
            if currIntervalStart is not None:
                if firstCurrEnd < secondCurrEnd:
                    currIntervalEnd = firstCurrEnd
                    firstPointer += 1
                else:
                    currIntervalEnd = secondCurrEnd
                    secondPointer += 1
            
            if currIntervalStart is not None and currIntervalEnd is not None:
                intervals.append([currIntervalStart,currIntervalEnd])

        return intervals