possible_locations_for_letter = []
height = 375
width = 375
remove_after_game = []
back_up = []
taken_posistions = []
list_of_letters = [['','',''],['','',''],['','','']]
turn = True #true = X, false = Y 
diameter = 5
number_split = 5
done_game = False

#EASIER SQUARE
def square(width, length, pos_x, pos_y, color = Color.black):
    square = Rectangle(width, length)
    square.set_position(pos_x, pos_y)
    square.set_color(color)
    add(square)
    return square

#EASIER CIRCLE 
def circle(diameter, pos_x, pos_y, color = Color.black):
    circle = Circle(diameter)
    circle.set_position(pos_x, pos_y)
    circle.set_color(color)
    add(circle)
    return circle
    
#EASIER TEST    
def text(text, pos_x, pos_y, color = Color.black):
    text = Text(text)
    text.set_position(pos_x, pos_y)
    text.set_color(color)
    add(text)
    return text

#BUTTON, USES EVENT HANDLERS
def click_event(x, y):
    global possible_locations_for_letter, turn, back_up, done_game, turn, list_of_letters
    if done_game:
        for i in remove_after_game:
            remove(i)
        possible_locations_for_letter = []
        for i in back_up:
            possible_locations_for_letter.append(i)
        list_of_letters = [['','',''],['','',''],['','','']]
        done_game = not done_game
        turn = True
        return
    
    for loc in possible_locations_for_letter:
        loc_x = loc.get_x() #loc of square (x)
        loc_y = loc.get_y() #loc of square (y)
        width = int(loc.get_width()) #opposite side of square (x)
        height = int(loc.get_height()) #opposite side of square (y)
        x_true = False #check if in loc (x)
        y_true = False #check if in loc (y)
        #checks if in a square (x)
        if (loc_x <= x and loc_x + width >= loc_x:
            x_true = True
            break
        #checks if in a square (y)
        if x_true:
            if (loc_y <= y and loc_y + height >= loc_y:
                if (loc_y + i) == y:
                    y_true = True
                    break
            if y_true:
                if turn:
                    build_x(loc)
                else:
                    build_y(loc)
                turn = not turn
                possible_locations_for_letter.remove(loc)
                is_done_game()#?
                break
            
#builds the X 
def build_x(loc):
    global list_of_letters, taken_posistions
    for i in range(len(taken_posistions)):
        if (taken_posistions[i] == loc):
            list_in_loc = i / 3
            loc_letter = i % 3
            list_of_letters[list_in_loc][loc_letter] = 'x'
    x = loc.get_x()
    y = loc.get_y()
    width = loc.get_width()
    height = loc.get_height()
    x_coords = width/2+x
    y_coords = height/2+y
    for i in range(30):
        remove_after_game.append(circle(5, x_coords+i, y_coords+i))
        remove_after_game.append(circle(5, x_coords+i, y_coords-i))
        remove_after_game.append(circle(5, x_coords-i, y_coords+i))
        remove_after_game.append(circle(5, x_coords-i, y_coords-i)) 

#builds the Y
def build_y(loc):
    global list_of_letters, taken_posistions
    for i in range(len(taken_posistions)):
        if (taken_posistions[i] == loc):
            list_in_loc = i / 3
            loc_letter = i % 3
            list_of_letters[list_in_loc][loc_letter] = 'o'
    x = loc.get_x()
    y = loc.get_y()
    width = loc.get_width()
    height = loc.get_height()
    x_coords = width/2+x
    y_coords = height/2+y
    remove_after_game.append(circle(35, x_coords, y_coords, Color.black))
    remove_after_game.append(circle(25, x_coords, y_coords, Color.white))
#  checks if done with game, COULD be way more effient (RAM) if using java :/
def is_done_game():
    global list_of_letters
    horozontal = [[],[],[]]
    vertical = [[],[],[]]
    diagonal = [[], []]
    for i in range(3):
        for j in range(3):
            horozontal_letter = list_of_letters[i][j]
            vertical_letter = list_of_letters[i][j]
            horozontal[j].append(horozontal_letter)
            vertical[i].append(vertical_letter)
    diagonal[0].append(list_of_letters[0][0])
    diagonal[0].append(list_of_letters[1][1])
    diagonal[0].append(list_of_letters[2][2])
    diagonal[1].append(list_of_letters[0][2])
    diagonal[1].append(list_of_letters[1][1])
    diagonal[1].append(list_of_letters[2][0])
    for j in range(3):
        horozontal_count_x = 0;
        horozontal_count_o = 0;
        vertical_count_x = 0;
        vertical_count_o = 0;
        for i in horozontal[j]:
            #replace print(x) with a win game fuct 
            if (i == 'x'):
                horozontal_count_x += 1
            if (i == 'o'):
                horozontal_count_o += 1
            if (horozontal_count_x >= 3):
                win_game("x", horozontal[j])
                return
            if (horozontal_count_o >= 3):
                win_game("o", horozontal[j])
                return
        for i in vertical[j]:
            if (i == 'x'):
                vertical_count_x += 1
            if (i == 'o'):
                vertical_count_o += 1
            if (vertical_count_x >= 3):
                win_game("x", vertical[j])
                return
            if (vertical_count_o >= 3):
                win_game("o", vertical[j])
                return
    for j in range(len(diagonal)):
        diagonal_count_x = 0
        diagonal_count_o = 0
        for i in diagonal[j]:
            if (i == 'x'):
                diagonal_count_x += 1
            if (i == 'o'):
                diagonal_count_o += 1
            if (diagonal_count_x >= 3):
                win_game("x", diagonal[j])
                return
            if (diagonal_count_o >= 3):
                win_game("o", diagonal[j])
                return
    num = 0
    for i in horozontal:
        for j in i:
            if not ('' == j):
                num+=1
    if num >= 9:
        tie_game()
def win_game(winner, list_of_win_loc):
    global done_game
    done_game = True
    remove_after_game.append(text(winner + " wins!", get_width()/2, get_height()/2, Color.red))
def tie_game():
    global done_game
    done_game = True
    remove_after_game.append(text("You tied", get_width()/2, get_height()/2, Color.red))
#BUILDS BOARD
def build_board():
    global width, height, diameter, possible_locations_for_letter, taken_posistions, number_split
    set_size(width, height)
    #Generates left side of board
    for i in range(1, 4):
        for j in range(1, 4):
            button = square(width/3, height/3, (i-1)*width/3, (j-1)*height/3, Color.white)
            possible_locations_for_letter.append(button)
            back_up.append(button)
            taken_posistions.append(button)
    for i in range((int)((width-diameter*2)/number_split)):
        circle(diameter, width/3, diameter+i*number_split)
    for i in range((int)((width-diameter*2)/number_split)):
        circle(diameter, width*2/3, diameter+i*number_split)
    for i in range((int)((width-diameter)/number_split)):
        circle(diameter, diameter+i*number_split, height/3)
    for i in range((int)((width-diameter*2)/number_split)):
        circle(diameter, diameter+i*number_split, height*2/3)
build_board()
add_mouse_click_handler(click_event)
