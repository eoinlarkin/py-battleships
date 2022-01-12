from blessed import Terminal
term = Terminal()


TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 43


def printTerminal(text, xcoords, ycoords, color):
    term.home
    with term.location(x=xcoords, y=ycoords):
       print(color + text)

def print_target_request():
    print(term.move(TERM_INPUT_LINE,0)+term.normal)
    target = input(term.white_on_blue + term.center('Select your next target:')+term.move(TERM_INPUT_LINE+1,58)+term.normal)
    return target

def clearTerminal():
    print(term.home + term.clear)

def target_invalid(xcoords,ycoords):
        term.home
        with term.location(x=xcoords, y=ycoords):
            print(term.black_on_yellow + term.center('Invalid coordinate selected; please try again...!' ))
   
def target_previously_selected(xcoords,ycoords):
        term.home
        with term.location(x=xcoords, y=ycoords):
            print(term.black_on_yellow + term.center('This target has already been selected; please select an alternative target.' ))

