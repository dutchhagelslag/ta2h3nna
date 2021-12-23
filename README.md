# ta2h3nna
- https://ta2h3nna.herokuapp.com/

![example workflow](https://github.com/dutchhagelslag/ta2h3nna/actions/workflows/main.yml/badge.svg)
- Github actions (main)

[![Build Status](https://app.travis-ci.com/dutchhagelslag/ta2h3nna.svg?branch=master)](https://app.travis-ci.com/dutchhagelslag/ta2h3nna)
- Travis (will run out again soon)

## Requirements
- Create Request from user input for a tattoo/henna design by type (ie. flower & old school)
- Fetch Designs and display to user as image inially.
- Fetch potential artists with correct specialty.
- The user will have the option to view all available artists, designs and fonts. 
- Create a request from user input for a visualisation of a font as an image. 



## Design
The design requirements are: 
- The user can input a string into the search field which will show the user an image of a tattoo suggestion.
- Our API server will be built using Flask_restx

### Endpoints
- All requirements will be handled using endpoints. The main endpoints are:

  -`all_fonts`: serves a list of all tattoo fonts in the database

  -`all_artists`: serves a list of all tattoo artists in the database

  -`all_designs`: serves a list of all designs available in the database  

  -`/design/<name>`: takes a string of the input and returns an image of the design  

  -`/font/<name>`: takes a string as input and returns a visualisation of the font
 
- Other endpoints available, which are mainly for development purposes currently are:

  -`Hello2`: endopoint to see if the server is running 

- Use Agile development to deliver multiple iterations of product to receive feedback
- Use pair programming over Discord to collaborate on each iteration of the code
- For documentation: Swagger, pydoc and  docstrings.
