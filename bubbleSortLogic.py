OFSSET_BETWEEN_TIMAG_IMAGES = 25
class BubbleSortLogic:
    def __init__(self):
        self.tImgArr = []
    def inithilizeTimagesPos(self,userNumbers,index,tImg):
        # Calculate the initial position based on the length of userNumbers
        initial_offset = len(userNumbers) // 2 * 85
        startPosx = - initial_offset
        tImg.setpos(x=startPosx, y=0)
        if index != 0:
            # psitioning calculations
            lastx = self.tImgArr[index-1].xcor()
            lastoffset = self.tImgArr[index-1].getImgWidth() / 2
            newoffset = self.tImgArr[index].getImgWidth() / 2 + OFSSET_BETWEEN_TIMAG_IMAGES
            startPosx = lastx + lastoffset + newoffset
        tImg.setx(startPosx)
    def setTimagesSpeed(self,speed):
        for t in self.tImgArr:
            t.speed(speed)
    def swapTimages(self,userNumbers):
        for index in range(len(userNumbers)):
            for j in range(0, len(userNumbers)-index-1):
                # Swap if the element found is greater than the next element
                if userNumbers[j] > userNumbers[j+1]:
                    tempXoffset = self.tImgArr[j].getImgWidth() + OFSSET_BETWEEN_TIMAG_IMAGES
                    self.tImgArr[j].forward(self.tImgArr[j+1].getImgWidth() + OFSSET_BETWEEN_TIMAG_IMAGES)
                    self.tImgArr[j+1].backward(tempXoffset)
                    userNumbers[j], userNumbers[j+1] = userNumbers[j+1], userNumbers[j]
                    self.tImgArr[j],self.tImgArr[j+1] =  self.tImgArr[j+1],self.tImgArr[j]
    
  



        
