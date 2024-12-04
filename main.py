# Enhanced Python program to greet the user and provide additional information

def greet_user(name):
    """Function to greet the user with their name."""
    print(f"Hello, {name}!")

def name_length(name):
    """Function to calculate and return the length of the user's name."""
    return len(name)

def main():
    # Ask the user for their name
    name = input("Please enter your name: ")
    
    # Greet the user
    greet_user(name)
    
    # Calculate the length of the user's name
    length = name_length(name)
    
    # Display the length of the user's name
    print(f"Did you know? Your name has {length} characters.")

if __name__ == "__main__":
    main()
