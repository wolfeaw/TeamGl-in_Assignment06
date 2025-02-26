# jar_jar.py
# Name: Connor Thomas
# Email: thoma5cg@mail.uc.edu
# Assignment Number: Assignment06
# Due Date: 2/26/25
# Course #/Section: IS4010/002
# Semester/Year: 2nd/4th
# Brief description of the assignment: Collaborate with a partner to develop a Python project in VS.
# Brief description of what this module does: Defines a class that models Jar Jar Binks.
# Citations:
# Anything else that's relevant:

from random import choice
class JarJarBinks:
    """
    A class representing Jar Jar Binks
    """
    def __init__(self, energy_level=100, mood="cheerful"):
        """
        Initialize Jar Jar Binks with an energy level and mood
        @param energy_level int: The energy level of Jar Jar
        @param mood string: The current mood of Jar Jar
        """
        self._energy_level = energy_level
        self.mood = mood
    def __str__(self):
        """
        Return a human readable string representation of Jar Jar
        @return string: A formatted string describing Jar Jar's current state
        """
        return f"Jar Jar Binks - Energy: {self._energy_level}, Mood: {self.mood}"
    def __repr__(self):
        """
        Return an unambiguous string representation of the object
        @return string: A representation of the JarJarBinks object
        """
        return f"JarJarBinks(energy_level={self._energy_level}, mood='{self.mood}')"
    @property
    def energy_level(self):
        """
        Get Jar Jar's energy level.
        @return int: The current energy level of Jar Jar
        """
        return self._energy_level
    @energy_level.setter
    def energy_level(self, value):
        """
        Set Jar Jar's energy level, ensuring it stays within 0-100
        @param value int: The new energy level to set 
        @raises ValueError: If the energy level is outside the valid range
        """
        if 0 <= value <= 100:
            self._energy_level = value
        else:
            raise ValueError("Energy level must be between 0 and 100.")
    def cause_mishap(self):
        """
        Simulate Jar Jar Binks accidentally causing chaos
        @return string: A randomly chosen mishap description and updated energy level
        """
        mishaps = [
            "trips over his own feet",
            "knocks over a battle droid",
            "drops his booma grenade in the wrong place",
            "gets his tongue stuck in a podracer engine",
            "accidentally saves the day",
        ]
        mishap = choice(mishaps)
        self.energy_level -= 10 
        return f"Jar Jar {mishap}! His energy drops to {self.energy_level}."