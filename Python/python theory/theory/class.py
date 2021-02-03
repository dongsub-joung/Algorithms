class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second =second
    
    def addData(self):
        return self.first +self.second
cal = FourCal()
cal.setdata(1,3)
result = cal.addData()
print(result)