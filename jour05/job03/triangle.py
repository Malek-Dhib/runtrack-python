def draw_triangle(height):
    for i in range(height):
        if i == 0:
            print(' ' * (height - 1) + '/\\' )
        elif i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

hauteur = int(input("Veuillez entrer la hauteur du triangle : "))

draw_triangle(hauteur)
