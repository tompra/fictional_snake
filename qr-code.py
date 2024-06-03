import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr(data, name_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'/Users/tom/desktop/qr-code/{name_file}.png')
    print(f'QR Code generated and saved as as "{name_file}.png"')

def decode_qr(image_path):
    img = Image.open(image_path)
    result = decode(img)
    
    if result:
        for qr_code in result:
            print(f'Decoded data: {qr_code.data.decode('utf-8')}')
    else:
        print('No QR code found.')
        
def main():
    while True:
        user_choice = input("Generate a QR Code for a website (1) or a email address (2). Enter 1 or 2: ")
        if user_choice == '1':
            data = input('Enter the website URL: ')
            name_file = input('Enter the name of the file: ')
            if data.startswith('http://') or data.startswith('https://'):
                generate_qr(data, name_file)
                break
            else:
                print("Invalid URL. Please include 'http://' or 'https://' at the beginning.")
        elif user_choice == '2':
            data = input('Enter the email address: ')
            name_file = input('Enter the name of the file: ')
            if "@" in data and "." in data and '.com' in data:
                generate_qr(f"mailto:{data}", name_file)
            else:
                print("Invalid email address. Please enter a valid email.")
        else:
            print('Invalid choice. Please enter 1 or 2.')

    decode_qr(f'/Users/tom/desktop/qr-code/{name_file}.png')
    
if __name__ == '__main__':
    main()