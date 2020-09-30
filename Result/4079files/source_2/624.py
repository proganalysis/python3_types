# -*- coding: utf-8 -*-
"""**Copyright 2017 Stephen Rigden.**
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from typing import Any


class Payee:
    """Payee.
    
    This class has been created for v1.0 with minimum functionality with the intention of 
    providing a foundation for extension in later versions. (Such as aliases and where used.)
    """
    # pigjar-#320 Extend Payee functionality
    def __init__(self, name) -> None:
        """ Args:
            name: Name of supplier
        """
        self.name: str = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "{}({})".format(self.__class__.__name__, self.name)

    def __eq__(self, other: Any) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.__dict__ == other.__dict__

    @classmethod
    def from_json(cls, *args: Any, **namespace: dict) -> 'Payee':
        """Alternative constructor for json loads decoder.

        Args:
            *args:
            **namespace: Namespace of new payee.
        """
        obj = cls(args)
        obj.__dict__ = namespace
        return obj

    def json_encode(self) -> dict:
        """Create a json serialized string that can recreate self.

        Returns:
            dict: A dictionary with the keys __class__, __id__, __args__,
            and __kw__.
            '__class__' is a tag used to identify this class.
            '__id__' is used to memoize decoded objects.
            '__args__' is a list of positional arguments.
            '__kw__' can be used for keyword arguments.
            The presence of the four keys is used by the json decoder
            to identify the need for a custom handler that will be used to
            recreate this object.
        """
        return dict(__class__='payee.Payee',
                    __id__=id(self),
                    __args__=self.name,
                    __kw__=self.__dict__)
