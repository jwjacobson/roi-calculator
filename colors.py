# source: https://stackoverflow.com/questions/25709798/color-a-strings-segments-in-python
import termcolor

def colorChanger(s, firstSeg, secondSeg, thirdSeg, fourthSeg, hyphen):
     colors = [firstSeg, secondSeg, thirdSeg, fourthSeg]
     frags = s.split('-')
     for ind, color in enumerate(colors):
         frags[ind] = frags[ind].replace(frags[ind], termcolor.colored(frags[ind], color))
     return termcolor.colored('-', hyphen).join(frags)
 
string = "type-name-function-location"

print(colorChanger(string, 'red', 'green', 'yellow', 'magenta', 'cyan'))
print(colorChanger(string, 'yellow', 'blue', 'cyan', 'red', 'grey'))