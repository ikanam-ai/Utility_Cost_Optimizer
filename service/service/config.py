from __future__ import annotations

import os


class Config:
    _instance: Config = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False

        return cls._instance

    def __init__(self, override: bool = False):
        if self.__initialized and not override:
            return

        self.USER_LOGIN: str = os.environ.get("USER_LOGIN")
        self.USER_PASSWORD: str = os.environ.get("USER_PASSWORD")

        self.__initialized: bool = True
