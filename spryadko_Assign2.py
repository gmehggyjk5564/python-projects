# My name is Sofya.I am a 1st year CS student.
# This program computes volume for a cube, a pyramid and an ellipsoid.

# Create lists to store the results of volume calculations.
listCubeVolume=[]
listPyramidVolume=[]
listEllipsoidVolume=[]

# Create functions to calculate and return volume for different shapes.
def cubeVolume(sideLength):
  volumeCube = round(sideLength ** 3, 1)
  listCubeVolume.append(str(volumeCube))
  print("The volume of a cube with a length of side of "+str(sideLength)+" is "+str(volumeCube))

def pyramidVolume(height, baseLength):
  volumePyramid = round(1/3 * baseLength ** 2 * height, 1)
  listPyramidVolume.append(str(volumePyramid))
  print("The volume of a pyramid with the base length of "+str(baseLength)+" and the height of "+str(height)+" is "+str(volumePyramid))

def ellipsoidVolume(r1, r2, r3):
  import math
  volumeEllipsoid = round((4/3 * math.pi * r1 * r2 * r3), 1)
  listEllipsoidVolume.append(str(volumeEllipsoid))
  print("The volume of an ellipsoid with three radius of "+str(r1)+" ,"+str(r2)+" ,"+str(r3)+" is "+str(volumeEllipsoid)+"")

# Ask user for the shape that he wants to know the volume of.
# Based on the users input, prompt them for the necessary dimensions.
def computeVolume():
  shape = input('I will calculate the volume of a shape. What shape are you interested in?').lower()
  while shape != 'quit':
    if shape == 'cube':
     sideLength = int(input("What will be the length of the side for a cube? Enter:" ))
     cubeVolume(sideLength)
     return computeVolume()
    elif shape == 'pyramid':
      baseLength = int(input("What will be the base length of a pyramid? Enter:"))
      height = int(input("What will be the height of a pyramid? Enter:"))
      pyramidVolume(height, baseLength)
      return computeVolume()
    elif shape == 'ellipsoid':
      r1=int(input("The first radius will be:"))
      r2=int(input("The second radius will be:"))
      r3=int(input("The third radius will be:"))
      ellipsoidVolume(r1, r2, r3)
      return computeVolume()
    else:
      print("Invalid shape. You can enter 'cube', 'pyramid', 'ellipsoid' or, to end the session, 'quit'")
      return computeVolume()

# Make sure that loop will end as the user asks to quit the program.
  if shape == "quit":
     print("You have come to the end of the session.")
     if len(listCubeVolume) == 0 and len(listPyramidVolume) == 0 and len(listEllipsoidVolume) == 0:
        print("You did not perform any volume calculations.")
     else:
      print("The volumes calculated for each shape are shown below")
      if len(listCubeVolume) == 0:
        print("\nCube: No computations for this shape", end="")
      else:
        listCubeVolume.sort()
        print("\nCube: ", end="")
        for i in listCubeVolume:
         print(i,end=",")

      if len(listPyramidVolume) == 0:
        print("\nPyramid: No computations for this shape", end="")
      else:
        listPyramidVolume.sort()
        print("\nPyramid: ", end="")
        for i in listPyramidVolume:
         print(i, end=",")

      if len(listEllipsoidVolume) == 0:
        print("\nEllipsoid: No computations for this shape", end="")
      else:
        listEllipsoidVolume.sort()
        print("\nEllipsoid: ", end="")
        for i in listEllipsoidVolume:
          print(i, end=",")

# The program starts.
computeVolume()
