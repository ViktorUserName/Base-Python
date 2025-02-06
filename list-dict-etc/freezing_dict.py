from copy import deepcopy
from types import MappingProxyType

config = {'db': {'host': 'localhost', 'port': 5432}}
immutable_config = MappingProxyType(deepcopy(config))