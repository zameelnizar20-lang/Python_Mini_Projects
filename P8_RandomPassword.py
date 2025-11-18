#Random Password Generator Mini Project
import string , random
password = ""


for pw in range(1,10):
    rand = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password = password+rand
print(password)




