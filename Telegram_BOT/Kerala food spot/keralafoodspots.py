import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

bot=telebot.TeleBot('6523829599:AAG4c_vHccsSBxXqyiWBggh4Dz-ux5XEjbM')

#define a dictionary to keep track of user states
user_states = {}

@bot.message_handler(commands= ['start'])
def start(message):
    #create keyboard just below the message section in telegram 
    #replyKeyboardMarkup object represents a custom keyboard markup
    #resize_keyboard=true sets the resize_keyboard option to True. This tells Telegram to
    #resize the keyboard to fit the width of the screen
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    #create a button using a variable
    #The KeyboardButton object represents a button that can be displayed on a keyboard. The button can have a text label, an image, or both. The button can also have a 
    # callback function that is executed when the button is pressed.
    kozhikode_district_button =KeyboardButton("Kozhikode")
     # Add "Back" and "Main Menu" buttons
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")
    #row() method is a useful way to organize buttons on a keyboard. 
    # It allows you to group related buttons together
    keyboard.row(kozhikode_district_button)

    bot.send_message(message.chat.id, 'Welcome to my keral food spots bot!', reply_markup=keyboard)

    # Set the user's initial state to the main menu
    user_states[message.chat.id] = "main_menu"
'''
@bot.message_handler(func=lambda message: message.text == "Back")
def back_button_clicked(message):
    chat_id = message.chat.id
    
    if chat_id in user_states:
        current_state = user_states[chat_id]
        
        # Handle "Back" button based on the user's current state
        if current_state == "category_selected":
            # User was in the "travel brochure" section, go back to the main menu
            start(message)
        # Add more cases for other states as needed
        
        # Update the user's current state
        user_states[chat_id] = current_state
'''
@bot.message_handler(func=lambda message: message.text == "Main Menu")
def main_menu_button_clicked(message):
    # Handle the "Main Menu" button click by sending the main menu again
    start(message)
'''
@bot.message_handler(func=lambda message: message.text =="Kozhikode")
def kozhikode_district_button_selected(message):
    nest_keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    kozhikode_taluk_button =KeyboardButton("Kozhikode.")
    #Koyilandy_taluk_button =KeyboardButton("Koyilandy ")
    #Vatakara_taluk_button =KeyboardButton("Vatakara")
    #Thamarassery_taluk_button =KeyboardButton("Thamarassery")
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")

    nest_keyboard.row(kozhikode_taluk_button)
    nest_keyboard.row(Koyilandy_taluk_button)
    nest_keyboard.row(Vatakara_taluk_button)
    nest_keyboard.row(Thamarassery_taluk_button)
    nest_keyboard.row(back_button)
    nest_keyboard.row(main_menu_button)

    bot.send_message(message.chat.id, 'Please select a taluk:', reply_markup=nest_keyboard)

    # Update the user's current state to category_selected
    user_states[message.chat.id] = "category_selected"
'''    

@bot.message_handler(func=lambda message: message.text == "Kozhikode")
def kozhikode_district_buttonselected(message):
    nest2_keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    special_offerNow_button=KeyboardButton("special offer now")
    famous_spot_button =KeyboardButton("famous spots")
    unlimited_dailyFood_button =KeyboardButton("unlimited & daily food spot")
    snacks_juice_button=KeyboardButton("Snacks & juice")
    vegetarians_button=KeyboardButton("Vegetarian Restaurants")
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")

    nest2_keyboard.row(special_offerNow_button)
    nest2_keyboard.row(famous_spot_button)
    nest2_keyboard.row(unlimited_dailyFood_button)
    nest2_keyboard.row(snacks_juice_button)
    nest2_keyboard.row(vegetarians_button)
    nest2_keyboard.row( back_button)
    nest2_keyboard.row( main_menu_button)

    bot.send_message(message.chat.id, 'welcome to kozhikode taluk',reply_markup=nest2_keyboard)

    user_states[message.chat.id] ="Kozhikode_selected"

