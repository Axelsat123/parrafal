from config import *
import telebot
import threading
import time 
import requests

bot = telebot.TeleBot(TOKEN)
CHANNEL_NAME = -1001902741533

def fetch_bin_data(bin):
    req = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
    return req

def send_file_lines_to_channel(cc, extra_file, bin_info): 
    with open(cc, "r") as file, open(extra_file, "r") as extra:    
      for line, extra_line in zip(file, extra):
        cc = line.strip()    
        extra_text = extra_line.strip()
         	
        bin = cc[:6]   
        bin_info = fetch_bin_data(bin)
        
        brand = bin_info['brand']
        country = bin_info['country']
        country_name = bin_info['country_name']  
        country_flag = bin_info['country_flag']       
        country_currencies = bin_info['country_currencies']
        bank = bin_info['bank']
        level = bin_info['level']
        typea = bin_info['type']
         
        text = f"""<b>  
╔══════════════════════
╟ ● Yoimiya free scrapp
╟══════════════════════
╟ ● CC: <code>{cc}</code>
╟ ● COUNTRY: {country_name}{country_flag}
╟ ● BANK: {bank} - {typea} - {level}
╟ ● EXTRA: <code>{extra_text}</code>
╟══════════════════════
╟ ● Frank3601
╟══════════════════════
        </b>"""
        
 	    
        bot.send_photo(CHANNEL_NAME, "https://danbooru.donmai.us/posts/5448196", caption=text, parse_mode="html")
        time.sleep(20)
        print(cc)
          
send_file_lines_to_channel("ccs.txt", "extra.txt", fetch_bin_data("your_bin"))

def recibir_msg():
    bot.infinity_polling() 

recibir_msg()