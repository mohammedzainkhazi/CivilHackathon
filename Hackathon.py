
# Libraries used for plotting Graphs 

import matplotlib.pyplot as plt
import numpy as np



# Simple Support Functionality 
def simple_support():
	print("Select Type of Simple Support Beam ")
	opt=5
	while opt !=2 and opt !=1:
								# Choice Entry for 2 options 

		opt = int(input("1. Point Load \t 2.UDL\n: "))
		if opt == 1:
			length= float(input("Enter the length of the beam: "))
			weight= float(input("Enter the weight of the point load (in KN): "))
			x=-1

			# Condition for X should be +ve number less than the length of BEAM 

			while x<0 or x>length:
				x=float(input("Enter the distance of the point to calculate SF & BMD : "))
			 
			# BMD Calculation at origin / left point
			bmd= weight*x*(length-x)/length

			# SFD Calculation at origin / left point

			sfdR1=weight*(length-x)/length

			# SFD Calculation at right point

			sfdR2=weight*x/length

			# Printing Values 
			print("The BMD is:",bmd,"\nThe SFD at A:",sfdR1,"The SFD at B:",sfdR2)

			# Plotting Values in Graph 
			xpoints= np.array([0,x,length])
			ypoints=np.array([0,bmd,0])
			plt.plot(xpoints,ypoints,'b')
			plt.plot(np.array([0,length]),np.array([0,0]),'g')
			plt.title("BMD Graph")
			plt.show()
			plt.title("SFD Graph")
			plt.plot(np.array([0,0,x,x,length,length]),np.array([0,sfdR1,sfdR1,-sfdR2,-sfdR2,0]),'b')
			plt.plot(np.array([0,length]),np.array([0,0]),'y')
			plt.show()

		elif opt == 2:
			length= float(input("Enter the length of the beam: "))
			weight= float(input("Enter the weight per metre (in KN/M): "))
			x=-1
			# Condition for X should be +ve number less than the length of BEAM 
			while x<0 or x>length:
				x=float(input("Enter the distance of the point to calculate SF & BMD : "))

			# BMD Calculation at given Point 
			bmd= weight*length*x/2-weight*x*x/2
			
			# SFD Calculation at given point
			sfdR1=weight*length/2-weight*x
			print("The BMD at given distance is:",bmd,"\nThe SFD at distance given is:",sfdR1)
			
			# Plotting Graphs 
			xpoints= np.linspace(0,length,1000)
			ypoints=weight*xpoints*length/2-weight*xpoints*xpoints/2
			plt.plot(xpoints,ypoints,'b')
			plt.plot(np.array([0,length]),np.array([0,0]),'y')
			plt.show()
			ypoints=weight*length/2-weight*xpoints
			plt.plot(xpoints,ypoints,'b')
			plt.plot(np.array([0,length]),np.array([0,0]),'y')
			plt.show()



def cantelever_support():
	print("Select Type of Cantelever Support Beam")
	opt=5
	while opt !=2 and opt !=1:
		opt = int(input("1. Point Load \t 2.UDL\n: "))
		if opt == 1:
			length= float(input("Enter the length of the beam: "))
			weight= float(input("Enter the weight of the point load at free end(in KN): "))
			x=-1
			# Condition for X & Length should be +ve number less than the length of BEAM 
			while x<0 or x>length:
				x=float(input("Enter the distance of the point to calculate SF & BMD : "))


			bmd= -weight*x
			sfd= -weight
			print("The BMD is:",bmd,"\nThe SFD is:",sfd)
			xpoints= np.array([0,length])
			ypoints=np.array([0,-weight*length])

			# Plotting Graphs - SFD & BMD 

			plt.plot(xpoints,ypoints)
			plt.title("BMD Graph")
			plt.plot(np.array([0,length]),np.array([0,0]))
			plt.show()

			plt.title("SFD Graph")
			ypoints=xpoints*0+sfd
			plt.plot(xpoints,ypoints)
			plt.plot(np.array([0,length]),np.array([0,0]))
			plt.show()

		elif opt == 2:
			length= float(input("Enter the length of the beam: "))
			weight= float(input("Enter the weight per metre (in KN/M): "))
			x=-1

			# Condition for X should be +ve number less than the length of BEAM 
			while x<0 or x>length:
				x=float(input("Enter the distance of the point to calculate SF & BMD : "))

			# Calculating BMD & SFD at given point 
			bmd= -weight *x*x/2
			sfd=-weight*x
			print("The BMD at given distance is:",bmd,"\nThe SFD at given distance is:",sfd)


			# Plotting Graphs 

			xpoints= np.linspace(0,length,1000)
			ypoints=-weight* xpoints*xpoints/2
			plt.plot(xpoints,ypoints,'b')
			plt.title("BMD Graph")
			plt.plot(np.array([0,length]),np.array([0,0]),'y')
			plt.show()
			ypoints=-weight*xpoints
			plt.plot(xpoints,ypoints,'b')
			plt.title("SFD Graph")
			plt.plot(np.array([0,length]),np.array([0,0]),'y')
			plt.show()

# Beginning Point of Program 

if __name__ == '__main__':
	print("Select Type of Beam ")
	beam = int(input("1. SIMPLE Support \t 2.Cantiliver\n:"))
	print(beam)
	if beam == 1:
		simple_support()
	elif beam == 2:
		cantelever_support()
	else:
		print('Choose Right Option ')
