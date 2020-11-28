import random
import numpy as np


class Player:
    def __init__(self, ag: object) -> None:
        self.agaria = ag
        self.color = (0,0,0)
        self.position = (200,200)
        self.health = 100
        self.size = 10
        self.age = 0
        self.NOP = 0
        self.UP = 1
        self.RIGHT = 2
        self.DOWN = 3
        self.LEFT = 4
        self.ACTION = [self.NOP, self.UP, self.RIGHT, self.DOWN, self.LEFT]
        self.RAM = np.zeros(128, dtype=np.uint32)

    def updateRAM(self):
        """This is an important part. call it every time the Player is modified"""
        self.RAM[0] = self.position[0]
        self.RAM[1] = self.position[1]
        self.RAM[2] = self.health
        self.RAM[3] = self.size
        self.RAM[4] = self.age

        pass

    def getRAM(self) -> np.ndarray:
        return self.RAM

    def getPosition(self) -> (int,int):
        return self.position

    def getHealth(self) -> int:
        return self.health

    def getSize(self) -> int:
        return self.size

    def getColor(self) -> (int,int,int):
        return self.color
