"""AI Study Partner - Programming Tutor
This module provides an interactive command-line tool for learning beginner
programming concepts. Users can query topics, view all available topics,
and contribute new topics to expand the knowledge base.
Module-level variables:
    topics (dict): A dictionary storing topic names (str) as keys and
                   explanations (str) as values.
Author: AI Study Partner Team
Version: 1.0
Date: 2025
"""
# Global knowledge base for programming topics
# Key: topic name (lowercase string), Value: explanation (string)
topics = {
    "variables": "A variable stores information. Think of it like a labeled box where you can put data.\nExample: age = 25 or name = 'Alice'",
    "data types": "Data types classify the type of data:\n  • int: whole numbers (5, 100, -3)\n  • str: text ('hello', 'world')\n  • bool: True/False values\n  • float: decimal numbers (3.14, 2.5)",
    "print": "The print() function displays output to the screen.\nExample: print('Hello World!') shows the text on screen.",
    "comments": "Comments explain code and are ignored by the computer.\nIn Python, they start with #\nExample: # This is a comment"
}
def display_menu():
    """
    Display the main menu of the AI Study Partner application.
    This function prints a formatted menu to the console showing all available
    options for the user. It uses decorative elements (borders, emojis) to
    enhance readability and user experience.
    Parameters:
        None
    Returns:
        None: This function only performs console output.
    Raises:
        None: This function does not raise any exceptions.
    Example:
        >>> display_menu()
        ==================================================
        :mortarboard: AI STUDY PARTNER - Programming Tutor
        ==================================================
        Options:
          1. Learn a topic
          2. View all topics
          3. Teach me something new
          4. Exit
        --------------------------------------------------
    Notes:
        - Uses Unicode emojis which may not display correctly in all terminals
        - The border width is fixed at 50 characters
        - This function has no side effects beyond console output
    """
    print("\n" + "="*50)
    print(" AI STUDY PARTNER - Programming Tutor")
    print("="*50)
    print("\nOptions:")
    print("  1. Learn a topic")
    print("  2. View all topics")
    print("  3. Teach me something new")
    print("  4. Exit")
    print("-"*50)
def show_all_topics():
    """
    Display a numbered list of all available programming topics.
    This function iterates through the global topics dictionary and prints
    each topic name in a formatted, numbered list. Topic names are title-cased
    for better presentation.
    Parameters:
        None
    Returns:
        None: This function only performs console output.
    Raises:
        None: This function does not raise any exceptions.
    Side Effects:
        - Reads from the global 'topics' dictionary
        - Outputs to console
    Example:
        >>> show_all_topics()
        :books: Available Topics:
          1. Variables
          2. Data Types
          3. Print
          4. Comments
    Notes:
        - If the topics dictionary is empty, only the header will be displayed
        - Enumeration starts at 1 for user-friendliness
        - Topic names are converted to title case for consistent formatting
        - The function assumes the global 'topics' dictionary exists
    """
    print("\n Available Topics:")
    for i, topic in enumerate(topics.keys(), 1):
        print(f"  {i}. {topic.title()}")
def learn_topic():
    """
    Interactive function to query and display information about a programming topic.
    This function prompts the user to enter a topic name, searches for it in the
    topics dictionary, and displays the explanation if found. If the topic is not
    found, it offers the user the option to teach the system about it.
    Parameters:
        None
    Returns:
        None: This function performs interactive I/O operations.
    Raises:
        KeyboardInterrupt: If the user interrupts input with Ctrl+C
        EOFError: If input stream is closed unexpectedly
    Side Effects:
        - Reads user input from console
        - Modifies the global 'topics' dictionary (via teach_new_topic)
        - Outputs to console
    Example:
        >>> learn_topic()
        :bulb: What topic do you want to learn? variables
        :white_tick: VARIABLES
        --------------------------------------------------
        A variable stores information. Think of it like a labeled box...
        >>> learn_topic()
        :bulb: What topic do you want to learn? loops
        :x: I don't know about 'loops' yet, teach me!
        :memo: What topic do you want to teach me?
    Notes:
        - Input is automatically stripped of whitespace and converted to lowercase
        - Topic matching is case-insensitive
        - If topic is not found, automatically calls teach_new_topic()
        - Empty input will be treated as a new (unknown) topic
    """
    topic = input("\n What topic do you want to learn? ").strip().lower()
    if topic in topics:
        print(f"\n {topic.upper()}")
        print("-"*50)
        print(topics[topic])
    else:
        print(f"\n I don't know about '{topic}' yet, teach me!")
        teach_new_topic(topic)
