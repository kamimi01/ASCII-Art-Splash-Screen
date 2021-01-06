import random
import os
i = random.randrange(9) + 1 
website="https://raw.githubusercontent.com/kamimi01/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
