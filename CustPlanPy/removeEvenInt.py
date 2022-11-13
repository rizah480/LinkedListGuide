class RemoveEvenInt:

    def removeEInt(self,a:list) -> list:
        for i in a:
            if i % 2 == 0:
                a.remove(i)
                print("Value removed form list!")
        return a
        

