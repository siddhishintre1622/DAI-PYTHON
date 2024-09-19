class Musicalinstruments :
    is_tuned = True
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def play(self):
        print("Instrument palying")

    def tune(self):
        if Musicalinstruments.is_tuned == True:
            print("Instrument is tuned")
        else:
            print("Instrument is not tuned")

    def check_tuning(self):
        print(Musicalinstruments.is_tuned)

    def get_vals(self):
        print(self.name , self.type)
        
    def set_vals(self,a,b):
        self.name = a 
        self.type = b


class Guitar(Musicalinstruments):
    def __init__(self,nos):
        self.nos = nos
    
    def play(self):
        print("Guitar palying")
    

class Piano(Musicalinstruments):
    def __init__(self,nok):
        self.nok = nok 
    
    def play(self):
        print("Piano palying")

class Drum(Musicalinstruments):
    def __init__(self,ds):
        self.ds = ds

    def play(self):
        print("Drum palying")



g = Guitar(10)
p = Piano(5)
d = Drum(50)

g.tune()
p.tune()
d.tune()


       
    





