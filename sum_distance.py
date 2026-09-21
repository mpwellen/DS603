from mrjob.job import MRJob

class CALCULATE_SUM(MRJob):

    def mapper(self, _, line):
        (location, date, type, Route_Numb, distributi, dist, z) = line.split(',')
        if (type != 'Route_Type'):
            quest = float(dist)
            yield date, quest

    def reducer(self, date, distances):
        yield date, sum(distances)


if __name__ == '__main__':
    CALCULATE_SUM.run()
