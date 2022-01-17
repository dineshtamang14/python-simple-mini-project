import string
from random import *


value = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(value) for x in range(randint(8, 16)))
print(f"\n Your New Strong Password is: {password}")
