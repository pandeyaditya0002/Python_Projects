import random  # random module to generate random values
import string  # string module to access different character sets

# Function to generate a secure password
def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters   

    if use_digits:
        characters += string.digits  
    
    if use_special_chars:
        characters += string.punctuation  # Adds symbols like @, #, $, etc.
    
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None  
    
    # Generate a password by randomly selecting characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password

# Main function to handle user interaction
def main():
    print("Welcome to the Password Generator!")
   
    length = int(input("Enter password length: "))
    
    use_digits = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    
    # Generate the password based on user inputs
    password = generate_password(length, use_digits, use_special_chars)
    
    # Display the generated password
    if password:
        print(f"Generated Password: {password}")

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to execute the program
