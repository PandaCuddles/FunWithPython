# Valid python showing that 'self' is just a naming convention

class Boop():
	def __init__(boop):
		boop.bip = "bip"
		boop.bop = "bop"

	def boop(boop):
		print(boop.bip)

	def bopp(bop):
		print(bop.bop)


py_boop = Boop()
py_boop.boop()
py_boop.bopp()
