

def addnum(a, b):
	return a+b
	
if __name__ == "__main__":
    # Every python file when executed has a special variable called __name__. If the file is executed
    # directly, the value of the __name__ variable is equal to "__main__"
    
	print ("Executing the utils file")
	result = addnum(5,3)
	print(f"Result = {result}")