import string
from Core.Game.Interfaces.AssetInterface import AssetInterface
from collections import defaultdict


class _AssetCollection:
    def __init__(self):
        self._assets: dict[str, AssetInterface] = {}

    def register_asset(self, name: string, asset: AssetInterface):
        self._assets[name] = asset

    def get_asset(self, name) -> AssetInterface:
        return self._assets[name]


class GameAssetManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameAssetManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._assets = defaultdict(_AssetCollection)
            cls._instance._content_directory = ""
        return cls._instance

    def set_content_directory(self, directory: string):
        self._content_directory = directory

    def get_content_directory(self) -> string:
        return self._content_directory

    def register_asset(self, asset_type, name: string, asset: AssetInterface):
        self._assets[asset_type].register_asset(name, asset)

    def get_asset(self, asset_type, name: string) -> AssetInterface:
        return self._assets[asset_type].get_asset(name)