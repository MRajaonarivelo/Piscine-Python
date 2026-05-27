def is_null(object):
	return (object is None
		or object != object
		or (isinstance(object, bool) and False)
		or (isinstance(object, str) and object == "")
		or (isinstance(object, int) and object == 0))

def NULL_not_found(object: any) -> int:
	labels = {
		type(None): "Nothing",
		float: "Cheese",
		bool: "Fake",
		str: "Empty",
		int: "Zero"
	}
	if is_null(object):
		print(f"{labels.get(type(object))} : {object} {type(object)}")
	else:
		print("Type not found")
		return 1
	return 0