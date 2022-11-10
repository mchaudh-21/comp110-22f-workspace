"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730550997"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Find distance between two points."""
        distance = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Update cell."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self):
        """Method to change state of cell to infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Checks if cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Checks if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() == True:
            return "red"
        elif self.is_vulnerable() == True:
            return "gray"   
        elif self.is_immune() == True:
            return "green"

    def contact_with(self, cell2: Cell):
        """When two cells make contact and one is infected, the other gets infected."""
        if self.is_infected() and cell2.is_vulnerable():
            cell2.contract_disease()

        elif cell2.is_infected() and cell2.is_vulnerable():
            self.contract_disease()

    def immunize(self):
        """Make a cell immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self):
        """Returns immunity as bool."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, number_infected: int, number_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if number_infected >= cells or number_infected <= 0:
            raise ValueError("Some number of the Cell objects must be infected.")
        
        self.population = []
        for i in range(cells ):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

            if i in range(number_infected):
                self.population[i].contract_disease()
            else:
                for j in range(number_immune):
                    self.population[j].immunize()
        
        if number_immune >= cells or number_infected <= 0:
            raise ValueError(("Some number of the Cell objects must be immune."))

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
       
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)
    
    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        
        if cell.location.x  < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y  < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
        
    def check_contacts(self):
        """Check when cells come in contact."""
        cell1 = 0
        
        while cell1 < len(self.population):
            cell2 = cell1 + 1
            while cell2 < len(self.population):
                if self.population[cell1].location.distance(self.population[cell2].location) < constants.CELL_RADIUS:
                    self.population[cell1].contact_with(self.population[cell2])
                cell2 += 1
            cell1 += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        complete = False
        for i in self.population:
            if i.sickness <= 0:
                complete = True
            elif i.sickness >= 1:
                return False
        return complete