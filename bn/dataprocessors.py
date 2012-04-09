# -*- coding: utf-8 -*-

class ProcReturnAsString(object):
    def __call__(self, value):
        return unicode(value)

class ProcReturnAsInteger(object):
    def __call__(self, value):
        return value.atoi()

