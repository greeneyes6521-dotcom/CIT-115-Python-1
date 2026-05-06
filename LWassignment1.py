# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 2-16-2026
# Assignment: Planetary Weights

# Share what you liked about this assignment?
# I liked learning how to try to figure out how to get the proper output even though I
# found it confusing with applying inproper input when first trying.


# Share what you struggled with?
# I struggled with the order of the formatting structure options.  
# I used the word format instead of {} which made it more confusing. 
# I forgot about the use of fString f" in formatting.
# I struggled with the alingnment of the column output.


# Explain specifically how you used the Python forematting options to align the output


# Share exactly three things you learned on this assignment:
#1. How to align the colums to show in output by specifying width.  
#2. How converting to a fString simplifies how much input you have to type in
#   versus using (format).
#3. Learned a better understanding of formatting order and options.

# Named Constants Surface Gravity Factor (SGF)
# nPlanets name = number
nMERCURY_SGF = 0.38
nVENUS_SGF = 0.91
nMOON_SGF = 0.165
nMARS_SGF = 0.38
nJUPITER_SGF = 2.34
nSATURN_SGF = 0.93
nURANUS_SGF = 0.92
nNEPTUNE_SGF = 1.12
nPLUTO_SGF = 0.066

#1. Input
# Make name string = Input ask What is your name
sName = input("What is your name? ")
fWeight = input("What is your weight? ")    
#2. Convert fWeight to float
fWeight = float(fWeight)

#2. Compute  Multiply fWeight by each planets Surface gravity factor
# Multiply each planets SGF by weight entered converted to float (fWeight * each planets SGF)
fMercuryWeight = fWeight * nMERCURY_SGF
fVenusWeight = fWeight * nVENUS_SGF
fMoonWeight = fWeight * nMOON_SGF
fMarsWeight = fWeight * nMARS_SGF
fJupiterWeight = fWeight * nJUPITER_SGF 
fSaturnWeight = fWeight * nSATURN_SGF
fUranusWeight = fWeight * nURANUS_SGF
fNeptuneWeight = fWeight * nNEPTUNE_SGF
fPlutoWeight = fWeight * nPLUTO_SGF

#3. Output
# print out to scren sName Here are your weights on our solar systems planets.
print(sName , ("Here are your weights on our solar systems planets. "))

#3.1 Convert fHuman weight to a string with formatting that is 10 charachters with 2 decimal points:
# print out to screen by making into a fString adding formatting to align and formatting for decimal float.
print(f"{'Weight on Mercury':20s} {fMercuryWeight:10.2f} ")
print(f"{'Weight on Venus':20s} {fVenusWeight:10.2f} ")
print(f"{'Weight on Moon':20s} {fMoonWeight:10.2f} ")
print(f"{'Weight on Mars':20s} {fMoonWeight:10.2f} ")
print(f"{'Weight on Jupiter':20s} {fJupiterWeight:10.2f} ")
print(f"{'Weight on Saturn':20s} {fSaturnWeight:10.2f} ")
print(f"{'Weight on Uranus':20s} {fUranusWeight:10.2f} ")
print(f"{'Weight on Neptune':20s} {fNeptuneWeight:10.2f} ")     
print(f"{'Weight on Pluto':20s} {fPlutoWeight:10.2f} ")

