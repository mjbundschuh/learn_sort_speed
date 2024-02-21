import time

class myMain:
    def __init__(self):
        self.nameset = set()
        self.namelist = list()
        self.goodlist = ('michael', 'mike', 'paul', 'moni', 'julie', 'greg', 'hannah', 'hanna', 'leroy', 'calli', 'eddie')
        self.badlist = ('michaelx', 'mikex', 'paulx', 'monix', 'juliex', 'gregx', 'hannahx', 'hannax', 'leroyx', 'callix', 'eddiex')
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
    
    def run_test(self, search_type, good_bad, endrange):
        list = self.goodlist if good_bad == "good" else self.badlist
        if good_bad == "good":
            print(f"\n{search_type} search speed: average {endrange}x")
        start = time.process_time()
        for t1 in range(1,endrange):
            for n1 in list:
                match search_type:
                    case "set":
                        isFound = True if n1 in self.nameset else False
                    case "list":
                        isFound = True if n1 in self.namelist else False
                    case "bsearch":
                        isFound = True if self.bsearch(n1) > -1 else False
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"    {good_bad} list: " + str(msec))

    def test_speed(self):
        endrange =  5000        # use to repeat search aka add a delay since it is fast

        # test set speed
        self.run_test("set", "good", endrange)
        self.run_test("set", " bad", endrange)

        # test list speed
        self.run_test("list", "good", endrange)
        self.run_test("list", " bad", endrange)

        # test binary sort speed
        self.run_test("bsearch", "good", endrange)
        self.run_test("bsearch", " bad", endrange)

        print()

    def run(self):
        self.test_speed()
        exit(0)

########## MAIN ##########

# Script will compare the speed of lookup for a set, list and custom binary search

if __name__ == '__main__':
    g_main = myMain()
    g_main.run()
