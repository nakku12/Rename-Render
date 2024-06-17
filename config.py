# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "9439609")

API_HASH = os.environ.get("API_HASH", "3a64962f1face2fc285d0bb72587b139")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6468135188:AAGjLxrOAupH2VrjM9OEbIROorB8tKuyocc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "englishkaaranmain") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Rename")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mithunkrishna:mithun@rename.xcxgov0.mongodb.net/?retryWrites=true&w=majority&appName=Rename")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/c82eb78aa14cfca0890b5.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
