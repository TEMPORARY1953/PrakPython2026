class ObjectsError(Exception):
	pass
class SafeSafeIndexError(Exception):
	pass
def safesafeindex(c, *a):
	try:
		return itemget(c, *a)
	except TypeError as e:
		err = ObjectsError(); err.__context__ = e; err.__cause__ = None
		return err
	except Exception as e:
		err = SafeSafeIndexError(); err.__cause__ = e; err.__suppress_context__ = True
		return err
