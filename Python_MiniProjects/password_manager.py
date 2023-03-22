import Fernet from cryptography.fernet 

pwd = input("What is the master password? ")

def view():
   with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

def add():
   name = input('Account Name: ')
   pwd = input("Password: ")

   with open('passwords.txt', 'a') as f:
      f.write(name + " | " + pwd + "\n")
      # /n puts things on the next line in the file
      # every account and password combo is on the next line

   # file = open('passwords.txt', 'a')
 # with this format ^, without the with keyword, you have to manually close the file after opening it with file.close()
    # which will mess up your Python process
    # 'a' is a mode to open the file in
# there are different modes like 'a', 'w', 'r'
  # 'w' means overwrite the file, it will clear the file it opens and resave it
 # 'r' is read mode, where you can't edit or do anything
 # 'a' is append mode, you can add something to the file
    



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) )")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
      print("Invalid mode.")
      continue