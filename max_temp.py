from mrjob.job import MRJob

class TEST(MRJob):

    def mapper(self, _, line):
        (location, date, type, Route_Numb, x, y, z) = line.split(',')
        if (type == 'MTA Commuter Bus' or type == 'MTA Local Bus - Express BusLink'):
            quest = float(y)
            yield location, quest

    def reducer(self, location, temps):
        yield location, max(temps)


if __name__ == '__main__':
    MRMaxTemperature.run()
