from mrjob.job import MRJob

class MRSumLength(MRJob):

    def mapper(self, _, line):
        (OBJECTID, route_name, type, Route_Numb, Distributi, Shape_Length, GlobalID) = line.split(',')
        yield route_name, Shape_Length

    def reducer(self, route_name, routes):
        yield route_name, sum(routes)


if __name__ == '__main__':
    MRSumLength.run()
