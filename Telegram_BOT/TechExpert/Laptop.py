
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot('6491643059:AAHJBfRK5gy7vk6gDO0acUhAA1lYG69g0TA')

@bot.message_handler(commands=['start'])
def start(message):
    # Create a custom keyboard with a "Category" button and a "Student" button
  keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  keyboard.row(('Laptop'))
  keyboard.row(('coming soon'))
  keyboard.row(('contact us'))
  #keyboard.row(('developer'))
  keyboard.row(('other bots'))
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text =="Laptop")
def laptop_selected(message):
  nest_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest_keyboard.row(('under 30K'))
  nest_keyboard.row(('under 40K'))
  nest_keyboard.row(('under 50K'))
  nest_keyboard.row(('under 60K '))
  nest_keyboard.row(('under 70K'))
  nest_keyboard.row(('under 80K'))
  nest_keyboard.row(('contact for personal recommendation'))
  bot.send_message(message.chat.id, 'xc', reply_markup=nest_keyboard)
@bot.message_handler(func=lambda message: message.text =="under 30K")
def under30k_selected(message):
  nest1_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest1_keyboard.row(('aser aspire Lite'))
  nest1_keyboard.row(('infinix inbook X1 neo'))
  nest1_keyboard.row(('infinix y1 +'))
  nest1_keyboard.row(('infinix x3 slim'))
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')

  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest1_keyboard)
@bot.message_handler(func=lambda message: message.text =="aser aspire Lite")
def aser_aspire_Lite_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'aser aspire Lite')
    bot.send_message(message.chat.id,'8gb 512SSD')
    bot.send_message(message.chat.id,'full HD')
    bot.send_message(message.chat.id,'price = 27,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/3ttnl4s')
@bot.message_handler(func=lambda message: message.text =="infinix inbook X1 neo")
def infinix_inbook_X1_neo_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'infinix inbook X1 neo')
    bot.send_message(message.chat.id,'f')
    bot.send_message(message.chat.id,'8gb 256SSD')
    bot.send_message(message.chat.id,'price = 25,999')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/3LSjRPg')
@bot.message_handler(func=lambda message: message.text =="infinix y1 +")
def infinix_y1__selected(message):
    #image_url='#'
    ##bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'infinix y1 +')
    bot.send_message(message.chat.id,'i3 10 gen')
    bot.send_message(message.chat.id,'8gb 512 SSD')
    bot.send_message(message.chat.id,'price = 29,990')
    bot.send_message(message.chat.id,'https://amzn.to/3ZMQ2FN')
@bot.message_handler(func=lambda message: message.text =="infinix x3 slim")
def infinix_x3_slim_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'infinix x3 slim')
    bot.send_message(message.chat.id,'i3 1215U')
    bot.send_message(message.chat.id,'8g 512SSD')
    bot.send_message(message.chat.id,'FHD screen 100%srgb                                          ----')
    bot.send_message(message.chat.id,'price = ')
    bot.send_message(message.chat.id,'f')
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
    
    
#  '''''''''''''''""""""""""""""""""""""""40K""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@bot.message_handler(func=lambda message: message.text =="under 40K")
def under40k_selected(message):
  nest2_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest2_keyboard.row(('Honour magic book 14'))
  nest2_keyboard.row(('Samsung Galaxy book 2'))
  nest2_keyboard.row(('Asus vivobook 14'))
#   nest1_keyboard.row((''))
#   nest1_keyboard.row((''))
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest2_keyboard)
@bot.message_handler(func=lambda message: message.text =="Honour magic book 14")
def Honour_magic_book_14_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Honour magic book 14')
    bot.send_message(message.chat.id,'ryzen 5500U')
    bot.send_message(message.chat.id,'8gb 512SSD')
    bot.send_message(message.chat.id,'Price = 34,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/3RT86fp')
