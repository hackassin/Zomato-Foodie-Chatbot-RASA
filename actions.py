from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import re
import smtplib
import sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from rasa_sdk import Action
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import zomatopy
import json

# Action Class to implement location validation
class ActionCheckLocation(Action):

    def name(self):
        return 'action_chk_location'

    def run(self, dispatcher, tracker, domain):
        try:
            loc = tracker.get_slot('location')
            print("Location = ", loc)
            cuisine = tracker.get_slot('cuisine')
            print("Cuisine=",cuisine)
            synonym = [{'Ahmadabad': 'Ahmedabad'}, {'Ahmdbd': 'Ahmedabad'}, {'Ahmdbad': 'Ahmedabad'},
                       {'Bangalore': 'Bengaluru'}, {'Bnglr': 'Bengaluru'},
                       {'Bnglor': 'Bengaluru'},
                       {'Madras': 'Chennai'}, {'Chn': 'Chennai'}, {'Chenai': 'Chennai'}, {'Dilli': 'Delhi'},
                       {'Dehli': 'Delhi'},
                       {'Deli': 'Delhi'}, {'Hydrbd': 'Hyderabad'},
                       {'Klkta': 'Kolkata'},{'Calcutta': 'Kolkata'}, {'Calcuta': 'Kolkata'}, {'Bombay': 'Mumbai'},
                       {'Poona': 'Pune'}, {'Puna': 'Pune'},
                       {'Pona': 'Pune'}]

            cities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
                      'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
                      'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
                      'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Dindigul',
                      'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
                      'Guwahati', 'Gwalior', 'Hubli-Dharwad','Hamirpur', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar',
                      'Jammu','Jamnagar', 'Karnal',
                      'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam', 'Kolhapur',
                      'Kollam', 'Purulia',
                      'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura',
                      'Mangalore',
                      'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad',
                      'Patna', 'Shimla',
                      'Pondicherry', 'Prayagraj', 'Allahabad', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem',
                      'Sangli',
                      'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur',
                      'Tiruchirappalli', 'Thanjavur',
                      'Tirunelveli', 'Tiruppur', 'Ujjain', 'Bijapur','Bilaspur', 'Vadodara', 'Varanasi', 'Vasai-Virar City',
                      'Vijayawada', 'Vellore', 'Warangal', 'Vishakhapatnam']
            cities_lower = [x.lower() for x in cities]
            flag = 0
            for item in synonym:
                if loc.lower() in list(item.keys())[0].lower():
                    print("Location is a synonym",item)
                    loc = item[loc]
                    flag = 1
                    break
                if loc.lower() in cities_lower:
                    print("Location found in cities\n")
                    flag = 1
                    break

            """if (flag == 0):
                print("Location might be misspelt")
                dispatcher.utter_message("Location might be misspelt\nLet's restart our conversation")
                return [FollowupAction(name="utter_ask_location")]"""

            if flag == 0:
            #if loc.lower() not in cities_lower:
                print("Sorry, we don’t operate in this city")
                dispatcher.utter_message("Sorry, we don’t operate in this city. Please enter location again")
                loc = None
                return [SlotSet('location', loc), FollowupAction(name="utter_ask_location")]

            if cuisine == None:
                return [SlotSet('location', loc), FollowupAction(name="utter_ask_cuisine")]

            return [SlotSet('location', loc), FollowupAction(name='utter_ask_price')]

        except Exception as e:
            dispatcher.utter_message("I don't recognize your inputs and still "
                                     "learning to converse like humans. I am restarting the conversation"
                                     " for you.\nLet's try again ^_^")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(" kindly check %s---> %s, %s, %s", e,
                  exc_type, tb[2], tb[1])

            print(e)
            return [Restarted()]

