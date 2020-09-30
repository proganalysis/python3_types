# The MIT License
#
# Copyright (c) 2017 Eugene Chekanskiy, echekanskiy@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import collections
from enum import Enum


class RangedCodeEnum(Enum):
  @classmethod
  def from_code(cls, value):
    for enum_item in cls:
      enum_val = enum_item.value
      if isinstance(enum_val, collections.Iterable):
        if len(enum_val) == 1:
          if enum_val[0] == value:
            return enum_item
        elif enum_val[0] <= value <= enum_val[1]:
          return enum_item
      elif enum_val == value:
        return enum_item


def opencls(cls):
  """
  Implements 'open class' pattern for python. Allow to add members for already existing class.
  This example shows how to make Test class with tho methods in tho class definitions::

     class Test(object):
       def method1(self):
         pass


      @opencls(Test)
      class Test(object)
       def method2(self):
         pass

  So, this will results in one Test class that will have methods from both definitions.

  :param cls: class to open
  :return: modified class object
  """
  def update(extension):
    for k, v in extension.__dict__.items():
      if k != '__dict__':
        try:
          setattr(cls, k, v)
        except AttributeError as e:
          if "attribute is read-only" in str(e):
            pass
          else:
            raise
    return cls

  return update
