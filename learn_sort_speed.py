import time

class myMain:
    def __init__(self):
        self.name_set = set()
        self.name_list = list()
        self.name_dict = dict()
        self.good_list = ('michael', 'mike', 'paul', 'moni', 'julie', 'greg', 'hannah', 'hanna', 'leroy', 'calli', 'eddie')
        self.bad_list = ('michaelx', 'mikex', 'paulx', 'monix', 'juliex', 'gregx', 'hannahx', 'hannax', 'leroyx', 'callix', 'eddiex')
        with open('names.txt', 'r') as db:
            for line in db.readlines():
                self.name_set.add(line.lower().rstrip()) 
                self.name_list.append(line.lower().rstrip())
                self.name_dict[line.lower().rstrip()] = 1

    def bsearch(self, val):
        # binary search of values list
        first = 0
        last = len(self.name_list)-1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first+last)//2
            if self.name_list[mid] == val:
                index = mid
            else:
                if val<self.name_list[mid]:
                    last = mid -1
                else:
                    first = mid +1
        return(index)
    
    def run_test(self, search_type, good_bad, endrange):
        list = self.good_list if good_bad == "good" else self.bad_list
        if good_bad == "good":
            print(f"\n{search_type} search speed: average {endrange}x")
        start = time.process_time()
        for t1 in range(1,endrange):
            for n1 in list:
                match search_type:
                    case "bsearch": isFound = True if self.bsearch(n1) > -1 else False
                    case    "dict": isFound = True if n1 in self.name_dict else False
                    case    "list": isFound = True if n1 in self.name_list else False
                    case     "set": isFound = True if n1 in self.name_set else False
        end = time.process_time()
        msec = round(((end-start)*1000)/endrange,4)
        print(f"    {good_bad} list: " + str(msec))

    def test_speed(self):
        endrange =  5000        # use to repeat search aka add a delay since it is fast

        # test set speed
        self.run_test("set", "good", endrange)
        self.run_test("set", " bad", endrange)

        # test dict sort speed
        self.run_test("dict", "good", endrange)
        self.run_test("dict", " bad", endrange)

        # test binary sort speed
        self.run_test("bsearch", "good", endrange)
        self.run_test("bsearch", " bad", endrange)

        # test list speed
        self.run_test("list", "good", endrange)
        self.run_test("list", " bad", endrange)

        print()

    def run(self):
        self.test_speed()
        exit(0)

########## MAIN ##########

# Script will compare the speed of lookup for a set, list and custom binary search

if __name__ == '__main__':
    g_main = myMain()
    g_main.run()
