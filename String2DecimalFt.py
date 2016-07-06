import clr
import re
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# FUNCTIONS

def convert2DecimalFeet(strFtInches):
	feet = strFtInches.split("'")[0]
	inches = strFtInches.split("'")[1].split("\"")[0]
	return int(feet)+float(re.sub('[-]','', inches))/12
	
def convert2DecimalFt(strFtInches):
	feet = strFtInches.split("'")[0]
	inches = strFtInches.split("'")[1].split("\"")[0]
	if('/' in inches):
		wholeInches = inches.split(" ")[0]
		wholeInches = re.sub('[-]', '', wholeInches)
		fractionalInches = inches.split(" ")[1]
		numerator = fractionalInches.split("/")[0]
		denominator = fractionalInches.split("/")[1]
		decimalInches = int(wholeInches) + float(numerator)/float(denominator)
		return int(feet) + decimalInches/12
		
	else:
		return int(feet)+float(re.sub('[-]','', inches))/12

#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

convertedValues = []
for len in IN[0]:
	#convertedValues.append(convert2DecimalFeet(len))
	convertedValues.append(convert2DecimalFt(len))

#Assign your output to the OUT variable.
OUT = convertedValues
