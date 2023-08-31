from captcha.image import ImageCaptcha
from PIL import Image

# define generation of captcha text
def generate_captcha_text(length=6):
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
