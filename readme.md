# Python Command-Line Calculator - KRISHANG PATEL

This Python Command-Line Calculator is a versatile tool designed for performing arithmetic operations and managing calculation history with efficiency and ease. Featuring a Read-Eval-Print Loop (REPL), a dynamic plugin system, and advanced data handling with Pandas, this application caters to both casual users and developers seeking extensibility.

## Core Functionalities

- **REPL Interface**: An interactive command-line interface for arithmetic operations and calculation history management.
- **Plugin System**: Easily extendable with dynamically loaded plugins for additional functionalities.
- **Calculation History with Pandas**: Robust management of calculation history, including saving, loading, and deletion of records.
- **Professional Logging**: Detailed logging of operations, errors, and informational messages with configurable severity levels.
- **Advanced Data Handling**: Utilizes Pandas for efficient data operations and CSV file management.
- **Design Patterns**: Incorporates the Facade, Command, Factory Method, Singleton, and Strategy patterns for scalable architecture.

## Setup Instructions

1. **Installation**
   - Ensure Python 3.8+ is installed on your system.
   - Clone the repository: `git clone https://github.com/kdp8/IS219_midtermProject`.
   - Navigate to the project directory: `cd IS219_midtermProject`.
   - Install dependencies: `pip install -r requirements.txt`.

2. **Running the Application**
   - Launch the calculator: `python main.py`.
   - Use the `menu` command within the REPL for guidance on specific commands.

## Usage

This calculator application supports basic arithmetic operations, management of calculation history, and extension through plugins. Follow the instructions below to use these features.

For example, to perform addition:

1. Enter `add` at the prompt and press Enter.
2. When prompted with `> Num1: `, enter the first number you wish to add and press Enter.
3. When prompted with `> Num2: `, enter the second number and press Enter.
4. The application will calculate the sum and display the result.

## Architectural Decisions

### Design Patterns

- **Facade Pattern**: Simplifies complex data manipulations with Pandas, providing an easy-to-use interface for calculation history management.
- **Command Pattern**: Organizes commands within the REPL, allowing for scalable feature integration and management.
- **Factory Method, Singleton, Strategy Patterns**: Enhances code structure and flexibility, accommodating future application growth.

### Plugin System

- Dynamically loads plugins, enabling users to extend functionality without altering core code, fostering an open ecosystem for custom commands.

### Calculation History Management

- Employs Pandas for sophisticated data handling, supporting operations like load, save, and delete with high efficiency.

## Development, Testing, and Documentation

### Testing and Code Quality

- Achieves over 90% test coverage with pytest, ensuring robust application performance.
- Adheres to PEP 8 standards, with code quality verified by pylint, promoting maintainability and readability.

### Version Control

- Emphasizes logical commits, clearly documenting the development process and facilitating effective version tracking.

## License

This project is licensed under the MIT License.
