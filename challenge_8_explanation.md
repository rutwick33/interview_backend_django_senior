## Challenge 8
If you have cloned the repo and have got it up and running, skip to the 'Explanation' section of the file. Else, continue with the Setup.

### Setup
1. Ensure that you have Docker Desktop installed on your computer
2. Set up a python environment using Python 3.10
3. Create a virtual environment, add the folder to your .gitignore, and activate the virtual environment
4. Install the requirements in the requirements.txt file
5. Use the docker compose file to set up a local postgres database
6. Migrate your data and start the server
7. Populate the db with test data by running the database.py file
8. Check localhost URLs to confirm the working of the project

### Explanation - Adding and item to Inventory through the API
#### Method 1 - Through the web app directly
1. Copy the base inventory URL in your browser window - https://localhost:8000/inventory/
2. Click on the 'Options' button
3. Scroll to the bottom section of the page
4. Enter the details of the inventory item including the necessary metadata
5. If using the form enter the fields accordingly.
6. If using the input box, select the media type as application/json and paste the necessary data
    Example:
    {"id":21,"name":"The Good, Bad, and Ugly","type":{"id":3,"name":"Version"},"language":{"id":1,"name":"Abkhaz"},"tags":[{"id":1,"name":"Action","is_active":true}],"metadata":{"year":1919,"actors":["Laurence Fishburne","Carrie-Anne Moss"],"imdb_rating":8.7,"rotten_tomatoes_rating":87}}
7. POST the data
