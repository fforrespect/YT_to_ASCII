from os import remove


def delete_if_extant(path: str) -> None:
	try: remove(path)
	except FileNotFoundError: pass
	