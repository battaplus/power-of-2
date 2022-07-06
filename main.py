print("Awesome program to do power of 2.")

# Prompt user for a number
print("Enter a number:", end=" ")
input = input()

# Check that the input is valid
if input.isdigit()==False:
	print("Not an integer")
	quit()

# Convert input to type integer
input = int(input)  

# Calculate power of 2
result = input*input

# Print results
if input<8:
	print("Can't you do this yourself?")
else:
  	print("The power of 2 of ", input, " is ", result, ".", sep="")

#--------------------------------------------------
# Alternate coding for learning python syntax
#--------------------------------------------------

#print(type(input))
#print(input.isdigit())


# Check that the input is valid
#if input.isdigit():
#	print(result)
#else:   
#	quit()

#--------------------------------------------------
# Additional notes for python syntax
#--------------------------------------------------

# In print statements. sep="" means no automatic spaces between elements.
# In print statements, end="" means no automatic newline.
