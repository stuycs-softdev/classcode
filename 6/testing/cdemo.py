
class cdemo():
    
    def __init__(self,x=20):
        """Constructor
        """
        self.x = x # set up an instance variable

    def inc(self):
        
        self._p = 20 # for some reason I'm setting up
                     # a private variable _p here
        self.x = self.x + 1
        

if __name__=="__main__":
    c = cdemo(100)
    c.inc()
    print c.x

    
