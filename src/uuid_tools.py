from requests import get

class UUIDTools:
	def __init__(self):
		self.api = "https://www.uuidtools.com/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def generate_uuid_v1(self, count: int = 1):
		return get(
			f"{self.api}/generate/v1/count/{count}",
			headers=self.headers).json()

	def generate_uuid_v3(self, name: str, name_space: str):
		return get(
			f"{self.api}/generate/v3/namespace/{name_space}/name/{name}",
			headers=self.headers).json()

	def generate_uuid_v4(self, count: int = 1):
		return get(
			f"{self.api}/generate/v4/count/{count}",
			headers=self.headers).json()

	def generate_uuid_v5(self, name: str, name_space: str):
		return get(
			f"{self.api}/generate/v5/namespace/{name_space}/name/{name}",
			headers=self.headers).json()

	def generate_timestamp_first_uuid(self, count: int = 1):
		return get(
			f"{self.api}/generate/timestamp-first/count/{count}",
			headers=self.headers).json()

	def decode_uuid(self, uuid: str):
		return get(
			f"{self.api}/decode/{uuid}",
			headers=self.headers).json()