# @bot.message_handler(func=lambda message: message.text =="Samsung Galaxy book 2")
# def Samsung_Galaxy_book_2_selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'Samsung Galaxy book 2')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'Price =')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
@bot.message_handler(func=lambda message: message.text =="Asus vivobook 14")
def Asus_vivobook_14_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Asus vivobook 14')
    bot.send_message(message.chat.id,' i3-1215U')
    bot.send_message(message.chat.id,'8gb 512')
    bot.send_message(message.chat.id,'Price = 36,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/45gJKPS')
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')

  
#  '''''''''''''''""""""""""""""""""""""""50K""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@bot.message_handler(func=lambda message: message.text =="under 50K")
def under50k_selected(message):
  nest3_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest3_keyboard.row(('Asus vivobook go 15 oled'))
  nest3_keyboard.row(('Lenova ideapad gaming 3'))
  nest3_keyboard.row(('ascer aspire 5'))
  nest3_keyboard.row(('honor magic book x16'))
  #nest1_keyboard.row((''))
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest3_keyboard)
@bot.message_handler(func=lambda message: message.text =="honor magic book x16")
def honor_magic_book_x16_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'honor magic book x16')
    bot.send_message(message.chat.id,'i5 12450H')
    bot.send_message(message.chat.id,'16gb 512SSD')
    bot.send_message(message.chat.id,'FHD screen')
    bot.send_message(message.chat.id,'price = 48,990')
    bot.send_message(message.chat.id,'https://amzn.to/46Cq9KY')
@bot.message_handler(func=lambda message: message.text =="ascer aspire 5")
def ascer_aspire_5_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'ascer aspire 5')
    bot.send_message(message.chat.id,'i5 12gen')
    bot.send_message(message.chat.id,'16 gb 512 ')
    bot.send_message(message.chat.id,'price =49,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/46GTzrc')

@bot.message_handler(func=lambda message: message.text =="Asus vivobook go 15 oled")
def Asus_vivobook_go_15_oled_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Asus vivobook go 15 oled')
    bot.send_message(message.chat.id,'Ryzen 5 7520U')
    bot.send_message(message.chat.id,'8gb 512')
    bot.send_message(message.chat.id,'Price = 44,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/3F718vH')
    
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#  '''''''''''''''""""""""""""""""""""""""60K""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@bot.message_handler(func=lambda message: message.text =="under 60K")
def under60k_selected(message):
  nest4_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(('infinix zerobook 13'))
  nest4_keyboard.row(('asus vivobook filp 14'))
  nest4_keyboard.row(('Asus vivobook s14 intel evo'))
  nest4_keyboard.row(('lenova ideapad gaming 3'))
  nest4_keyboard.row(('xiaomi notebook pro 120G'))
  #nest1_keyboard.row(('hp victus ryzen 5'))
  #   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest4_keyboard)
@bot.message_handler(func=lambda message: message.text =="infinix zerobook 13")
def infinix_zerobook_13_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'infinix zerobook 13')
    bot.send_message(message.chat.id,'i5 13500H')
    bot.send_message(message.chat.id,'16gb 512')
    bot.send_message(message.chat.id,'price = 50,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'price = https://shorturl.at/hnxy9')
@bot.message_handler(func=lambda message: message.text =="asus vivobook filp 14")
def asus_vivobook_filp_14_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'asus vivobook filp 14')
    bot.send_message(message.chat.id,'Ryzen 5 5600H')
    bot.send_message(message.chat.id,'8gb 512')
    bot.send_message(message.chat.id,'price 58,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'f')
@bot.message_handler(func=lambda message: message.text =="Asus vivobook s14 intel evo")
def Asus_vivobook_s14_intel_evo_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Asus vivobook s14 intel evo')
    bot.send_message(message.chat.id,'i5 12500H')
    bot.send_message(message.chat.id,'16gb 512')
    bot.send_message(message.chat.id,'price 58,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'g')
@bot.message_handler(func=lambda message: message.text =="lenova ideapad gaming 3")
def lenova_ideapad_gaming_3_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'lenova ideapad gaming 3')
    bot.send_message(message.chat.id,'Ryzen 5 5600H')
    bot.send_message(message.chat.id,'16gb 512')
    bot.send_message(message.chat.id,'Rtx 3050')
    bot.send_message(message.chat.id,'price = 54,990 ')
    bot.send_message(message.chat.id,'filpkart')
@bot.message_handler(func=lambda message: message.text =="xiaomi notebook pro 120G")
def xiaomi_notebook_pro_120G_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'xiaomi notebook pro 120G')
    bot.send_message(message.chat.id,'i5 12450')
    bot.send_message(message.chat.id,'16gb 512')
    bot.send_message(message.chat.id,'price 59,990')
    #bot.send_message(message.chat.id,'')
    bot.send_message(message.chat.id,'https://amzn.to/3tlcCcq')
# @bot.message_handler(func=lambda message: message.text =="hp victus ryzen 5")
# def hp victus ryzen 5_selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'hp victus ryzen 5')
#     bot.send_message(message.chat.id,'ryzen 5 5600H')
#     bot.send_message(message.chat.id,'16gb 512 ')
#     bot.send_message(message.chat.id,'amd ')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')


