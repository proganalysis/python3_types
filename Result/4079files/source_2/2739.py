'''result_py/__init__.py
Error types used to encode error handling into our type system and error-handling code.
'''

from contextlib import AbstractContextManager
import enum
from typing import Generic, Optional, TypeVar


# !!! NOTE !!!
#
# You'll notice that the type signatures of Result's methods have been commented out.
# The reason for this is because Python does not yet have support for representing
# the type of a generic class before said class is defined. As a result, methods
# cannot refer to their class type in arguments or return values.
#
# See:
# [0] https://github.com/python/mypy/issues/1212
# [1] https://github.com/python/mypy/issues/3645
# [2] https://github.com/python/mypy/issues/2354


# The generic 'Ok' value for a Result.
T = TypeVar('T')

# A generic type for transformations from `Ok(T)` to `Ok(U)`.
U = TypeVar('U')

# The generic 'Err' value for a Result.  Must be either `Exception` or a subclass thereof.
E = TypeVar('E', bound=Exception)

# A generic type for transformations from `Err(E)` to `Err(F)`.
F = TypeVar('F', bound=Exception)


class _ResultVariant(enum.Enum):
    '''Enumerates the variants that Result can take.'''

    OK = enum.auto()
    ERR = enum.auto()


class Result(Generic[T, E], AbstractContextManager):
    '''A container for the result of functions that can produce errors.
    Instances should be constructed using either the `Ok` or `Err` functions.
    '''

    def __init__(self, ok: T = None, err: E = None) -> None:
        '''Construct a new result with either an Ok or Err value. Not for use by consumers of this type.'''

        self._variant = _ResultVariant.ERR  # type: _ResultVariant
        self._ok = None  # type: Optional[T]
        self._err = None  # type: Optional[E]

        if err is not None:
            self._err = err
        else:
            self._variant = _ResultVariant.OK
            self._ok = ok


    def __enter__(self):
        '''Proxy any context established by a value contained in an Ok variant through this Result.'''

        if self.is_ok():
            return Ok(self._ok.__enter__())

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Proxy any context teardown handled by a value contained in an Ok variant through this Result.'''

        if self.is_ok():
            return self._ok.__exit__(exc_type, exc_val, exc_tb)


    def is_ok(self) -> bool:
        '''Determines whether the Result contains an Ok value.'''

        return self._variant == _ResultVariant.OK


    def is_err(self) -> bool:
        '''Determines whether the Result contains an Err value.'''

        return not self.is_ok()


    def ok(self) -> Optional[T]:
        '''Converts the Result into an Optional[T] containing the Ok value if present, else None.'''

        if self.is_ok():
            return self._ok

        return None


    def err(self) -> Optional[E]:
        '''Converts the Result into an Optional[E] containing the Err value if present, else None.'''

        if self.is_err():
            return self._err

        return None


    # def map(self, f: Callable[[T], U]) -> Result[U, E]:
    def map(self, f):
        '''Map a function over an Ok variant value, leaving an Err untouched.'''

        if self.is_err():
            return Err(self._err)

        return Ok(f(self._ok))


    # def map_err(self, f: Callable[[E], F]) -> Result[T, F]:
    def map_err(self, f):
        '''Map a function over an Err variant's error, leaving an Ok untouched.'''

        if self.is_ok():
            return Ok(self._ok)

        return Err(f(self._err))


    # def and_then(self, f: Callable[[T], Result[U, E]]) -> Result[U, E]:
    def and_then(self, f):
        '''Flat map a function that produces a Result over an Ok variant's value, leaving an Err untouched.'''

        if self.is_err():
            return Err(self._err)

        return f(self._ok)


    # def or_else(self, f: Callable[[E], Result[T, F]]) -> Result[T, F]:
    def or_else(self, f):
        '''Flat map a function that produces a Result over an Err variant's value, leaving an Ok untouched.'''

        if self.is_ok():
            return Ok(self._ok)

        return f(self._err)


    # def conjunct(self, res: Result[U, E]) -> Result[U, E]:
    def conjunct(self, res):
        '''Returns res if the self is an Ok variant, else returns the Err variant of self.'''

        if self.is_err():
            return Err(self._err)

        return res


    # def disjunct(self, res: Result[U, E]) -> Result[U, E]:
    def disjunct(self, res):
        '''returns res if the self is an Err variant, else returns the Ok variant of self.'''

        if self.is_ok():
            return Ok(self._ok)

        return res


def Ok(value: T) -> Result[T, E]:
    '''Construct a new Result of the Ok variant containing some value.'''

    return Result(ok=value)


def Err(error: E) -> Result[T, E]:
    '''Construct a new Result of the Err variant containing some error.'''

    return Result(err=error)


def try_(fn):
    '''Wraps any function that may raise an exception in another function
    that will return an Err containing that exception if it is raised, or
    else simply wrap the successful result in Ok.
    '''

    def closure(*args, **kwargs):
        '''Call the wrapped function.'''

        try:
            return Ok(fn(*args, **kwargs))
        except Exception as ex:
            return Err(ex)

    return closure
