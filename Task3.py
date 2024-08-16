# Import the necessary modules
import random
import string

def generate_password(length):
    """
    Generate a password of the specified length
    """
    # Define the characters that can be used in the password
    # string.ascii_letters includes all uppercase and lowercase letters
    # string.digits includes all digits from 0 to 9
    # string.punctuation includes all special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use a list comprehension to generate a password of the specified length
    # random.choice(characters) selects a random character from the characters string
    # This is done length number of times to generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Return the generated password
    return password

def main():
    """
    Main program
    """
    print("Password Generator")
    print("------------------")
    
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            # Get the length of the password from the user
            length = int(input("Enter the desired length of the password (min 8): "))
            
            # Check if the length is at least 8
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                # Break out of the loop if the length is valid
                break
        except ValueError:
            # If the user enters something that is not a number, print an error message
            print("Invalid input. Please enter a number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
