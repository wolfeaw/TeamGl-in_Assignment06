# main.py
# Name: Drew Wolfe
# Email: wolfeaw@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/25
# Course #/Section: IS4010-002
# Semester/Year: Spring 2025
# Brief description of the assignment: Use OOP with a partner
# Brief description of what this module does: Instantiates the JarJarBinks class
# Citations: 
# Anything else that's relevant:

from jarjarbinks_package.jar_jar import JarJarBinks
if __name__ == "__main__":
    jarjar = JarJarBinks()

    print("Initial State:", jarjar)  
    print("Debug Representation:", repr(jarjar))  
    print("Mishap 1:", jarjar.cause_mishap())
    print("Mishap 2:", jarjar.cause_mishap())
    print("Energy Before:", jarjar.energy_level) 
    
    jarjar.energy_level = 50
    print("Energy After Manual Change:", jarjar.energy_level)
    print("Final State:", jarjar)
