import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import socket
import time

# Set up the OLED display
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()
disp.clear()
disp.display()

# Create a blank image for drawing.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "No IP"
    return ip

while True:
    # Clear the display
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get IP address
    ip_address = get_ip_address()
    draw.text((0, 0), "IP Address:", font=font, fill=255)
    draw.text((0, 15), ip_address, font=font, fill=255)

    # Display image
    disp.image(image)
    disp.display()

    # Wait a bit before updating
    time.sleep(10)