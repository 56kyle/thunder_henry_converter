# thunder_henry_converter
A set of scripts used to convert the naming inside the Thunder Henry repo to the name you want for your survivor

## Usage
Just as a heads up you can ignore most of the errors thrown by the script. Most were just used for debugging and are accepted try statements.

- clone/download this repository
- cd into thunder_henry_converter
- ```pip install -r requirements.txt```
- make sure you already have cloned the [altered ThunderHenry repo](https://github.com/56kyle/Thunderkit-Henry)
- open the ThunderHenry project in Unity, and make sure Assembly-CSharp.Public.dll as described in the ThunderHenry repository.
- close Unity
- ```.\src\create_survivor <path to Thunderkit-Henry-main\ThunderkitHenry\Thunderkit-Henry\ThunderkitHenry> <name of the new survivor in snake_case>```
- wait for the script to prompt you to open the project in Unity, then do so and close it before continuing.
- wait for the script to prompt you to open the project in Unity one last time, then do so and close it before continuing.
- wait for the script to finish
- open the project in Unity and click on Thunderkit-Henry-main\ThunderkitHenry\Thunderkit-Henry\ThunderkitHenry\Assets\Survivors\<SurvivorName>\Stage.asset
- set the manifest in the top right to be your new survivor's manifest
    
