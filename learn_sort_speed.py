import time

class myMain:
    def __init__(self):
        self.nameset = set()
        self.namelist = list()
        with open('names.txt', 'r') as db:
            for line in db.readlines():
                self.nameset.add(line.lower().rstrip()) 
                self.namelist.append(line.lower().rstrip()) 

    def bsearch(self, val):
        # binary search of values list
        first = 0
        last = len(self.namelist)-1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first+last)//2
            if self.namelist[mid] == val:
                index = mid
            else:
                if val<self.namelist[mid]:
                    last = mid -1
                else:
                    first = mid +1
        return(index)

    def test_speed(self):
        goodlist = ('michael', 'mike', 'paul', 'moni', 'julie', 'greg', 'hannah', 'hanna', 'leroy', 'calli', 'eddie')
        badlist = ('michaelx', 'mikex', 'paulx', 'monix', 'juliex', 'gregx', 'hannahx', 'hannax', 'leroyx', 'callix', 'eddiex')
        endrange =  5000

        # test set speed

        print(f"\nSet search speed: average {endrange}x")

        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in goodlist:
                if n in self.nameset:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\tgood list: " + str(msec))

        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in badlist:
                if n in self.nameset:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\t bad list: " + str(msec))

        # test list speed

        print(f"\nList search speed: average {endrange}x")

        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in goodlist:
                if n in self.namelist:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\tgood list: " + str(msec))

        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in badlist:
                if n in self.namelist:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\t bad list: " + str(msec))

        # test binary sort speed

        print(f"\nBinary search speed: average {endrange}x")

        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in goodlist:
                if self.bsearch(n) > -1:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\tgood list: " + str(msec))

        endrange =  1000
        start = time.process_time()
        for t in range(1,endrange):
            g = b = 0
            for n in badlist:
                if self.bsearch(n) > -1:
                    g = g + 1
                else:
                    b = b + 1
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"\t bad list: " + str(msec))

        print()

    def run(self):
        self.test_speed()
        exit(0)

########## MAIN ##########

# Script will compare the speed of lookup for a set, list and custom binary search
        
g_main = myMain()
g_main.run()
