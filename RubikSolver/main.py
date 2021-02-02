#This program solve 3x3 rubik's cube
#Version: 0.1
#Autor: Julien Collos
#Last modification: 02/01/2021
#Package: pycuber, rubik-cube

import pycuber as pc
from pycuber.solver import CFOPSolver

def scramble_cube(mycube):
    algo = pc.Formula ()
    random_alg = algo.random ()
    return mycube(random_alg), random_alg

def dispay_cube(mycube, formula_scramble):
    print("########################################################")
    print("#                                                      #")
    print("#          @         APP CUBE SOLVER         @         #")
    print("#                                                      #")
    print("########################################################")
    print()

    up = []
    front = []
    down = []
    left = []
    right = []
    back = []

    for layer in mycube.get_face("U"):
        up.append(layer)
    for layer in mycube.get_face("F"):
        front.append(layer)
    for layer in mycube.get_face("D"):
        down.append(layer)
    for layer in mycube.get_face("L"):
        left.append(layer)
    for layer in mycube.get_face("R"):
        right.append(layer)
    for layer in mycube.get_face("B"):
        back.append(layer)

    print("This is your new challange...\n")
    print("The new scramble is the following:")
    print(formula_scramble,"\n")

    print("            ", up[0])
    print("            ", up[1])
    print("            ", up[2])
    print(left[0], front[0], right[0], back[0])
    print(left[1], front[1], right[1], back[1])
    print(left[2], front[2], right[2], back[2])
    print("            ", down[0])
    print("            ", down[1])
    print("            ", down[2])
    print()

def menu(solver):
    print ("If you want the solution, please enter: yes")
    response = input ()
    if response == "yes":
        print("Solving is process...\n")
        solution = solver.solve (suppress_progress_messages=False)

    else:
        print ("The input is not 'yes'")
        menu(solver)

if __name__ == "__main__":
    mycube = pc.Cube()
    new_cube, formula_scramble= scramble_cube(mycube)
    dispay_cube(new_cube, formula_scramble)
    solver = CFOPSolver(mycube)
    menu(solver)



