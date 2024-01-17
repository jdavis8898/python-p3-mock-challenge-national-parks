class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 < len(value) and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception
        
    def trips(self):
        
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):

        return list(set(trip.visitor for trip in self.trips())) 
    
    def total_visits(self):

        return len(self.trips())
    
    def best_visitor(self):
        
        best_vis = None
        most_vis = 0

        for visitor in self.visitors():
            new_most = len([trip for trip in self.trips() if trip.visitor == visitor])

            if new_most > most_vis:
                most_visits = new_most
                best_vis = visitor
            
        return best_vis

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if (isinstance(value, str) and 6 < len(value) and
        (value.endswith("st") or value.endswith("nd") or value.endswith("rd") or
        value.endswith("th"))):
            
            self._start_date = value
        
        else:
            raise Exception
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if (isinstance(value, str) and 6 < len(value) and
         (value.endswith("st") or value.endswith("nd") or value.endswith("rd") or
        value.endswith("th"))):
            
            self._end_date = value
        
        else:
            raise Exception
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value
        
        else:
            raise Exception
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        if isinstance(value, NationalPark):
            self._national_park = value
        
        else:
            raise Exception

class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value
        else:
            raise Exception
        
    def trips(self):
        
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        
        return list(set(trip.national_park for trip in self.trips()))
    
    def total_visits_at_park(self, park):
        
        times_visited = 0

        for trip in self.trips():
            if park == trip.national_park:
                times_visited += 1
        
        return times_visited