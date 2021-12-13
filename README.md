# ta2h3nna
![example workflow](https://github.com/dutchhagelslag/ta2h3nna/actions/workflows/main.yml/badge.svg)
https://ta2h3nna.herokuapp.com/

## Requirements
- Create Request from user input for a tattoo/henna design by type (ie. flower & old school)
- Fetch Designs and display to user as image initially.
- Fetch potential artists with correct specialty.
- Return estimation of price, time consumed, and locations.



## Design
- The user can input a string into the search field which will show the user an image of a tattoo suggestion.:w
- Our API server will be built using Flask_restx
- All requirements will be handled using endpoints. The main endpoints are:

  -`Tattoo`: takes a string of the input and returns an image of the design
  
  -`Tattoofont`: serves tattoo fonts
  
  -`CreateSearchDesign`: creates a search query from the user's input

- Use Agile development to deliver multiple iterations of product to receive feedback
- Use pair programming over Discord to collaborate on each iteration of the code
- For documentation: Swagger, pydoc and  docstrings.
