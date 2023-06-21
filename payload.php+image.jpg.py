
print('''
 ▄▄▄     ▓██   ██▓ ███▄ ▄███▓▓█████  ███▄    █ 
▒████▄    ▒██  ██▒▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ 
▒██  ▀█▄   ▒██ ██░▓██    ▓██░▒███   ▓██  ▀█ ██▒
░██▄▄▄▄██  ░ ▐██▓░▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒
 ▓█   ▓██▒ ░ ██▒▓░▒██▒   ░██▒░▒████▒▒██░   ▓██░
 ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ 
  ▒   ▒▒ ░▓██ ░▒░ ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░
  ░   ▒   ▒ ▒ ░░  ░      ░      ░      ░   ░ ░ 
      ░  ░░ ░            ░      ░  ░         ░ 
          ░ ░                                  
                      [injection tool ]                   
          Facebook:https://www.facebook.com/profile.php?id=100067567612149 ''')
 
from PIL import Image

jpg_path = input("path image  JPG: ")
php_code = input("path payloadـ PHP: ")

image = Image.open(jpg_path)

php_bytes = php_code.encode()

image.info["PHP"] = php_bytes

output_path = "injected.jpg"
image.save(output_path)

print("The injection was successful  JPG!")

output_path = "injected.jpg"
image.save(output_path)

print("The injection was successful  JPG!")

 

