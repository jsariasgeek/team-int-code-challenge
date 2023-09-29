class Stats:
    def __init__(self, total_count) -> None:
        self._counts = {}
        self._total_count = total_count
    
    def less(self, number):
        """
        Returns the number of items in the list that are less than the number passed in.
        """
        return self._counts[number]['less']
    
    def between(self, lowest, highest):
        """
        Returns the number of items in the list that are between the lower and upper bounds passed in.
        """
        return self._total_count - self._counts[lowest]['less'] - self._counts[highest]['greater']
    
    def greater(self, number):
        """
        Returns the number of items in the list that are greater than the number passed in.
        """
        return self._counts[number]['greater']


class DataCapture:

    MAXIMUM_ACCEPTED_VALUE = 1000 # From the Statement

    def __init__(self) -> None:
        self.total_count = 0
        self._counts = {i: 0 for i in range(self.MAXIMUM_ACCEPTED_VALUE)}
        self._input_data = []

    def add(self, number_to_add):
        """
        Adds a number to the internal list.
        """
        # self.stats._counts[number_to_add] += 1
        if number_to_add not in self._counts:
            self._counts[number_to_add] = 0
        self._counts[number_to_add] += 1
        self.total_count += 1

    
    def build_stats(self):
        stats: Stats = Stats(self.total_count)
        less: int = 0
        greater: int = self.total_count
        for number in self._counts:
            if number not in stats._counts.keys():
                stats._counts[number] = {}
            stats._counts[number]['count'] = self._counts[number]
            stats._counts[number]['less'] = less
            less += self._counts[number]
            stats._counts[number]['greater'] = greater - self._counts[number]
            greater -= self._counts[number]
        
        return stats
            

    
