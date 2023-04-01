length = int(input("length in feet."))
width = int(input("width in feet."))
height = int(input("height in feet."))
 
 
def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")