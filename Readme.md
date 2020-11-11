1. Application Name: Zomato Foodie Chatbot

2. To check the libraries used in creating the application, please refer 'requirements.txt' file in root. 

3. For checking the actions and intents used, please refer 'data\nlu.md' and 'domain.yml' in root. 

4. For going through the conversations implemented for dialogue-flow management please check 'data\stories.md'

5. Trained models are located in 'models' directory located in root. 

6. Conversation Flows: The bot is able to handle generic queries nicely and performs decent on unseen data. 

7. Error Handling: Generic, conversation interpretation by bot and event errors have been handled with the 
   necessary messages. Bot may not work properly with the location synonyms/misspelt names of some of the 'Tier-II' cities.   
   It can be made fully functional by expanding the list of possible synonyms. 
   
8. Email validation has been handled effectively such that mail action isn't performed on invalid inputs.

9. Handled 'No Results Received' scenario with necessary message to the user.

10. Observed a bug in Zomato's 'Search Result Message', in a few scenarios. Faced 'int' and 'str' type comparison error.
    Solution was to convert the 'aggregate_rating' and 'average_cost_for_two' values to float datatype from string.     
