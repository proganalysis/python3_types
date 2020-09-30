"""Query string parameter validation using webargs.

"""

import typing
from enum import Enum

from webargs.fields import (Date, Str, Int, DelimitedList, Bool)
from webargs.flaskparser import use_args

EVERY_ENDPOINT_ARGS = {
    'mock': Bool(missing=False)
}
"""dict: arguments (and their corresponding schemas) which
all endpoints must have.
"""

GET_COLLECTION_ARGS = {
    'from': Int(validate=lambda n: n >= 0),
    'size': Int(validate=lambda n: 1 <= n <= 100, missing=25),
    'order': DelimitedList(
        Str(),
        # FIXME: this is actually not standard REST API ordering
        validate=lambda l: len(l) == 2 and l[1] in ['asc', 'desc'],
    ),
}
"""dict: arguments (and their schemas) which all collection resource
HTTP GET methods must have.
"""

GET_SINGLETON_ARGS = {
    'normalize': Bool(missing=False),
}
"""dict: arguments (and their schemas) which all singleton resource
HTTP GET methods must have.
"""

ALL_ARGS = {
    'usaState': Str(),  # FIXME: Str of len 2
    'findWorks': Str(),
    'findPersons': Str(),
    'findSchools': Str(),
    'findCountries': Str(),
    'findFields': Str(),
    'findPublishers': Str(),
    'fullTextSearch': Str(),
    'publishedYearStart': Date(),
    'publishedYearEnd': Date(),
    'classYearStart': Date(),
    'classYearEnd': Date(),
    'persons': DelimitedList(Int(validate=lambda n: n >= 0)),
    'schools': DelimitedList(Int(validate=lambda n: n >= 0)),
    'fields': DelimitedList(Int(validate=lambda n: n >= 0)),
    'works': DelimitedList(Int(validate=lambda n: n >= 0)),
    'countries': DelimitedList(Int(validate=lambda n: n >= 0)),
    'publisher': Int(validate=lambda n: n >= 0),
    'field': Int(validate=lambda n: n >= 0),
    'school': Int(validate=lambda n: n >= 0),
    'country': Int(validate=lambda n: n >= 0),
    **EVERY_ENDPOINT_ARGS,
    **GET_COLLECTION_ARGS,
    **GET_SINGLETON_ARGS,
}
"""dict: Names and schemas of every shared argument used
by endpoints.
"""


class NotStandardArg(Exception):
    """Bad standard argument name.

    There is no such standard arg by the name `%s`.
    These fields are defined in the use_standard_args()
    decorator. This error is probably because of a typo
    you made while defining standard fields to use, or
    the field has not yet been added as a standard field.

    """

    def __init__(self, key: str):
        super().__init__(self.__doc__ % key)


# FIXME: just :doc: link to the Consistency Guide
# section in sphinx via these docs
def use_standard_args(*args,
                      locations: typing.Tuple[str, ...] = ('querystring',),
                      get_collection: bool = False,
                      get_singleton: bool = True,
                      webargs_schema: dict = None):
    """A decorator using @webargs.use_args, but you only need to
    define the argument name (because the schemas are standardized
    in this module).

    The standard arguments and their schemas are defined as
    constants in this module. They are also defined in this
    project's Sphinx docs.

    This ensures each web argument name has a consistent schema and
    name across all endpoints. Additionally, schemas/names are easier to
    update (needing to only update in one spot). Consistent argument
    names and their consistent schemas make the API more intuitive.
    This also prevents typos when defining the same argument name again.

    Arguments:
        *args (list[str]): ...
        locations (tuple[str]): ...
        get_collection (bool): If True add all the standard args for
            a collection GET request.
        get_singleton (bool): If True add all the standard args for
            a singleton GET request.
        webargs_schema: arg name (key), arg schema (value), just like
            webargs.use_args. In case you're defining a unique
            arg that isn't shared anywhere else.

    Warning:
        `get_collection` and `get_singleton` shouldn't BOTH be True!

    Note:
        Automatically includes the `mock` parameter.

    """

    try:
        marshmallow_schema = {arg: ALL_ARGS[arg] for arg in args}
    except KeyError as error:
        raise NotStandardArg(error)

    if get_collection:
        marshmallow_schema.update(GET_COLLECTION_ARGS)
    elif get_singleton:
        marshmallow_schema.update(GET_SINGLETON_ARGS)

    if webargs_schema:
        marshmallow_schema.update(webargs_schema)

    marshmallow_schema.update(EVERY_ENDPOINT_ARGS)
    return use_args(marshmallow_schema, locations=locations)
