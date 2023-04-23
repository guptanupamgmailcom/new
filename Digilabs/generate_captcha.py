import random
def generate_captcha():
    """
    Function to generate a 5-digit CAPTCHA
    """
    captcha = ''
    for i in range(5):
        captcha = captcha + str(random.randint(0,9)) # below is the short form of this line
        #captcha += str(random.randint(0, 9))
    return captcha
print(generate_captcha())
print(generate_captcha())
print(generate_captcha())
print(generate_captcha())