#  '''''''''''''''""""""""""""""""""""""""70K""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@bot.message_handler(func=lambda message: message.text =="under 70K")
def under70k_selected(message):
  nest5_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest5_keyboard.row(('Macbook M1 air'))
  nest5_keyboard.row(('Asus vivobook pro 15'))
  nest5_keyboard.row(('Lenova ideapad gaming '))
#   nest1_keyboard.row((''))
#   nest1_keyboard.row((''))
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest5_keyboard)

@bot.message_handler(func=lambda message: message.text =="Macbook M1 air")
def MacbookM1_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Macbook M1 air')
    bot.send_message(message.chat.id,'M1')
    bot.send_message(message.chat.id,'8gb 256')
    bot.send_message(message.chat.id,'Price = 67,990')
    #bot.send_message(message.chat.id,'price=')
    bot.send_message(message.chat.id,'https://amzn.to/3PJfyHn')
@bot.message_handler(func=lambda message: message.text =="Lenova ideapad gaming")
def Lenova_gaming3(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Lenova ideapad gaming')
    bot.send_message(message.chat.id,'ryzen 7 5800H')
    bot.send_message(message.chat.id,'8gb 512')
    bot.send_message(message.chat.id,'Rtx 3050')
    bot.send_message(message.chat.id,'price = 60,990')
    #bot.send_message(message.chat.id,'')
@bot.message_handler(func=lambda message: message.text =="Asus vivobook pro 15")
def Asus_vivobook_pro_15_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Asus vivobook pro 15')
    bot.send_message(message.chat.id,'ryzen 5 5600H')
    bot.send_message(message.chat.id,'16gb 512')
    bot.send_message(message.chat.id,'Rtx 3050')
    bot.send_message(message.chat.id,'Price =66,990')
    bot.send_message(message.chat.id,'https://shorturl.at/iyKV1')
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')


#  '''''''''''''''""""""""""""""""""""""""80K""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@bot.message_handler(func=lambda message: message.text =="under 80K")
def under80k_selected(message):
  nest6_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest6_keyboard.row(('Lenova LOQ '))
  nest6_keyboard.row(('Acer nitro V'))
  nest6_keyboard.row(('Hp Victus'))
#   nest1_keyboard.row((''))
#   nest1_keyboard.row((''))
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
#   bot.send_message(message.chat.id,'')
  bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=nest6_keyboard)
@bot.message_handler(func=lambda message: message.text =="Lenova LOQ")
def Lenova_LOQ_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Lenova LOQ')
    bot.send_message(message.chat.id,'i5 12500H')
    bot.send_message(message.chat.id,'16gb 512SSD ')
    bot.send_message(message.chat.id,'Rtx 3050 6gb Vram')
    bot.send_message(message.chat.id,'price =https://shorturl.at/fhwB4')
    #bot.send_message(message.chat.id,'')
@bot.message_handler(func=lambda message: message.text =="Hp Victus")
def Hp_Victus80_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Hp Victus')
    bot.send_message(message.chat.id,'Ryzen 7 Octa Core 7840HS')
    bot.send_message(message.chat.id,'16gb 512SSD ')
    bot.send_message(message.chat.id,'Rtx 3050 6gb Vram')
    bot.send_message(message.chat.id,'Price =79,990')
    bot.send_message(message.chat.id,'Price = https://shorturl.at/mxDQ0')
@bot.message_handler(func=lambda message: message.text =="Acer nitro V")
def Acer_nitro_V_selected(message):
    #image_url='#'
    #bot.send_photo(message.chat.id,image_url)
    bot.send_message(message.chat.id,'Acer nitro V')
    bot.send_message(message.chat.id,' i5-13420H')
    bot.send_message(message.chat.id,'16gb 512SSD')
    bot.send_message(message.chat.id,'Rtx 4050 6gb Vram')
    bot.send_message(message.chat.id,'price = 72,990 ')
    bot.send_message(message.chat.id,'https://amzn.to/3th8Hx8')
# @bot.message_handler(func=lambda message: message.text =="")
# def _selected(message):
#     #image_url='#'
#     #bot.send_photo(message.chat.id,image_url)
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')
#     #bot.send_message(message.chat.id,'')
#     bot.send_message(message.chat.id,'')

bot.polling()


