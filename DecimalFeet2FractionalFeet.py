import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# PRECISION DICTIONARY - GLOBAL
# p1b32 = precision of 1 / 32... and so on
pdict = {'p1b2':2, 'p1b4':4, 'p1b8':8, 'p1b16':16, 'p1b32':32}

# FUNCTIONS

def convert2DecimalFeet(strFtInches):
	feet = strFtInches.split("'")[0]
	inches = str(strFtInches-int(strFtInches))[1:]
	return int(feet)+float(re.sub('[-]','', inches))/12
	
def convert2FractionalInches(decimalFeet, precision):
	#inches = str(decimalFeet-int(decimalFeet))[1:]
	inches = str(decimalFeet).split(".")[1]
	
	if(float(inches)==0):
		return 0
		
	inches = float(inches)*12
		
	return inches
	
def convert2FractionalFeetInches(decimalFeet, precision):
	feet = str(decimalFeet).split(".")[0]
	inches = round((decimalFeet - int(feet)),8)*12
	wholeInches = str(abs(inches)).split(".")[0]
	fractionalInches = abs(inches - int(wholeInches))
	
	fractionalNumerator = fractionalInches*precision
	numerator = int(fractionalNumerator)
	
	while(numerator%2==0 and precision > 2):
		numerator = int(numerator/2)
		precision = precision/2
	
	returnVal = ""
	if(numerator!=0):
		fraction = str(numerator) +"/"+str(precision)
		returnVal = str(feet)+"\'-"+ str(wholeInches) + " " + str(fraction)+"\""
	else:
		returnVal = str(feet)+"\'-"+ str(wholeInches)+"\""
	
	return returnVal
	

#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

convertedValues = []
for len in IN[0]:
	convertedValues.append(convert2FractionalFeetInches(len, pdict['p1b32']))
	
#Assign your output to the OUT variable.
OUT = convertedValues
