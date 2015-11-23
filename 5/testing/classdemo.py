
class cdemo():
    a=20
    def __init__(self,x=20,a=3):
        """Constructor
        """
        self.x = x # instance variable
        self._p = 20 # private (sort of)
    def inc(self):
        self.x = self.x + 1

        

if __name__=="__main__":
    c = cdemo(10)
    d = cdemo(20)
    c.inc()
    d.inc()
    print c.x
    print d.x
    c.x=150
    print c.x
    


    