@bot.message_handler(func=lambda message: message.text == "famous spots")
def famous_spot_button_selected(message):
    nest3_keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    paragon_button=KeyboardButton("Paragon Restaurant")
    rahmath_button=KeyboardButton("Rahmath hotel")
    champion_button=KeyboardButton("champion Restaurant")
    edele_button=KeyboardButton("Edele Hotel")

    kuttichira_button=KeyboardButton("Kuttichira Biriyani Center")
    nahdi_kuzhi_mandi_button=KeyboardButton("Nahdi Kuzhi Mandi")
    amma_button=KeyboardButton("Amma Hotel")
    ambika_button=KeyboardButton("Ambika Hotel")
    #_button=KeyboardButton("")

    nest3_keyboard.row(paragon_button)
    nest3_keyboard.row(rahmath_button)
    nest3_keyboard.row(champion_button)
    nest3_keyboard.row(edele_button)
    nest3_keyboard.row( kuttichira_button)
    nest3_keyboard.row(nahdi_kuzhi_mandi_button)
    nest3_keyboard.row(amma_button)
    nest3_keyboard.row(ambika_button)

    bot.send_message(message.chat.id, 'Here are some famous spots in Kozhikode Taluk:', reply_markup=nest3_keyboard)

    user_states[message.chat.id] = "famous_spot_button_selected"  

@bot.message_handler(func=lambda message: message.text == "Paragon Restaurant")
def paragon_button_selected(message):
    # Send an image of Kappad Beach
    photo_url = 'https://images.newindianexpress.com/uploads/user/imagelibrary/2023/7/14/w900X450/At_the_Paragon.jpg?w=400&dpr=2.6' 
    bot.send_photo(message.chat.id, photo_url)
    
    # Send a description of Kappad Beachm
    description = """ 11 most legendenry hotel in the world Best sea food I've eaten in a long time. It's a tiny place that draws a large crowd but the fish fry is to die for.
    If you're in Kozhikode, you shouldn't miss this place."""
    bot.send_message(message.chat.id, description)
    
    #can use it to send a youtube vido
    youtube_video_url = 'https://youtu.be/89HMJ4KU7VA?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    # You can also provide additional information or options for the user here.

    gmap_link='https://goo.gl/maps/CeSjXT87rkGWwA9c8'
    bot.send_message(message.chat.id,gmap_link)

   
    
    # Update the user's current state (optional)
    #user_states[message.chat.id] = "paragon_button_selected"   
