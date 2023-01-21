def casinoGame():
    toss_guesses = input()
    face_values  = input()
    v1, v2 = toss_guesses.split()
    v1, v2 = int(v1), int(v2)
    numerator_v1 = 0
    numerator_v2 = 0
    dice_values = []
    for i in face_values.split():
        x = int(i)
        if x == v1:
            numerator_v1 += 1
        elif x == v2:
            numerator_v2 += 1
    total_probability = numerator_v1 / 6 * numerator_v2 / 6
    return total_probability

print(casinoGame())
   
   
   



    # if v1 is equal to all of the face values:
        # face_f = 6/6
    # if v1 is equal to 5/6 face values:
        # face_f = 5/6
    # if v1 is equal to 4/6 face values:
        # face_f = 4/6
    # if v1 is equal to 3/6 face values:
        # face_f = 3/6
    # if v1 is equal to 2/6 face values:
        # face_f = 2/6
    # if v1 is equal to 1/6 face values:
        # face_f = 1/6
    # if v1 is equal to 0/6 face values:
        # face_f = 0/6
    # repeat above for v2 

# return int(toss1_guess) / 6 * int(toss2_guess) / 6 

'''

ace_values_list = [f1, f2, f3, f4, f5, f6]

if facevalues value 1 == toss_guesses value1 . . .

if v1 == f1 and v1 == f2 and v1 == f3 and v1 == f4 and v1 == f5 and f1 == f6:
        toss_f = 6/6
        toss_f = int(toss_f)

f v1 == f1 and v1 == f2 and v1 == f3 and v1 == f4 and v1 == f5 and v1 == f6:
        toss_f = 6/6
        toss_f = int(toss_f)
    if v1 != f2 and v1 != f2 and v1 != f3 and v1 != f4 and v1 != f5 and v1 != f6:
        toss_f = 0/6 
        toss_f = int(toss_f)

'''
