class Solution():
    def __init__(self):
        self.formula = "" # Formula to be counted
        self.pointer = 0 # Current character in the formula being looked at
        self.counting = True # Should we continue counting atoms

    # Check if current character is a new element
    # Returns boolean
    def is_new_element(self):
        if self.formula[self.pointer].isalpha() and self.formula[self.pointer].isupper():
            return True
        return False

    # Get the full element being pointed at
    # Returns a string containing the element abbreviation
    def get_element(self):
        element = self.formula[self.pointer] # Set element string to the pointed at character
        self.pointer += 1 # Move pointer right
        checking = True # Boolean to see if still checking for element

        while checking: # For element
            # If the pointer is out of bounds, return element string
            if self.pointer >= len(self.formula):
                return element
            # If the pointed at character is a lowercase letter, add it to the element string
            if not self.formula[self.pointer].isalpha() or self.is_new_element():
                break
            element += self.formula[self.pointer] # Add the currently pointed at character to the element string
            self.pointer += 1 # Move pointer right
        return element

    # Get the full number being pointed at
    # Returns an integer converted from the string number
    def get_number(self):
        number = '' # Set to empty string for easy concatenation
        checking = True # Boolean to see if still checking for numbers

        while checking: # For numbers
            # If the pointer is out of bounds, break
            if self.pointer >= len(self.formula):
                break
            # If the pointed at character is not a number, break
            if self.formula[self.pointer].isalpha() or self.formula[self.pointer] in '()':
                break
            number += self.formula[self.pointer] # Add pointed at character to number string
            self.pointer += 1 # Move pointer right

        # If number string is empty, return 1
        if number == '':
            return 1
        return int(number) # Return number string as integer

    # Merge two given dictionaries together, adding the values when the same key is in both
    # Returns a dictionary containing the counts of both input dictionaries combined
    def merge_dicts(self, d1, d2):
        for key in d2.keys():
            if key in d1.keys():
                d1[key] += d2[key]
            else:
                d1[key] = d2[key]
        return d1

    # Multiply every value in a given dictionary by a given factor
    # Returns the multiplied dictionary
    def multiply_dict(self, d, f):
        for key in d.keys():
            d[key] *= f
        return d

    # Count how many of each atom is in a given formula
    # Returns a dictionary with key/value pairs of elements and their amounts respectively
    def count_atoms(self):
        atoms = {} # Initialise dictionary of atom counts

        # Keep looping if still counting
        while self.counting:
            #print(f"Pointer: {self.pointer}")

            # If the pointer is out of bounds, return
            if self.pointer >= len(self.formula):
                return atoms
            
            #print(f"Pointing at: '{self.formula[self.pointer]}'")
            
            if self.formula[self.pointer] == '(':
                self.pointer += 1 # Move pointer right
                self.merge_dicts(atoms, self.count_atoms()) # Count the atoms inside the brackets and merge the dictionaries
            elif self.formula[self.pointer] == ')':
                self.pointer += 1 # Move pointer right
                atoms = self.multiply_dict(atoms, self.get_number()) # Multiply the values in the brackets dictionary by a factor of the trailing number
                return atoms # Return the atom counts inside the brackets
            elif self.is_new_element():
                element = self.get_element()
                #print(f"Element: {element}")
                number = self.get_number()
                #print(f"Number: {number}")
                
                # If element already exists, add to existing amount, else create new element
                if element in atoms:
                    atoms[element] += number
                else:
                    atoms[element] = number

            #print(atoms)
        return atoms

    # Run count_atoms() and return its output
    def countOfAtoms(self, formula):
        self.formula = formula # Copy formula to class variable
        atoms = self.count_atoms() # Count the atoms
        atoms = {key:atoms[key] for key in sorted(atoms.keys())} # Sort dictionary
        #print(atoms)
        output = ''
        # Put the elements with counts into a string
        for key, value in atoms.items():
            # If the count is 1, only add the element
            if value == 1:
                output += key
            else:
                output += f'{key}{value}'
        return output
    
S = Solution()

#print(S.countOfAtoms("H2O"))
#print(S.countOfAtoms("Mg(OH)2"))
print(S.countOfAtoms("K4(ON(SO3)2)2"))
#print(S.countOfAtoms("Uuo"))