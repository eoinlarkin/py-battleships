# Battleships Game
![game-gif](/docs/images/game-demo.gif)

## Overview



### Game Sequence:
- Get user name
- Get board size
- Place ships on board
- Display board to user
- Ask user for shot
- Display board with shot
- Iterate through game

___



## Features

- A dynamically updated Terminal window, implemented using the `blessed` Python library
- Error checking and validation of user input
- A clear interface that is easy to understand and use
- A robust data model; the Board class is implemented in line with Object Orientated Programming principles and is portable to other implementations of 
___

## Data Model

___

## Testing


### Validator Testing 

Each of the Python scripts were validated against PEP8 validation, with the following validator used [PEP8 Validator](http://pep8online.com/). 

For the `layout.py` file, the PEP8 validator indicated that several lines exceeded the recommended length of 80 characters. However, this file is solely used to store the string constants which define the game boards and instruction text that is printed during the game. It was decided not to modify this file to resolve the validator errors. 

No issues were detected. Results from the validation were as follows:

- <details>
  <summary><strong style="color:skyblue">run.py:</strong></summary>
  <img src="./docs/images/pep8-run.png" alt="pep8-run-png"/>
  </details>
- <details>
  <summary><strong style="color:skyblue">battleship.py:</strong></summary>
  <img src="./docs/images/pep8-battleship.png" alt="pep8-battleship-image"/>
  </details>
- <details>
  <summary><strong style="color:skyblue">game.py:</strong></summary>
  <img src="./docs/images/pep8-game.png" alt="pep8-game-image"/>
  </details>
- <details>
  <summary><strong style="color:skyblue">layout.py:</strong></summary>
  <img src="./docs/images/pep8-layout.png" alt="pep8-layout-png"/>
  </details>
- <details>
  <summary><strong style="color:skyblue">termprint.py:</strong></summary>
  <img src="./docs/images/pep8-termprint.png" alt="pep8-termprint-png"/>
  </details>


___

## Deployment

The py-battleship repository was deployed using a `xterm.js` mock terminal to Herkou. 

The repoitory can be deployed as follows:
- Fork or clone the repository
- Create a new Heroku application
- For deployment, the `Python` and `NodeJS` buildpacks are required
- The foowing `Config Vars` are required:
    - PORT=8000
- Link the Heroku application to the repository
- Click *Deploy*

___


___

## Development

### Languages
- Python
- HTML
- CSS
- JavaScript
- jQuery

### Tools / Technologies

- **[VScode](https://code.visualstudio.com/)**  
All coding was completed in VS Code.
- **[Heroku](http://heroku.com/)**
Heroku was used for the deployment of the app.
- **[node-pty](https://github.com/microsoft/node-pty) and [xterm.js](https://github.com/xtermjs/xterm.js)**
These open source libraries were used to generate the web based terminal; these are integrated using a modified version of the CodeInstitute template
- **[blessed](https://github.com/jquast/blessed)
This Python library was used to dynamically update the Terminal window.
- **[coolors.co](https://coolors.co/)**  
Potential site palettes were tested with Coolors.  
- **[ASCII Art Generator](http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Battleships)**
This ASCII generator was used to create the game logo and welcome message
- **[gauger.io](https://gauger.io/fonticon/)**  
This website was used to generate the favicon using an icon from Font Awesome.
- **[Chrome Capture - Screenshots & Gifs](https://chrome.google.com/webstore/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe)**
This was used to create the animated gif showing the game functionality.
- **[https://ecotrust-canada.github.io/](https://ecotrust-canada.github.io/markdown-toc/)**  
For generating the formatted table of contents in markdown
- **[cdnjs](https://cdnjs.com/libraries/jquery)**  
cdnjs was used as the reference for the `jQuery` and `xterm` libraries.
- **[Google Fonts](https://fonts.google.com/)**  
Used to provide the custom fonts for the site



## Credits & Attributions

- **[blessed Python library](https://github.com/jquast/blessed)
Example applications and reference documentation for the `blessed` library was used to help implement the library features 
- **[How to draw a continuous line in terminal?](https://unix.stackexchange.com/questions/559708/how-to-draw-a-continuous-line-in-terminal)
The following StackExchange article was referenced to understand how to print complex characters to the Terminal
- **[Disable xterm.js scroll bar](https://github.com/xtermjs/xterm.js/issues/3074)
This issue was referenced to determine how to disable the scroll bar in the Terminal window
- **[Setting xterm.js font size](https://github.com/xtermjs/xterm.js/blob/4.14.1/typings/xterm.d.ts#L1031)
The `xterm.js` documentation was referenced to understand how to modify the Terminal font size
- **[CSS Vertical Stripes](https://css-tricks.com/stripes-css/)
The followign tutorial was used to help implement the vertical stripes for the Terminal background

