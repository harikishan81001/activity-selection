import sys
import itertools

from csv_reader import FileReader


class Organizer(object):
    """
    Description:
        Organizer which organize based presentaion
        based on given conditions
    """
    def __init__(self, file_path, no_of_hrs):
        _reader = FileReader(file_path)
        self.data = None
        try:
            self.data = _reader.converter()
        except IOError, e:
            print e
        self.booked_hrs = no_of_hrs

    def get_cost(self, comb):
        cost = 0
        for each in comb:
            name = each.split('#')[0]
            cost += self.data[name]['cost']
        return cost

    def get_names(self, comb):
        return [e.split('#')[0] for e in comb]

    def maximum_number_of_presenters(self, hrs):
        self.combs = self.combinations(hrs)
        d = {}
        c_list = []
        for each in self.combs:
            c_list.append(self.get_cost(each))
        if c_list:
            min_cost = min(c_list)
            c_list = []
            for each in self.combs:
                cost = self.get_cost(each)
                if cost == min_cost:
                    d[each] = cost
            #### Printing Data ####
            print "Maximum the number of presenters with lowest cost"
            for k, v in d.items():
                names = self.get_names(k)
                print "{names} ${cost}".format(
                    names=",".join(names), cost=v)
        else:
            print "Not enough presenters"

    def minimum_cost(self, hrs):
        self.combs = []
        for slot in xrange(1, len(hrs)+1):
            self.combs.extend(self.combinations(hrs, slot))
        d = {}
        c_list = []
        for each in self.combs:
            c_list.append(self.get_cost(each))
        if c_list:
            min_cost = min(c_list)
            c_list = []
            for each in self.combs:
                cost = self.get_cost(each)
                if cost == min_cost:
                    d[each] = cost
            # Printing minimum cost ####
            print "Minimum cost with maximum number of presenters"
            key = ()
            for k in d.keys():
                if len(k) >  len(key):
                    key = k
            if key:
                names = self.get_names(k)
                cost = d[key]
                print "{name} ${cost}".format(name=",".join(names), cost=cost)
            else:
                print "Not enough presenters"

    def calculate(self):
        if not self.data:
            return
        hrs = [k + "#" + str(v["hrs"]) for k, v in self.data.items()]
        self.maximum_number_of_presenters(hrs)
        self.minimum_cost(hrs)

    def combinations(self, list_of_hours, slots=3):
        c = []
        for comb in itertools.combinations(list_of_hours, slots):
            total_hrs = [int(e.split('#')[-1]) for e in comb]
            if sum(total_hrs) == self.booked_hrs:
                c.append(comb)
        return c


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        file_path = sys.argv[1]
        no_of_hrs = sys.argv[2]
        no_of_hrs = int(no_of_hrs)
        calculator = Organizer(file_path, no_of_hrs)
        calculator.calculate()
    else:
        print "Invalid number of arguments provides"
