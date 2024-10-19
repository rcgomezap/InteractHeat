# InterHeat
#### Video demo: https://youtu.be/fOuBrLGixGc 
#### Description:
Interactive solution of the steady heat transfer equation using a web application based on Flask. The page has a 2D case of heat transport in a plate. The user sets the temperatures in the four boundaries, aswell the lenght of the plate, thermal conductivity and heat generation rate. When user clicks on calculate, a the frontend communicate with the API, which uses the finite difference method for solving the heat equation. Backend returns a JSON file and the results are plotted using Plotly.js.