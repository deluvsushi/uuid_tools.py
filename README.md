# uuid_tools.py
Web-API for [uuidtools.com](https://www.uuidtools.com) website that provides a free tool and API for generating UUIDs on-the-fly

## Example
```python
import uuid_tools
uuid_tools = uuid_tools.UUIDTools()
decoded_uuid = uuid_tools.decode_uuid(uuid="")
print(decoded_uuid)
```
