import cv2

def getColor(letter_color):
    #return un triplet [?, ?, ?] correspondand a un triplet de couleur

    colors = {'r': (255, 0, 0), 'o': (255, 128, 0), 'b': (0, 0, 255),
              'g': (0, 255, 0), 'w': (255, 255, 255), 'y': (255, 255, 0)}
    return tuple(list(colors[letter_color.lower ()])[::-1])


def draw_cube(mini_cube, cube_state):
    for i in range (3):
        for j in range (3):
            if cube_state != None:
                mini_cube = cv2.rectangle(mini_cube, (2 + 40 * j, 2 + 40 * i),
                                    (35 + 40 * j, 35 + 40 * i), getColor(cube_state[i][j]), 3)
                mini_cube = cv2.putText(mini_cube, cube_state[i][j], (17 + 40 * j, 32 + 40 * i),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                  getColor (cube_state[i][j]), 1)
            else:
                mini_cube = cv2.rectangle(mini_cube, (2 + 40 * j, 2 + 40 * i),
                                    (35 + 40 * j, 35 + 40 * i), (128, 128, 128), 3)
    return mini_cube