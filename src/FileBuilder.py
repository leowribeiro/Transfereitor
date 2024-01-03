


class FileBuilder:

	def __init__(self, file_name):
		self.fileName = file_name

	def build(self, int_list):
		file = open(self.fileName, "wb")
		for integer in int_list:
			byte = integer.to_bytes(1, byteorder="big")
			file.write(byte)
		file.close()

	def print(self):

		file = open(self.fileName, "rb")
		content = file.read()
		file.close()

		print("[", end="")
		size = len(content)
		for i in range(0, size-1):
			print(str(content[i]) + ", ", end="")
		print(str(content[-1]) + "]")
		
		