# Action Class to implement restaurant search
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def sort_results(self, data, price):
        print("Inside sort_results(): Price = ", price)
        data_list = data['restaurants']
        if (price[1] is not None):
            price_filtered_dict = [d for d in data_list if
                                   (float(d['restaurant']['average_cost_for_two']) <= float(price[1])) and
                                   (float(d['restaurant']['average_cost_for_two']) > price[0])]
        else:
            price_filtered_dict = [d for d in data_list if (float(d['restaurant']['average_cost_for_two']) >= price[0])]
        final_sorted_data = sorted(price_filtered_dict,
                                   key=lambda i: (float(i['restaurant']['user_rating']['aggregate_rating']),
                                                  float(i['restaurant']['average_cost_for_two'])), reverse=True)
        data.update({'restaurants': final_sorted_data})

        return data

    def run(self, dispatcher, tracker, domain):
        try:
            response = ""
            email_response = ""
            config = {"user_key": "b5d4e905a3ad91733f95dc0652aef040"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            print("Location is: ", loc)
            cuisine = tracker.get_slot('cuisine')

            price_val = {'less than 300': [0, 300],
                         '300 to 700': [300, 700],
                         'more than 700': [700, None]}

            price = price_val[tracker.get_slot('price')]
            location_detail = zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
            cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                             'south indian': 85, 'american': 1, 'mexican': 73}

            results = {}
            for i in range(0, 100, 20):
                results_temp = zomato.restaurant_search_all("", lat, lon, str(cuisines_dict.get(cuisine)), limit=100,
                                                            start=i)
                temp_dict = json.loads(results_temp)
                print("No. of restaurants fetched from the list of restaurants: ", len(temp_dict['restaurants']),
                      "For Batch: ", i)
                if not bool(results):
                    # if there is no results initialized , then initialize with first response
                    results = temp_dict
                    continue
                if len(temp_dict['restaurants']) < 20:
                    results['restaurants'].extend(temp_dict['restaurants'])
                    break
                results['restaurants'].extend(temp_dict['restaurants'])
            d = results
            # results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
            # d = json.loads(results)

            print("No. of restaurants fetched: ", len(d['restaurants']))
            print("Testing", d)
            d = self.sort_results(d, price)
            print("\nSorted_Results: ", d)
            if len(d['restaurants']) == 0:
                response = "No results found as per your requirements. Maybe enter different requirements"
                email_response = "No results found"
                dispatcher.utter_message("-----" + response)
                return [FollowupAction('utter_ask_cuisine'), FollowupAction('utter_ask_price')]
            else:
                # for restaurant in d['restaurants']:
                # 	response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
                for i, restaurant in enumerate(d['restaurants'][:10]):
                    if i < 5:
                        response = response + str(i + 1) + ". " + restaurant['restaurant']['name'] + " in " + \
                                   restaurant['restaurant']['location']['address'] + \
                                   " has been rated " + str(
                            restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n\n"
                    email_response = email_response + "Restaurant-" + str(i + 1) + ":\n------------------------------\n" + \
                                     "Name - " + restaurant['restaurant']['name'] + "\n" + \
                                     "Location - " + restaurant['restaurant']['location']['address'] + \
                                     "\nAverage Cost For Two People: " + str(
                        restaurant['restaurant']['average_cost_for_two']) + \
                                     "\nZomato User Rating: " + str(
                        restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n\n"

            dispatcher.utter_message("-------------------------------------------------------------------\n\n" + response)
            email_resp = email_response
            # return [SlotSet('location',loc)]
            return [SlotSet('email_response', email_resp)]
        except Exception as e:
            dispatcher.utter_message("I don't recognize your inputs and still "
                                     "learning to converse like humans. I am restarting the conversation"
                                     " for you.\nLet's try again ^_^")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(" kindly check %s---> %s, %s, %s", e,
                  exc_type, tb[2], tb[1])

            print(e)
            return [Restarted()]

# Action Class to send email to user
class ActionSendEmail(Action):

    def name(self):
        return 'action_send_email'

    def valid_email(self, email):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

    email_config = {
        "from": "foodie.upgradbot@gmail.com",
        "password": "26102020Q"
    }

    def run(self, dispatcher, tracker, domain):
        from_user = self.email_config['from']
        to_user = tracker.get_slot('email')
        print("Email-ID: ",to_user)

        if (to_user is None):
            dispatcher.utter_message('Alright. No email :). Ending this session. '
                                     'Let me start a new session for you')
            return [SlotSet('email_response', None), SlotSet('location', None),
                    SlotSet('cuisine', None), SlotSet('price', None),
                    SlotSet('email', None), Restarted()]

        #if self.valid_email(to_user):
        else:
            print("User email address: ", to_user)
            password = self.email_config['password']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_user, password)
            subject = 'Your request on the Restaurant Enquiry'
            msg = MIMEMultipart()
            msg['From'] = from_user
            msg['TO'] = to_user
            msg['Subject'] = subject
            body = tracker.get_slot('email_response')
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server.sendmail(from_user, to_user, text)
            dispatcher.utter_message("Email sent :). Goodbye. I am done for the day. "
                                     "Another bot will assist you further :)")
            server.close()
            return [SlotSet('email_response', None),SlotSet('location', None),
                    SlotSet('cuisine', None), SlotSet('price', None),
                    SlotSet('email', None),Restarted()]
