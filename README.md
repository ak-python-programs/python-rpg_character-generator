# 🛡️ RPG Character Validator & Sheet Generator

A robust Python utility designed for tabletop RPG systems to handle character creation. This script validates user input for character names and attributes, ensuring game balance through strict point-allocation rules and providing a visual character sheet output.

## 🚀 Features

* **String Validation**: Enforces naming conventions (no spaces, max 10 characters, non-empty).
* **Attribute Constraints**: Validates that stats (Strength, Intelligence, Charisma) are integers within the 1-4 range.
* **Point-Buy Balance**: Automatically calculates total points to ensure the character starts with exactly 7 points.
* **Visual Stat Bars**: Generates a clean, 10-point visual representation using Unicode symbols (● and ○).

## 🛠️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/aKmsdfhjb/python-rpg_character-generator.git](https://github.com/aKmsdfhjb/python-rpg_character-generator.git)
Run the script: You can import the function into your own project:

Python

from main import create_character

# Generate a character
# Example: Name 'Ren', Strength 4, Intelligence 2, Charisma 1
print(create_character("Ren", 4, 2, 1))
📊 Example Output
If the input is valid, the function returns a formatted sheet:

Plaintext

Ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
If the input is invalid (e.g., name too long), it returns a specific error: "The character name is too long."

🧪 Technical Implementation
The project demonstrates several core Python concepts:

Input Sanitization: Using isinstance() for type checking.

Logic Gates: Sequential if statements for error prioritizing.

String Arithmetic: Using * multipliers to generate visual bars dynamically.

F-Strings: Clean multi-line string formatting for output.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
