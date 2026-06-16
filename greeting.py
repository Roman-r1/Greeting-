"""
Greeting CLI: A beginner-friendly program to parse and greet users.

Demonstrates:
- Input validation and error handling
- String manipulation and splitting
- Function documentation and best practices
- Clean code structure

Author: Roman-r1
Date: 2026-06-16
"""

def get_user_name():
    """
    Prompt user for their name with validation.
    
    Keeps asking until the user provides a valid non-empty name.
    Handles keyboard interrupt (Ctrl+C) gracefully.
    
    Returns:
        str: Non-empty name in title case, or None if user cancels.
    """
    while True:
        try:
            name = input("What is your name? ").strip().title()
            
            # Validate input
            if not name:
                print("⚠️  Please enter a valid name.\n")
                continue
                
            return name
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            return None
        except Exception as e:
            print(f"❌ Error: {e}\n")


def split_name(name):
    """
    Split a full name into first and last name.
    
    Takes a full name and extracts the first word as first name
    and the last word as last name. If only one word is provided,
    returns it as first name with an empty last name.
    
    Args:
        name (str): Full name (e.g., "John Doe" or "John F Kennedy")
        
    Returns:
        tuple: (first_name, last_name)
        
    Examples:
        >>> split_name("John Doe")
        ("John", "Doe")
        >>> split_name("Mary")
        ("Mary", "")
        >>> split_name("Alice Bob Smith")
        ("Alice", "Smith")
    """
    if not name:
        return "", ""
    
    parts = name.split()
    
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]  # Last word is considered last name
    else:
        first_name = parts[0]
        last_name = ""
    
    return first_name, last_name


def greet_user(first_name, last_name):
    """
    Generate a personalized greeting message.
    
    Creates a friendly greeting based on whether a last name was provided.
    
    Args:
        first_name (str): User's first name
        last_name (str): User's last name (can be empty)
        
    Returns:
        str: Formatted greeting message
        
    Examples:
        >>> greet_user("John", "Doe")
        "Hello, John Doe! 👋"
        >>> greet_user("Mary", "")
        "Hello, Mary! 👋"
    """
    if last_name:
        return f"Hello, {first_name} {last_name}! 👋"
    else:
        return f"Hello, {first_name}! 👋"


def main():
    """
    Main program flow.
    
    Orchestrates the greeting application:
    1. Displays welcome message
    2. Gets user's name with validation
    3. Parses the name into first and last
    4. Generates and displays personalized greeting
    """
    print("=" * 45)
    print("Welcome to Greeting CLI")
    print("=" * 45 + "\n")
    
    # Get and validate user input
    name = get_user_name()
    if not name:  # User cancelled with Ctrl+C
        return
    
    # Parse the name
    first_name, last_name = split_name(name)
    
    # Greet the user
    greeting = greet_user(first_name, last_name)
    print(f"\n{greeting}")
    print("Welcome to the program test!\n")


if __name__ == "__main__":
    main()
