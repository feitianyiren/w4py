#!/usr/bin/env python

import sys
import time
from glob import glob
try:
    from cProfile import Profile
except ImportError:
    from profile import Profile

import FixPath
from MiscUtils.CSVParser import CSVParser


class BenchCSVParser(object):

    def __init__(self, profile=0, runTestSuite=1):
        self.parse = CSVParser().parse
        self._shouldProfile = profile
        self._shouldRunTestSuite = runTestSuite
        self._iters = 100

    def main(self):
        if len(sys.argv) > 1 and sys.argv[1].lower().startswith('prof'):
            self._shouldProfile = True
        if self._shouldRunTestSuite:
            from TestCSVParser import main
            main()
        start = time.time()
        if self._shouldProfile:
            prof = Profile()
            prof.runcall(self._main)
            filename = '%s.pstats' % self.__class__.__name__
            prof.dump_stats(filename)
            print 'Wrote', filename
        else:
            self._main()
        duration = time.time() - start
        print '%.1f secs' % duration

    def _main(self):
        print
        for name in glob('Sample*.csv'):
            print "Benchmark using", name, "..."
            self.benchFileNamed(name)

    def benchFileNamed(self, name):
        lines = open(name).readlines()
        for line in lines:
            for n in xrange(self._iters):
                # we duplicate lines to reduce the overhead of the loop
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)
                self.parse(line)


if __name__ == '__main__':
    BenchCSVParser().main()
