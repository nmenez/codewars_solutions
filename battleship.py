import unittest
from itertools import product
from math import sqrt
from collections import Counter


def istouching(ship, othership):
    touching_dist = sqrt(2)
    for p1, p2 in product(ship, othership):
        dist = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        if dist <= touching_dist:
            return True
    return False


def getNeighbors(point):
    r, c = point
    pot_neighbors = [(r - 1, c), (r, c - 1),
                     (r, c + 1), (r + 1, c)]

    neighbors = [(r, c) for r, c in pot_neighbors if (
        r >= 0) and (r < 10) and (c >= 0) and (c < 10)]
    return neighbors


def followpoint(point, battlefield, priorcoords=[]):
    priorcoords.append(point)
    battlefield[point[0]][point[1]] = 's'
    neighbors = getNeighbors(point)
    try:
        next_point = (
            list(filter(lambda p: battlefield[p[0]][p[1]] == 1, neighbors)))[0]
        priorcoords = followpoint(next_point, battlefield, priorcoords)
    except IndexError:
        return priorcoords
    return priorcoords


def scanfield(battlefield):
    ships = []
    for r in range(10):
        for c in range(10):
            if battlefield[r][c] == 1:
                ship_coords = followpoint((r, c), battlefield, priorcoords=[])
                ships.append(ship_coords)
    return ships


def checkshipCount(ships):
    correct = Counter([4, 3, 3, 2, 2, 2, 1, 1, 1, 1])
    shipcount = Counter([len(ship) for ship in ships])
    return correct == shipcount


def checkShipShape(ship):
    if len(ship) == 1:
        return True
    directions = {(-1, 0): 'u', (1, 0): 'd', (0, -1): 'l', (0, 1): 'r'}
    ship_directions = [directions[(nextp[0] - p[0], nextp[1] - p[1])]
                       for p, nextp in zip(ship[:-1], ship[1:])]
    return len(set(ship_directions)) == 1


def validateBattlefield(field):
    ships = scanfield(field)
    if checkshipCount(ships):
        for i, shipA in enumerate(ships):
            if not checkShipShape(shipA):
                return False

            for j, shipB in enumerate(ships):
                if i == j:
                    continue
                else:
                    if istouching(shipA, shipB):
                        return False
        return True
    else:
        return False


class TestBattleShip(unittest.TestCase):
    def testtouching(self):
        battleship = [(1, 4), (2, 4), (3, 4), (4, 4)]
        sub = [(5, 5)]
        cruiser = [(2, 5), (2, 6), (2, 7)]

        self.assertTrue(istouching(battleship, sub))
        self.assertTrue(istouching(battleship, cruiser))
        self.assertFalse(istouching(cruiser, sub))

    def testpotneighbors(self):
        self.assertEqual(getNeighbors((0, 1)), [(0, 0), (0, 2), (1, 1)])
        self.assertEqual(getNeighbors((4, 4)), [
                         (3, 4), (4, 3), (4, 5), (5, 4)])
        self.assertEqual(getNeighbors((9, 0)), [(8, 0), (9, 1)])
        self.assertEqual(getNeighbors((9, 9)), [(8, 9), (9, 8)])

if __name__ == "__main__":
    battleField = [[1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(validateBattlefield(battleField))