'''
@bot.message_handler(func=lambda message: message.text == "Rahmath Restaurant")
def  rahmath_button_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """One of the great Food destination for the passionate food lovers. They are present in two locations in Kozhikode. One near 2nd Date and One at Stadium Junction, Puthiyara Road. The hotel at Stadium Junction is spread over 4 Floors, Second and Third floor provides AC dining and Premium AC dining respectively.
They serve variety of dishes, their Beef Biriyani and other Beef dishes are famous among whole of Kerala. The food is awesome. And the service is also amazing.
They have enough parking and the staff are well behaved.
One of the Famous Food destinations in Kerala
                    -sreejyothi p p"""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/X53j85xnx3tFgQxW9'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/QlRCxFULGxs?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Champion Restaurant")
def  champion_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """Champion restaurant is the ultimate destination for beef lovers. It’s a small
    but cozy place near the historic Kuttichira and Mosques, with fast and friendly staff. The Malabar style beef dishes
    here are mouth-watering and live up to the hype.This is not a place for luxury dining, but a place for authentic and satisfying
    local cuisine. Limited seating only and Lil congested. Parking can be a challenge, so plan accordingly"""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/RhYmMSxvwEZMpq8L9'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/mmvi-pFtVYA?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  


@bot.message_handler(func=lambda message: message.text == "Edele Hotel")
def edele_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """Edele - One of the legendary spots in calicut known for their breakfast combos. I was asked to try their pazhampori with 
    signature beef fry combo. With mixed emotions, I tried it and boom 🔥It was so delicious & added parotta as well. The chaiya was average.
     Overall - good place with affordable price. The place has limited seating only. If you’re in calicut - do try them out."""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/7mHXyzDDvaRbBnAZ9'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/8qXK99edVqQ?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Kuttichira Biriyani Center")
def kuttichira_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """One of the best biriyanis of Kozhikkode.
We have tried beef biriyani,and Chicken Biriyani.
All of the items were so amazing and lipsmacking. Rice to Masala qauntity was awesome and was very perfect. Moving on to beef, it is topped at all beef biriyanis which i had so far, the qaulity of the beef was very nice super tender and very so
ft as in chicken chicken rice have a great flavour and rice to masala proportion was great. It is a good option for those dont like spicy food.
Moving on to the last, but not the least. Beef Guntur, the most spiciest and amazingly delicious among sides.   As i was a spicy food lover i liked beef guntur with ghee rice than beef stew.
All the items we had was very delicious, aromatic and was great in their quantities as well. The Price for all the items was reasonable and price to quantity proportion was great.
Parking will be mess as this is situated on side of a narrow road, but there is a pay and park option nearby. All together a wonderful experience
                     -mohammed aslam"""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/2rDAnGthxqvTT9ws9'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/KbQ0ticwwuY?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Nahadi Kuzhi Mandi")
def nahdi_kuzhi_mandi_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """We tried Alfaham kuzhimandi, the taste was amazing. We ordered half Mandi which was sufficient for 3 people.  Taste, service 
    and ambience are good. Definitely worth a visit when you are in Kozhikode."""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/3gMSk7nnq2PYTZJ57'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/J8Zha4Lx67Q?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Amma Hotel")
def amma_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """Best sea food I've eaten in a long time. It's a tiny place that draws a large crowd but the fish fry is to die for.
     If you're in Kozhikode, you shouldn't miss this place. In fact I'd go as far as to say miss everything else for this place.
    I had the king fish which I generally prefer. It was cooked really well and the rice and the curries they gave along with it were really 
    good too.
                                  -Rohit """
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/ZyY3BEeEYrmvSmrG6'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/mWsMXOkBxtc?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Ambika Hotel")
def ambika_button_selected(message):
    
    photo_url = ''
    bot.send_photo(message.chat.id, photo_url)
    
    description = """Best place in calicut for seafood dishes. They are providing good fresh fish, I had avoly fry and prawns fry especially the avoly fry masala is superb. Apart from seafood, the meals is  just an ordinary one. Most of
     them are coming with their families for having fish. During lunch time place is little bit over crowded. Ac as well as non ac rooms 
     are there.
                                 -rejith"""
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/NeamkRL9nbmstb6H7'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = 'https://youtu.be/1QhSfE7JvbA?feature=shared' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  


#from here on we start daily & budget friendly hotels
@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  
#from here we start snacks and juice
@bot.message_handler(func=lambda message: message.text == "Alikka Juicekada")
def alikka_juice_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ This is an amazing Juice Shop, will make you wonder. Juices are so tasty and we tried all the varieties and made 
    three visits in two days'stays.Drinks are so refreshing and  I wonder how they serve this at just Rs:20/- without compromising quality 
    and quantity. """
    bot.send_message(message.chat.id, description)

    gmap_location_link='https://goo.gl/maps/yCLNEgjY6F6Dr4oo9 '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Sangeeth Coolbar")
def sangeeth_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ The ice cream shop exceeded my expectations with its wide variety of flavors and exceptional quality. The creamy texture and delightful taste left me craving for more. The friendly staff and inviting ambiance added to the overall enjoyable experience. A must-visit destination for all ice cream enthusiasts!
Rather Than all the falooda in the menu, normal falooda is Awesome"""
    bot.send_message(message.chat.id, description)

    gmap_location_link=' https://goo.gl/maps/LddiUEheZaMcUBK39'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Jaffer’s Soya Fry")
def jaffer_soya_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """If you are hungry, you have a craving for non-vegetarians,but you are tensed about that and the prices, go to this shop...🏃. You will get the protein rich dry soybean masala ✨ it was amazing, even would be confused whether it is
     non veg or not. Don't over expect atmosphere and hygiene. Just normal.but the taste and price is amazing. We get 100g at only
      30 rupees.try it """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' https://goo.gl/maps/55j1XMMTFWXrz2Rg7'
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "Ganesh Fruit Stall & Juices")
def ganesh_juice_button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

 @bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""     

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  


@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  
       
@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

@bot.message_handler(func=lambda message: message.text == "")
def _button_selected(message):
    
    photo_url = '' 
    bot.send_photo(message.chat.id, photo_url)
    
    description = """ """
    bot.send_message(message.chat.id, description)

    gmap_location_link=' '
    bot.send_message(message.chat.id,gmap_location_link)
    
    youtube_video_url = '' 
    bot.send_message(message.chat.id, youtube_video_url)
    #user_states[message.chat.id] = ""  

'''
if __name__ == "__main__":
    bot.polling()

