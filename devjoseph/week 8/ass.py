class Ssorted: 
    def __init__(self):
        
        self.k = None

    #### Bobble sort #################
    def bobblesort(self):
        ff = myownlist
        for i in range (0 , len(myownlist)-1):
            for j in range (0, len(myownlist)-1):
                if ff[j] > ff[j+1]:
                    ff[j], ff[j+1] = ff[j+1], ff[j]
                    
        print (ff)

    

myownlist = [1,10,00,384,5,7,5,4,3,3,3,2,2,] 

mf = Ssorted()
mf.bobblesort()



