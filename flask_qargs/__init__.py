from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from functools import wraps
from flask import g
from flask_restful import reqparse


def init(*args, **kwargs):
    def decorator(f):
        f._qargs_parser = reqparse.RequestParser(*args, **kwargs)

        @wraps(f)
        def _wrapped(*args, **kwargs):
            parser = f._qargs_parser
            for t in getattr(f, '_qargs_arguments', []):
                parser.add_argument(*t[0], **t[1])

            g.qargs = parser.parse_args()
            return f(*args, **kwargs)

        return _wrapped

    return decorator


def argument(*args, **kwargs):
    def decorator(f):
        f._qargs_arguments = getattr(f, '_qargs_arguments', [])
        f._qargs_arguments.append((args, kwargs))

        return f

    return decorator
