class TestResults:
    def __init__(self,tag):
        self.tag = tag
        self.contents = {}

    def add_category(self,tag):
        if not tag in self.contents:
            self.contents[tag] = ResultsCategory(tag)

    def add_result(self,tag,parents,ratio,value):
        self.add_category(tag)
        self.contents[tag].add_result(parents,ratio,value)

    def get_tagged(self,tag):
        return self.contents[tag]

    def get_result(self,tag,parents,ratio):
        return self.get_tagged(tag).get_result(parents,ratio)

    def has_result(self,tag,parents,ratio):
        return self.get_result(tag,parents,ratio) != None

class ResultsCategory:
    def __init__(self,tag):
        self.tag = tag
        self.parents_extremes = [0,0]
        self.ratios_extremes = [0,0]
        self.parents_range = None
        self.ratios_range = None
        self.contents = []

    def add_result(self,parents,ratio,value):
        # remove result and replace it if it was already calculated
        prev = self.get_result_raw(parents,ratio)
        if prev != None:
            self.contents.remove(prev)

        self.contents.append(ResultEntry(parents, ratio, value))
        self.update_ranges()

    def get_result(self,parents,ratio):
        for c in self.contents:
            # if c.ra
            if equal(c.parents, parents) and equal(c.ratio, ratio):
                return c.value
        return None

    def get_result_raw(self,parents,ratio):
        for c in self.contents:
            if equal(c.parents, parents) and equal(c.ratio, ratio):
                return c
        return None        

    def update_ranges(self):
        pass

# could be lists
def equal(r1,r2):
    if isinstance(r1,list) and isinstance(r2,list):
        return all([float(r1[i]) == float(r2[i]) for i in range(len(r1))])
    elif isinstance(r1,list) or isinstance(r2,list):
        return False
    else:
        return r1 == r2

class ResultEntry:
    def __init__(self,parents,ratio,value):
        self.parents = parents
        self.ratio = ratio
        self.value = value