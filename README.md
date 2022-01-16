# Battleships Game

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

___

## Data Model

___

## Testing


### Validator Testing 

Each of the Python scripts were validated with the PEP8 validation. No issues were detected. Results from the validation were as follows:


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
Heroku was used for the deployment of the app..
- **[node-pty](https://github.com/microsoft/node-pty) and [xterm.js](https://github.com/xtermjs/xterm.js)**
These open source libraries were used to generate the web based terminal; these are integrated using a modified version of the CodeInstitute template
- **[cdnjs](https://cdnjs.com/libraries/jquery)**  
cdnjs was used as the reference for the `jQuery` and `xterm` libraries.
- **[coolors.co](https://coolors.co/)**  
Potential site palettes were tested with Coolors.  
- **[gauger.io](https://gauger.io/fonticon/)**  
This website was used to generate the favicon using an icon from Font Awesome.

- **[https://ecotrust-canada.github.io/](https://ecotrust-canada.github.io/markdown-toc/)**  
For generating the formatted table of contents in markdown
- **[Google Fonts](https://fonts.google.com/)**  
Used to provide the custom fonts for the site



## Credits & Attributions

ASCII Art Generator [link](http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Battleships)

Vertical Line in terminal: [link](https://unix.stackexchange.com/questions/559708/how-to-draw-a-continuous-line-in-terminal)

Setting font size: [link](https://github.com/xtermjs/xterm.js/blob/4.14.1/typings/xterm.d.ts#L1031)

Tips on removing the scrollbar: [link](https://github.com/xtermjs/xterm.js/issues/3074)

Tips on running code from run.py:
https://github.com/MattBCoding/calico-jack

Vertical stripes:
https://css-tricks.com/stripes-css/