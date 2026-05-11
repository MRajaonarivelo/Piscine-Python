def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing : None {type(object)}")
	elif object != object:
		print(f"Cheese : nan {type(object)}")
	elif isinstance(object, bool) and not object:
		print(f"Fake : False {type(object)}")
	elif isinstance(object, str) and object == "":
		print(f"Empty : {type(object)}")
	elif isinstance(object, int) and object == 0:
		print(f"Zero : 0 {type(object)}")
	else:
		print("Type not found")
		return 1
	return 0