from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        # Your code here

    def reducer(self, word, counts):
        # Your code here


if __name__ == '__main__':
    MRWordFreqCount.run()
