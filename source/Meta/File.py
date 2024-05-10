from os import remove, listdir

from Meta import Constants as c, GlobalVars as gv


def delete_if_extant(path: str) -> None:
	try: remove(path)
	except FileNotFoundError: pass
	

def check_is_destructive(argv: list[str]) -> None:
	if len(argv) > 1 and argv[1].isnumeric():
		gv.destructive = bool(argv[1])
	print("Program running " + ("non-" if not gv.destructive else "") + "destructively\n")
	
	
def delete_all() -> None:
	for folder in listdir(c.RESOURCES_FP):
		for file in listdir(folder):
			remove(file)
		
