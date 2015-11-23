


if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)

class cdemo():
    def __init__(self,x=20):
        self.x = 20
    def inc(self):
        # _p would be considered private
        # we're also creating it as an instance variable
        # in this method
        self._p = 20
        self.x = self.x + 1
