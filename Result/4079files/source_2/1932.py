'''test_result_py.py
Tests for the Result type (yes it's a monad).
'''

import unittest

from result_py import try_, Err, Ok


class TestResultType(unittest.TestCase):
    '''Tests to ensure the Result type provides adequate means of assisting with error handling.'''

    def test_ok_constructor(self):
        '''Ensure that the Ok constructor produces a Result that unwraps to the value we expect.'''

        test_values = [
            32,
            3.141592653589,
            'Hello, world!',
            lambda x: x * x,
            [1, 2, 3],
            range(4),
            {'hello': 'world'}
        ]
        for test_value in test_values:
            wrapped = Ok(test_value)
            self.assertEqual(wrapped.ok(), test_value)


    def test_err_constructor(self):
        '''Ensure that the Err constructor produces a Result that unwraps to the error we expect.'''

        class VarianceError(TypeError):
            '''Just for testing equality on subclasses of an Exception.'''

            def __init__(self, *args, **kwargs):
                TypeError.__init__(self, *args, **kwargs)


        errors = [
            TypeError('T != E'),
            ValueError('Value error'),
            VarianceError('Type T is not covariant with type U')
        ]
        for error in errors:
            wrapped = Err(error)
            self.assertEqual(wrapped.err(), error)


    def test_try_combinator(self):
        '''Ensure that we can wrap functions that raise exceptions using `try_` in order to get a Result instead.'''

        def raise_exception():
            raise RuntimeError('something went wrong')

        def safe_computation():
            return 42

        fail_case = try_(raise_exception)().map(lambda n: n * 10)
        pass_case = try_(safe_computation)().map(lambda n: n * 10)

        self.assertTrue(fail_case.is_err())
        self.assertTrue(isinstance(fail_case.err(), RuntimeError))

        self.assertTrue(pass_case.is_ok())
        self.assertEqual(pass_case.ok(), 420)


    def test_context_management(self):
        '''Ensure that Result proxies context management to underlying values so we can use it in `with` blocks.'''

        import os
        import random

        filename = ''.join(chr(ac) for ac in [random.randint(ord('a'), ord('z')) for _ in range(16)]) + '.txt'
        with try_(open)(filename, 'w') as out:
            self.assertTrue(out.is_ok())
            out.map(lambda writer: writer.write('hello!'))
        self.assertTrue(out.ok().closed)
        with open(filename) as _in:
            self.assertEqual(_in.read(), 'hello!')
        os.remove(filename)

        with Err(RuntimeError('should bind Err result')) as bound:
            self.assertTrue(bound.is_err())
            self.assertTrue(isinstance(bound.err(), RuntimeError))


    def test_is_ok(self):
        '''Ensures that Result.is_ok don't tell us no lies.'''

        wrapped1 = Ok('should be ok')
        self.assertTrue(wrapped1.is_ok())

        wrapped2 = Err('should not be ok')
        self.assertFalse(wrapped2.is_ok())


    def test_is_err(self):
        '''Ensure that Result.is_err don't tell us no lies.'''

        wrapped1 = Err('should be err')
        self.assertTrue(wrapped1.is_err())

        wrapped2 = Ok('should not be err')
        self.assertFalse(wrapped2.is_err())

    # NOTE
    #
    # Tests for Result.ok and Result.err are unnecessary, since test_ok_constructor and test_err_constructor
    # cover the cases we're interested in for the aforementioned methods.

    def test_map(self):
        '''Ensure that Result.map applies expected transformations only over Ok values.'''

        value1 = Ok(32).map(lambda n: n * 2)
        self.assertEqual(value1.ok(), 64)

        value2 = Err(TypeError('Bad types, dude.')).map(lambda n: n * 2)
        self.assertTrue(value2.is_err())
        self.assertFalse(isinstance(value2.err(), int))


    def test_map_err(self):
        '''Ensure that Result.map_err applies expected transformations only over Err values.'''

        class VarianceError(TypeError):
            '''Used to test transformations from one error type to another.'''

            def __init__(self, cause, *args, **kwargs):
                self.cause = cause
                TypeError.__init__(self, *args, **kwargs)


        value = Err(TypeError('Bad types but not sure why'))
        value1 = value.map_err(lambda err: VarianceError(err, 'T is not covariant with U'))
        self.assertTrue(isinstance(value1.err(), VarianceError))
        self.assertTrue(isinstance(value1.err().cause, TypeError))

        val = Ok(101)
        value2 = val.map_err(lambda err: VarianceError(err, 'Error message'))
        self.assertFalse(value2.is_err())
        self.assertEqual(val.ok(), 101)


    def test_and_then(self):
        '''Ensure that Result.and_then applies expected transformations only over Ok values.'''

        value1 = Ok(32).and_then(lambda n: Ok(n * 2))
        self.assertEqual(value1.ok(), 64)

        value2 = Ok(101).and_then(lambda n: Err(TypeError('Expected a string.')))
        self.assertTrue(value2.is_err())
        self.assertTrue(isinstance(value2.err(), TypeError))

        value3 = Err(TypeError('Expected a string.')).and_then(lambda n: Ok(n * 2))
        self.assertFalse(value3.is_ok())
        self.assertTrue(isinstance(value3.err(), TypeError))


    def test_or_else(self):
        '''Ensure that Result.or_else applies expected transformations only over Err values.'''

        class VarianceError(TypeError):
            '''Used to test transformations from one error type to another.'''

            def __init__(self, cause, *args, **kwargs):
                self.cause = cause
                TypeError.__init__(self, *args, **kwargs)


        value1 = Err(TypeError('Bad types')).or_else(lambda err: Err(VarianceError(err, 'Variance error')))
        self.assertTrue(value1.is_err())
        self.assertTrue(isinstance(value1.err(), VarianceError))

        value2 = Err(TypeError('Bad types')).or_else(lambda err: Ok('Nevermind'))
        self.assertFalse(value2.is_err())
        self.assertEqual(value2.ok(), 'Nevermind')

        value3 = Ok(101).or_else(lambda err: Err(VarianceError(err, 'Impossible')))
        self.assertFalse(value3.is_err())
        self.assertEqual(value3.ok(), 101)


    def test_conjuct(self):
        '''Ensures that Result.conjunct produces the conjunction of two results.'''

        value1 = Ok(32).conjunct(Ok(101))
        self.assertTrue(value1.is_ok())
        self.assertEqual(value1.ok(), 101)

        value2 = Ok('Hello').conjunct(Err(TypeError('Bad types')))
        self.assertTrue(value2.is_err())
        self.assertTrue(isinstance(value2.err(), TypeError))

        value3 = Err(TypeError('Bad types')).conjunct(Ok('Test'))
        self.assertFalse(value3.is_ok())
        self.assertTrue(isinstance(value3.err(), TypeError))

        value4 = Err(TypeError('Bad types')).conjunct(Err(ValueError('Bad values')))
        self.assertTrue(isinstance(value4.err(), TypeError))


    def test_disjunct(self):
        '''Ensure that Result.disjunct produces the disjunction of two results.'''

        value1 = Ok(32).disjunct(Ok(101))
        self.assertTrue(value1.is_ok())
        self.assertEqual(value1.ok(), 32)

        value2 = Ok(101).disjunct(Err(TypeError('Bad types')))
        self.assertFalse(value2.is_err())
        self.assertEqual(value2.ok(), 101)

        value3 = Err(TypeError('Bad types')).disjunct(Ok(32))
        self.assertFalse(value3.is_err())
        self.assertEqual(value3.ok(), 32)

        value4 = Err(TypeError('Bad types')).disjunct(Err(ValueError('Bad value')))
        self.assertTrue(isinstance(value4.err(), ValueError))

if  __name__ == '__main__':
    unittest.main()
