def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    def main():
        fruit : str = input("Enter a fruit: ")
        stock =num_in_stock(fruit)
        if stock == 0:
		        print("This fruit is not in stock.")
else:
		print("This fruit is in stock! Here is how many:")
print()

# There is no need to edit code beyond this point

def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()