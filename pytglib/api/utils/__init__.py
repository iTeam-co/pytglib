from .object import Object
from importlib import import_module
from .all_types import all_types

for k, v in all_types.items():
    Object.all[k[:1].lower() + k[1:]] = getattr(import_module("pytglib.api.types." + v), k)