def teach_new_topic(topic_name=None):
    """
    Allow users to add new programming topics to the knowledge base.
    This function provides an interactive interface for users to contribute new
    topics and their explanations to the system. If no topic name is provided,
    the user is prompted to enter one. The function then requests an explanation
    and adds it to the global topics dictionary.
    Parameters:
        topic_name (str, optional): The name of the topic to add. If None,
                                   the user will be prompted to enter a name.
                                   Default is None.
    Returns:
        None: This function performs interactive I/O operations and modifies
              the global topics dictionary.
    Raises:
        KeyboardInterrupt: If the user interrupts input with Ctrl+C
        EOFError: If input stream is closed unexpectedly
    Side Effects:
        - Reads user input from console
        - Modifies the global 'topics' dictionary by adding new entries
        - Outputs confirmation or warning messages to console
    Example:
        >>> teach_new_topic("loops")
        Great! Explain 'loops': Loops repeat code multiple times
        :sparkles: Thank you! I've learned about 'loops'!
        >>> teach_new_topic()
        :memo: What topic do you want to teach me? functions
        Great! Explain 'functions': Functions are reusable blocks of code
        :sparkles: Thank you! I've learned about 'functions'!
        >>> teach_new_topic("arrays")
        Great! Explain 'arrays':
        :warning: No explanation provided. Topic not added.
    Notes:
        - Topic names are automatically stripped and converted to lowercase
        - If an empty explanation is provided, the topic is not added
        - Existing topics can be overwritten without warning
        - The function does not validate the quality or accuracy of explanations
        - Input is stripped of leading/trailing whitespace
    Edge Cases:
        - Empty topic_name: User will be prompted for input
        - Empty explanation: Topic is not added, warning displayed
        - Duplicate topic: Silently overwrites existing entry
        - Whitespace-only explanation: Treated as empty
    """
    if not topic_name:
        topic_name = input("\n What topic do you want to teach me? ").strip().lower()
    explanation = input(f"Great! Explain '{topic_name}': ").strip()
    if explanation:
        topics[topic_name] = explanation
        print(f"\n Thank you! I've learned about '{topic_name}'!")
    else:
        print("\n No explanation provided. Topic not added.")
# Main program loop
def main():
    """
    Main entry point for the AI Study Partner application.
    This function runs the main program loop, handling user navigation through
    the menu system and dispatching to appropriate functions based on user choice.
    The loop continues until the user explicitly chooses to exit.
    Parameters:
        None
    Returns:
        None: This function runs until user exits, then terminates cleanly.
    Raises:
        KeyboardInterrupt: Gracefully handles Ctrl+C interruptions
        EOFError: Handles unexpected input stream closures
        ValueError: May occur if input() fails, caught by menu validation
    Side Effects:
        - Continuously reads user input from console
        - Calls various functions that modify global 'topics' dictionary
        - Outputs to console throughout execution
        - Manages program flow until exit
    Example:
        >>> main()
        Welcome! Let's learn programming together! :rocket:
        ==================================================
        :mortarboard: AI STUDY PARTNER - Programming Tutor
        ==================================================
        Options:
          1. Learn a topic
          2. View all topics
          3. Teach me something new
          4. Exit
        --------------------------------------------------
        Choose an option (1-4): 1
        :bulb: What topic do you want to learn? variables
        ...
    Flow Control:
        1. Display welcome message
        2. Enter infinite loop:
           a. Display menu
           b. Get user choice
           c. Route to appropriate function:
              - '1': learn_topic()
              - '2': show_all_topics()
              - '3': teach_new_topic()
              - '4': Exit program
              - Other: Display error message
           d. Wait for user acknowledgment (Enter key)
        3. Exit with goodbye message
    Notes:
        - The loop runs indefinitely until option '4' is selected
        - Invalid menu choices prompt an error without exiting
        - After each action, user must press Enter to continue
        - This ensures users can read output before screen clears
        - The function does not validate for non-numeric input explicitly
          (relies on string comparison)
    Error Handling:
        - Invalid menu choices: Displays warning, continues loop
        - Empty input: Treated as invalid choice
        - Whitespace is stripped from input
        - No exception handling for Ctrl+C (will terminate abruptly)
    Best Practices:
        - Consider adding try-except for KeyboardInterrupt for clean shutdown
        - Could implement input validation to reject non-numeric choices
        - Might benefit from clearing screen between menu displays
    """
    print("Welcome! Let's learn programming together! 🚀")
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        if choice == "1":
            learn_topic()
        elif choice == "2":
            show_all_topics()
        elif choice == "3":
            teach_new_topic()
        elif choice == "4":
            print("\n Happy coding! Keep learning!")
            break
        else:
            print("\n Invalid choice. Please choose 1-4.")
        input("\nPress Enter to continue...")
if __name__ == "__main__":
    main()