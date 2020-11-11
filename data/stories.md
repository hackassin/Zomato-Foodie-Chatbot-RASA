## interactive_story_3
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location

## interactive_story_4
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location

## interactive_story_5
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}

## interactive_story_6
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location

## interactive_story_7
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Pa Pa Ya\nLocation - A-3, Select Citywalk, District Centre, Saket, New Delhi\nAverage Cost For Two People: 2500\nZomato User Rating: 4.9\n\nRestaurant-2:\n------------------------------\nName - Honk - Pullman New Delhi Aerocity\nLocation - Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi\nAverage Cost For Two People: 2500\nZomato User Rating: 4.6\n\nRestaurant-3:\n------------------------------\nName - Plum By Bent Chair\nLocation - Ground Floor, Worldmark 2, Aerocity, New Delhi\nAverage Cost For Two People: 2200\nZomato User Rating: 4.6\n\nRestaurant-4:\n------------------------------\nName - Ziu\nLocation - Ground Floor, Sangam Courtyard, Major Somnath Marg, Sector 9, R K Puram, New Delhi\nAverage Cost For Two People: 2900\nZomato User Rating: 4.5\n\nRestaurant-5:\n------------------------------\nName - Master Koii's\nLocation - Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon\nAverage Cost For Two People: 1900\nZomato User Rating: 4.5\n\nRestaurant-6:\n------------------------------\nName - You Mee\nLocation - M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi\nAverage Cost For Two People: 1000\nZomato User Rating: 4.5\n\nRestaurant-7:\n------------------------------\nName - C.I.A. Call It Asiian\nLocation - 13 - 16, Narmada Shopping Complex, Alaknanda Road, Near Don Bosco School, Greater Kailash 2 (GK 2), New Delhi\nAverage Cost For Two People: 700\nZomato User Rating: 4.4\n\nRestaurant-8:\n------------------------------\nName - House of Ming - The Taj Mahal Hotel\nLocation - The Taj Mahal Hotel, 1, Mansingh Road, New Delhi\nAverage Cost For Two People: 5500\nZomato User Rating: 4.3\n\nRestaurant-9:\n------------------------------\nName - Chi Ni - The Roseate\nLocation - 21st Milestone, Samalkha, NH-8, Kapashera, New Delhi\nAverage Cost For Two People: 5000\nZomato User Rating: 4.3\n\nRestaurant-10:\n------------------------------\nName - Boa Village\nLocation - 13, Alipur Road, Civil Lines, New Delhi\nAverage Cost For Two People: 2300\nZomato User Rating: 4.3\n\n"}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_8
* restaurant_search{"cuisine": "North Indian", "location": "Ahmedabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Ahmedabad"}
    - action_chk_location
    - slot{"location": "Ahmedabad"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_9
* restaurant_search{"cuisine": "Italian", "location": "Bengaluru"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Bengaluru"}
    - action_chk_location
    - slot{"location": "Bengaluru"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_10
* restaurant_search{"cuisine": "North Indian", "location": "Chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Chennai"}
    - action_chk_location
    - slot{"location": "Chennai"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_11
* restaurant_search{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_12
* restaurant_search{"cuisine": "North Indian", "location": "Hyderabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Hyderabad"}
    - action_chk_location
    - slot{"location": "Hyderabad"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_13
* restaurant_search{"cuisine": "Chinese", "location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - slot{"location": "Kolkata"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_14
* restaurant_search{"cuisine": "South Indian", "location": "Mumbai"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - slot{"location": "Mumbai"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_15
* restaurant_search{"cuisine": "North Indian", "location": "Pune"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Pune"}
    - action_chk_location
    - slot{"location": "Pune"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_16
* restaurant_search{"cuisine": "Mexican", "location": "Agra"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Agra"}
    - action_chk_location
    - slot{"location": "Agra"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_17
* restaurant_search{"cuisine": "American", "location": "Ajmer"}
    - slot{"cuisine": "American"}
    - slot{"location": "Ajmer"}
    - action_chk_location
    - slot{"location": "Ajmer"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_18
* restaurant_search{"cuisine": "Italian", "location": "Aligarh"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Aligarh"}
    - action_chk_location
    - slot{"location": "Aligarh"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_19
* restaurant_search{"cuisine": "American", "location": "Amravati"}
    - slot{"cuisine": "American"}
    - slot{"location": "Amravati"}
    - action_chk_location
    - slot{"location": "Amravati"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_20
* restaurant_search{"cuisine": "Chinese", "location": "Amritsar"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Amritsar"}
    - action_chk_location
    - slot{"location": "Amritsar"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_21
* restaurant_search{"cuisine": "South Indian", "location": "Asansol"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Asansol"}
    - action_chk_location
    - slot{"location": "Asansol"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_22
* restaurant_search{"cuisine": "American", "location": "Aurangabad"}
    - slot{"cuisine": "American"}
    - slot{"location": "Aurangabad"}
    - action_chk_location
    - slot{"location": "Aurangabad"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_23
* restaurant_search{"cuisine": "South Indian", "location": "Bareilly"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Bareilly"}
    - action_chk_location
    - slot{"location": "Bareilly"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_24
* restaurant_search{"cuisine": "Italian", "location": "Belgaum"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Belgaum"}
    - action_chk_location
    - slot{"location": "Belgaum"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye


## interactive_story_25
* restaurant_search{"cuisine": "North Indian", "location": "Bhavnagar"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Bhavnagar"}
    - action_chk_location
    - slot{"location": "Bhavnagar"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_26
* restaurant_search{"cuisine": "North Indian", "location": "Vellore"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Vellore"}
    - action_chk_location
    - slot{"location": "Vellore"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_27
* restaurant_search{"cuisine": "North Indian", "location": "Dindigul"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Dindigul"}
    - action_chk_location
    - slot{"location": "Dindigul"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye    
    
## interactive_story_28
* restaurant_search{"cuisine": "North Indian", "location": "Warangal"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Warangal"}
    - action_chk_location
    - slot{"location": "Warangal"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye      
    
## interactive_story_29
* restaurant_search{"cuisine": "North Indian", "location": "Visakhapatnam"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Visakhapatnam"}
    - action_chk_location
    - slot{"location": "Visakhapatnam"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    
## interactive_story_30
* restaurant_search{"cuisine": "North Indian", "location": "Visakhapatnam"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Visakhapatnam"}
    - action_chk_location
    - slot{"location": "Visakhapatnam"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_31
* restaurant_search{"cuisine": "North Indian", "location": "Karnal"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Karnal"}
    - action_chk_location
    - slot{"location": "Karnal"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye 

## interactive_story_32
* restaurant_search{"cuisine": "North Indian", "location": "Purulia"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Purulia"}
    - action_chk_location
    - slot{"location": "Purulia"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye      
    
## interactive_story_33
* restaurant_search{"cuisine": "North Indian", "location": "Hamirpur"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Hamirpur"}
    - action_chk_location
    - slot{"location": "Hamirpur"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_34
* restaurant_search{"cuisine": "North Indian", "location": "Shimla"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Shimla"}
    - action_chk_location
    - slot{"location": "Shimla"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye                                

## interactive_story_36
* restaurant_search{"cuisine": "North Indian", "location": "Shimla"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Shimla"}
    - action_chk_location
    - slot{"location": "Shimla"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_37
* restaurant_search{"cuisine": "North Indian", "location": "Thanjavur"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Thanjavur"}
    - action_chk_location
    - slot{"location": "Thanjavur"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": ""}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Chinese", "location": "ladakh"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "ladakh"}
    - action_chk_location
    - followup{"name": "utter_ask_location"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_chk_location
    - slot{"location": "bengaluru"}
    - followup{"name": "utter_ask_cuisine"}    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Chianti\nLocation - 960, 12th Main, HAL 2nd Stage, Indiranagar, Bangalore\nAverage Cost For Two People: 2000\nZomato User Rating: 4.8\n\nRestaurant-2:\n------------------------------\nName - Truffles\nLocation - 28, 4th B Cross, Koramangala 5th Block, Bangalore\nAverage Cost For Two People: 900\nZomato User Rating: 4.8\n\nRestaurant-3:\n------------------------------\nName - Windmills Craftworks\nLocation - 331, EPIP Area, Road 5B, Near KTPO, Whitefield, Bangalore\nAverage Cost For Two People: 2500\nZomato User Rating: 4.7\n\nRestaurant-4:\n------------------------------\nName - Caperberry\nLocation - 203, 2nd Floor, UB City, 24 Vittal Mallya Road, Lavelle Road, Bangalore\nAverage Cost For Two People: 2200\nZomato User Rating: 4.7\n\nRestaurant-5:\n------------------------------\nName - Burma Burma\nLocation - 607, Ground Floor, 12th Main, Hal 2nd Stage, Indiranagar, Bangalore\nAverage Cost For Two People: 1500\nZomato User Rating: 4.7\n\nRestaurant-6:\n------------------------------\nName - Communiti\nLocation - 67 & 68, Brigade Solitaire, Opposite Advaith Hyundai, Residency Road, Bangalore\nAverage Cost For Two People: 1500\nZomato User Rating: 4.7\n\nRestaurant-7:\n------------------------------\nName - AB's - Absolute Barbecues\nLocation - 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore\nAverage Cost For Two People: 1300\nZomato User Rating: 4.7\n\nRestaurant-8:\n------------------------------\nName - AB's - Absolute Barbecues\nLocation - 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore\nAverage Cost For Two People: 1300\nZomato User Rating: 4.7\n\nRestaurant-9:\n------------------------------\nName - JW Kitchen - JW Marriott Bengaluru\nLocation - JW Marriott, 24/1, Vittal Mallya Road, Lavelle Road, Bangalore\nAverage Cost For Two People: 2200\nZomato User Rating: 4.6\n\nRestaurant-10:\n------------------------------\nName - Brahma Brews\nLocation - Opposite Brigade Palm Springs, 24th Main, 7th Phase, JP Nagar, Bangalore\nAverage Cost For Two People: 1900\nZomato User Rating: 4.6\n\n"}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_chk_location
    - slot{"location": null}
    - followup{"name": "utter_ask_location"}
    - utter_ask_location
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - action_chk_location
    - slot{"location": "Bhubaneswar"}
    - followup{"name": "utter_ask_cuisine"}    
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Silver Streak\nLocation - Ground Floor, BMC Bhawani Mall, Sahid Nagar, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.3\n\nRestaurant-2:\n------------------------------\nName - Taste Of China\nLocation - 139, District Center, Chandrasekharpur, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.3\n\nRestaurant-3:\n------------------------------\nName - Upre Kitchen & Cafe\nLocation - 3rd Floor, G-51, Near IOCL Office, Chandrasekharpur, Bhubaneshwar\nAverage Cost For Two People: 600\nZomato User Rating: 4.2\n\nRestaurant-4:\n------------------------------\nName - Taste Of China\nLocation - 142, Near Water Tank Lane, Bapuji Nagar, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.2\n\nRestaurant-5:\n------------------------------\nName - Adda Unplugged\nLocation - 3rd Floor,MRLA Complex,Patia,Bhubaneswar,751024\nAverage Cost For Two People: 500\nZomato User Rating: 4.2\n\nRestaurant-6:\n------------------------------\nName - Adda Unplugged\nLocation - Above Reliance Fresh, Near ITER College, Jagmohan Nagar, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.2\n\nRestaurant-7:\n------------------------------\nName - The China Hut\nLocation - C-38, Saheed Nagar, 3rd Floor, Opp BMC Bhawani Mall, Bhubaneswar\nAverage Cost For Two People: 600\nZomato User Rating: 4.1\n\nRestaurant-8:\n------------------------------\nName - TCD Restaurant & Banquet\nLocation - Plot 324, District Center, Niladri Vihar Road, Chandrasekharpur, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.1\n\nRestaurant-9:\n------------------------------\nName - 99 North Restaurant\nLocation - 36A, Chandaka Industrial Estate, Near infocity Road, Patia, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.1\n\nRestaurant-10:\n------------------------------\nName - Grand Kalinga\nLocation - 321, District Centre, Below SBI Bank, Niladri Vihar Road, Chandrasekharpur, Bhubaneshwar\nAverage Cost For Two People: 500\nZomato User Rating: 4.1\n\n"}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - followup{"name": "utter_ask_cuisine"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Barbeque Nation\nLocation - K1, RDB Boulevard, Block EP - GP, Sector 5, Salt Lake, Kolkata\nAverage Cost For Two People: 1800\nZomato User Rating: 4.9\n\nRestaurant-2:\n------------------------------\nName - The Grid\nLocation - 86A, Haute Street, Corporate Park, Topsia Road (South), Topsia, Kolkata\nAverage Cost For Two People: 2000\nZomato User Rating: 4.7\n\nRestaurant-3:\n------------------------------\nName - Barbeque Nation\nLocation - 1st Floor, 24, Park Center Building, Park Street Area, Kolkata\nAverage Cost For Two People: 1800\nZomato User Rating: 4.6\n\nRestaurant-4:\n------------------------------\nName - India Restaurant\nLocation - 34, Karl Marx Sarani, Kidderpore, Kolkata\nAverage Cost For Two People: 800\nZomato User Rating: 4.6\n\nRestaurant-5:\n------------------------------\nName - Hard Rock Cafe\nLocation - 57, Park Mansion, Near Reliance Digital, Park Street Area, Kolkata\nAverage Cost For Two People: 2500\nZomato User Rating: 4.5\n\nRestaurant-6:\n------------------------------\nName - Asia Kitchen By Mainland China\nLocation - Shop 1858/1, 4th Floor, Acropolis Mall, Rajdanga Main Road, Kasba, Kolkata\nAverage Cost For Two People: 2000\nZomato User Rating: 4.5\n\nRestaurant-7:\n------------------------------\nName - Oh! Calcutta\nLocation - 10/3, 4th Floor, Forum Mall, Elgin Road, Elgin, Kolkata\nAverage Cost For Two People: 1800\nZomato User Rating: 4.5\n\nRestaurant-8:\n------------------------------\nName - Tamara - Pipal Tree Hotel\nLocation - PRGM-AS/465, Hatiara, Major Arterial Road, New Town, Kolkata\nAverage Cost For Two People: 1800\nZomato User Rating: 4.5\n\nRestaurant-9:\n------------------------------\nName - Chili's Grill & Bar\nLocation - 375, 2nd Floor, South City Mall, Prince Anwar Shah Road, Kolkata\nAverage Cost For Two People: 1200\nZomato User Rating: 4.5\n\nRestaurant-10:\n------------------------------\nName - Chili's Grill & Bar\nLocation - 1858, Acropolis Mall, Rajdanga Main Road, Kasba, Kolkata\nAverage Cost For Two People: 1200\nZomato User Rating: 4.5\n\n"}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - followup{"name": "utter_ask_cuisine"}

## interactive_story_2
* restaurant_search{"cuisine": "North Indian", "location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - slot{"location": "Kolkata"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - 6 Ballygunge Place\nLocation - 6, Ballygunge Place, Ballygunge, Kolkata\nAverage Cost For Two People: 500\nZomato User Rating: 4.5\n\nRestaurant-2:\n------------------------------\nName - Zam Zam\nLocation - 28/A, Syed Amir Ali Avenue, Park Circus Area, Kolkata\nAverage Cost For Two People: 700\nZomato User Rating: 4.4\n\nRestaurant-3:\n------------------------------\nName - My Big Fat Belly\nLocation - 22, Sarat Bose Road, Sreepally, Bhawanipur, Kolkata\nAverage Cost For Two People: 600\nZomato User Rating: 4.4\n\nRestaurant-4:\n------------------------------\nName - The Chaiwala\nLocation - 6/1/2, Graham's Land, N.S.C Bose Road, Tollygunge, Kolkata\nAverage Cost For Two People: 500\nZomato User Rating: 4.4\n\nRestaurant-5:\n------------------------------\nName - Dada Boudi Restaurant\nLocation - 12/10, S.N. Bannerjee Road, Barrackpore, Kolkata\nAverage Cost For Two People: 600\nZomato User Rating: 4.3\n\nRestaurant-6:\n------------------------------\nName - Hanglaatherium\nLocation - 188/3/1A, Lake Gardens, Prince Anwar Shah Road, Kolkata\nAverage Cost For Two People: 600\nZomato User Rating: 4.3\n\nRestaurant-7:\n------------------------------\nName - Royal Indian Hotel\nLocation - 147, Rabindra Sarani, Bara Bazar, Kolkata\nAverage Cost For Two People: 550\nZomato User Rating: 4.3\n\nRestaurant-8:\n------------------------------\nName - Aminia\nLocation - 62, S.N. Banerjee Road, Near Great Eastern Showroom, Barrackpore, Kolkata\nAverage Cost For Two People: 700\nZomato User Rating: 4.2\n\nRestaurant-9:\n------------------------------\nName - Hondo's\nLocation - 58/100, Prince Anwar Shah Road, Kolkata\nAverage Cost For Two People: 700\nZomato User Rating: 4.2\n\nRestaurant-10:\n------------------------------\nName - Blue Mug\nLocation - 1/121, Jodhpur Park, Kolkata\nAverage Cost For Two People: 650\nZomato User Rating: 4.2\n\n"}
    - utter_email
* email_confirmation
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_chk_location
    - followup{"name": "utter_ask_location"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - followup{"name": "utter_ask_cuisine"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Hotel Ram Ashraya\nLocation - Bhandarkar Road, Matunga East, Mumbai\nAverage Cost For Two People: 200\nZomato User Rating: 4.9\n\nRestaurant-2:\n------------------------------\nName - Cafe Madras\nLocation - 38 B, Circle House, King's Circle Near Maheshwari Udyan, Matunga East, Mumbai\nAverage Cost For Two People: 250\nZomato User Rating: 4.8\n\nRestaurant-3:\n------------------------------\nName - Guru Kripa\nLocation - 40, Guru Kripa Building, Road 24, Near SIES College, Sion, Mumbai\nAverage Cost For Two People: 300\nZomato User Rating: 4.5\n\nRestaurant-4:\n------------------------------\nName - Pancham Puriwala\nLocation - 8-10, Perin Nariman Street, Fort, Mumbai\nAverage Cost For Two People: 300\nZomato User Rating: 4.2\n\nRestaurant-5:\n------------------------------\nName - Sardar Pav bhaji\nLocation - Tardeo Road Junction, Opposite Bus Depot, Tardeo, Mumbai\nAverage Cost For Two People: 250\nZomato User Rating: 4.0\n\n"}
    - utter_email
* email_confirmation{"email": "amnverma51@gmail.com"}
    - slot{"email": "amnverma51@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_search_restaurants
    - slot{"email_response": "Restaurant-1:\n------------------------------\nName - Amrit Sweets\nLocation - SCF 78, Phase 5, Mohali\nAverage Cost For Two People: 500\nZomato User Rating: 4.2\n\nRestaurant-2:\n------------------------------\nName - Anupam Sweets\nLocation - SCO 25, Sector 11, Panchkula\nAverage Cost For Two People: 500\nZomato User Rating: 4.2\n\nRestaurant-3:\n------------------------------\nName - Katani Dhaba\nLocation - SCF 40, B2, Phase 3, Mohali\nAverage Cost For Two People: 450\nZomato User Rating: 4.2\n\nRestaurant-4:\n------------------------------\nName - Toshib Fast Food\nLocation - Booth 48, Sector 34 C, Near Sector 34, Chandigarh\nAverage Cost For Two People: 700\nZomato User Rating: 4.1\n\nRestaurant-5:\n------------------------------\nName - O Chicken India -  Oil Free Healthy Chicken\nLocation - Bay Shop 15, Sector 18 D, Near Sector 18, Chandigarh\nAverage Cost For Two People: 700\nZomato User Rating: 4.1\n\nRestaurant-6:\n------------------------------\nName - Raju Chinese Fast Food 23\nLocation - Booth 75, Sector 23-C, Sector 23, Chandigarh\nAverage Cost For Two People: 600\nZomato User Rating: 4.1\n\nRestaurant-7:\n------------------------------\nName - Gopal's\nLocation - Sunny Enclave, Sector 125, Kharar Road, Mohali\nAverage Cost For Two People: 500\nZomato User Rating: 4.1\n\nRestaurant-8:\n------------------------------\nName - Kumar Rasoi\nLocation - Shop 206, Sector 37, Chandigarh\nAverage Cost For Two People: 450\nZomato User Rating: 4.1\n\nRestaurant-9:\n------------------------------\nName - Khalsa Dhaba\nLocation - SCF 81, Phase 5, Mohali\nAverage Cost For Two People: 400\nZomato User Rating: 4.1\n\nRestaurant-10:\n------------------------------\nName - Mad Over Chinese\nLocation - SCO 41, Sector 21 C, Near Sector 21, Chandigarh\nAverage Cost For Two People: 350\nZomato User Rating: 4.1\n\n"}
    - utter_email
* email_confirmation{"email": "amlan.ultimate@gmail.com"}
    - slot{"email": "amlan.ultimate@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
