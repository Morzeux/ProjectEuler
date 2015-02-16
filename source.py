'''
Created on 14.5.2014

@author: Morzeux
'''
import importlib, sys
from pylint import epylint as lint
from time import time

class Tester(object):
    """ Evaluates my solutions for Euler Project. """

    lint_out = None
    lint_err = None
    missings = []
    errors = []
    times = []

    RESULTS = {1: 233168,
               2: 4613732,
               3: 6857,
               4: 906609,
               5: 232792560,
               6: 25164150,
               7: 104743,
               8: 40824,
               9: 31875000,
               10: 142913828922,
               11: 70600674,
               12: 76576500,
               13: 5537376230,
               14: 837799,
               15: 137846528820,
               16: 1366,
               17: 21124,
               18: 1074,
               19: 171,
               20: 648,
               21: 31626,
               22: 871198282,
               23: 4179871,
               24: '2783915460',
               25: 4782,
               26: 983,
               27: -59231,
               28: 669171001,
               29: 9183,
               30: 443839,
               31: 73682,
               32: 45228,
               33: 100,
               34: 40730,
               35: 55,
               36: 872187,
               37: 748317,
               38: 932718654,
               39: 840,
               40: 210,
               41: 7652413,
               42: 162,
               43: 16695334890,
               44: 5482660,
               45: 1533776805,
               46: 5777,
               47: 134043,
               48: 9110846700,
               49: 296962999629,
               50: 997651,
               51: 121313,
               52: 142857,
               53: 4075,
               54: 376,
               55: 249,
               56: 972,
               57: 153,
               58: 26241,
               59: 107359,
               60: 26033,
               61: 28684,
               62: 127035954683,
               63: 49,
               64: 1322,
               65: 272,
               66: 661,
               67: 7273,
               68: 6531031914842725,
               69: 510510,

               81: 427337,
               82: 260324,
               83: 425185}

    @classmethod
    def print_result(cls):
        """ Prints results of tests. """

        print('')
        if cls.errors or cls.missings or cls.lint_out or cls.lint_err:
            if cls.lint_err:
                print('Pylint errors:\n%s' % cls.lint_err)

            if cls.lint_out:
                print('Pylint issues:\n%s' % cls.lint_out)

            if cls.errors:
                print('Errors in problems:')
                for err in cls.errors:
                    print('\t%s' % err)

            if cls.missings:
                print('These problems were missing:')
                for miss in cls.missings:
                    print('\t%s' % miss)

            print('\nNot all tests passed. Total time %.3fs.' % sum(cls.times))
        else:
            print('All tests passed. Total time %.3fs.' % sum(cls.times))

    @classmethod
    def test(cls, problem, expected_result):
        """ Performs specific test on specific result. """

        name = 'Problem%d' % problem
        print('%s...' % name, end=' ')

        sys.stdout.flush()
        start = time()
        result = cls.call(problem)
        cls.times.append(time() - start)

        try:
            assert result == expected_result
            print('OK - time %.3fs' % cls.times[-1])
            return True
        except AssertionError:
            error = '%d != %d' % (result, expected_result)
            print('FAIL -> %s' % error)
            cls.errors.append('%s -> %s' % (name, error))
            return False

    @classmethod
    def call(cls, number, *args):
        """ Call specific problem and evaluates it. """
        return importlib.import_module('Problems.Problem%d' % number)\
            .problem(*args)

    @classmethod
    def call_test(cls, num):
        """ Checks it test returns expected result. """

        if num in cls.RESULTS:
            cls.test(num, cls.RESULTS[num])
        else:
            cls.missings.append('Problem%d' % num)
            print('Problem%d is missing!' % num)

    @classmethod
    def run_pylint(cls):
        """ Runs pyLint on all modules. """

        print('Pylint...', end=' ')
        sys.stdout.flush()
        start = time()
        buffout, bufferr = lint.py_run('source.py Problems', True)
        cls.lint_out = buffout.read().strip()
        cls.lint_err = bufferr.read().strip()
        buffout.close()
        bufferr.close()
        cls.times.append(time() - start)

        if cls.lint_err == 'No config file found, using default configuration':
            cls.lint_err = ''

        if cls.lint_out == '' and cls.lint_err == '':
            print('OK - time %.3fs' % cls.times[-1])
        else:
            print('FAIL -> Code is not clear:')
            if cls.lint_err != '':
                print(cls.lint_err)
            if cls.lint_out != '':
                print(cls.lint_out)
            print('')

    @classmethod
    def run_tests(cls, min_test=1, max_test=True, pylint=False):
        """ Runs all tests between specified sequences. """
        if max_test is True:
            max_test = max(cls.RESULTS.keys())

        pylint_s = 'with Pylint' if pylint else 'without Pylint'

        print('Running tests %d-%d %s...\n' % (min_test, max_test, pylint_s))
        if pylint:
            cls.run_pylint()

        for i in range(min_test, max_test + 1):
            Tester.call_test(i)
        Tester.print_result()

def main():
    """ Main function to evaluate results. """
    Tester.run_tests(pylint=True)
    #Tester.call_test(66)
    #print(Tester.call(69))

if __name__ == "__main__":
    main()
