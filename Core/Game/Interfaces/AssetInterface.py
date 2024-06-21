from abc import abstractmethod


class AssetInterface:

    @abstractmethod
    def load(self) -> any:
        pass
