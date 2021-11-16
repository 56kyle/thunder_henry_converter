# thunder_henry_converter
A set of scripts used to convert the naming inside the Thunder Henry repo to the name you want for your survivor

## Usage
Just as a heads up you can ignore most of the errors thrown by the script. Most were just used for debugging and are accepted try statements.

#### Initial Setup
- follow the initial instructions of the Thunder Henry repo, once you there aren't errors in console when you clear it, you can continue
- clone/download this repository
- cd into thunder_henry_converter
- ```pip install -r requirements.txt```

#### Creating a New Survivor
- make sure that the unity project isn't open. (Seriously, there are actions that may break if files aren't generated at the times they are expected to)
- cd into thunder_henry_converter
- ```.\src\create_survivor <path to the unity project, the folder that contains Assets and Packages> <name of the new survivor in snake_case>```
- wait for the script to prompt you to open the project in Unity, then do so and close it before continuing.
- wait for the script to prompt you to open the project in Unity one last time, then do so and close it before continuing.
- wait for the script to finish
