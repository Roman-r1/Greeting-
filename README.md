# Greeting CLI

A beginner-friendly command-line application that greets users by parsing their names.

## 📚 What I Learned

This is my **first Python portfolio project**. It demonstrates:

- **Input Handling**: Using `input()` and string methods like `.strip()` and `.title()`
- **String Manipulation**: Splitting names and formatting output
- **Functions**: Organizing code into reusable, well-documented functions
- **Error Handling**: Try-except blocks, input validation, and graceful error recovery
- **Best Practices**: Docstrings, comments, proper project structure, and naming conventions
- **Documentation**: Clear README and comprehensive inline documentation

## 🚀 How to Run

### Prerequisites

- Python 3.7 or higher
- Git (optional, for cloning)

### Installation

```bash
# Clone the repository
git clone https://github.com/Roman-r1/Greeting-.git
cd Greeting-
```

### Usage

```bash
python greeting.py
```

Then enter your name when prompted!

## 📝 Example

```
=============================================
Welcome to Greeting CLI
=============================================

What is your name? John Doe

Hello, John Doe! 👋
Welcome to the program test!
```

## 🔧 Features

- ✅ User input validation with re-prompting
- ✅ Proper name formatting (title case)
- ✅ Name splitting into first and last names
- ✅ Error handling for edge cases
- ✅ Graceful handling of keyboard interrupt (Ctrl+C)
- ✅ Clean, readable code structure
- ✅ Comprehensive documentation

## 📖 Code Structure

### `get_user_name()`
Prompts the user for their name with validation. Re-prompts if input is empty.

### `split_name(name)`
Splits a full name into first and last name components.

### `greet_user(first_name, last_name)`
Generates a personalized greeting message.

### `main()`
Orchestrates the entire application flow.

## 🎓 What's Next?

Ideas for expanding this project in the future:

1. **Unit Tests** – Add `pytest` to test each function
2. **Command-line Arguments** – Use `argparse` for more flexibility
3. **Persistent Storage** – Save greetings to a file
4. **Multiple Greeting Styles** – Add formal, casual, and fun greeting options
5. **Internationalization** – Support greetings in multiple languages
6. **Package Distribution** – Publish to PyPI

## 📚 Resources Used

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python – Python Functions](https://realpython.com/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## 💬 Feedback Welcome!

This is my first portfolio project! I'm open to feedback, suggestions, and pull requests.

Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Fork and extend the project

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Started:** June 16, 2026  
**Author:** [Roman-r1](https://github.com/Roman-r1)
