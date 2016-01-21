# Morse Code Translator
_Morse Code: It's not dead yet._

Students will create a translator module that will read and write morse code messages. It will be able to both read and write morse code messages to external files.

The morse code Dictionary will be provided to students in a module they may leverage.

## Requirements
- A read_code function that accepts a filename and returns the English translation of the contents of the file.
- A write_code function that accepts an English message and filename, and writes the message in morse code to a file of the given name.
- The module should not execute any code when it is imported
- Students will use pair-programming to create their modules.

### Programing Concepts
- Python Dictionary
- File I/O
- Regex
- Module import
- Functional programming
- Pair-programming

### Fun Fact!
In morse code, there are 3 breaks between letters, and 7 breaks between words. So "Morse Code" would look like this in morse code:
"−− −−− ·−· ··· ·       −·−· −−− −·· ·"

#### Implementation Notes
- Remember to do 3 breaks (spaces) between letters, and 7 breaks (spaces) between words
- All files relevant to this assignment will reside in a directory called "morse_code", including this README, within the students Repo.
- The students module __must__ be named "morse_code.py"
- The functions defined in this documentation must be named "read_code" and "write_code" within the module. Any additional functions that may be created may be called whatever the student desires.
- Test morse code has been provided in the "test_code.txt" file. It translate to "Corgis are the best breed of dog, I don't care what you say."
