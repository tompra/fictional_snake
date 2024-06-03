from rembg import remove
from PIL import Image

def remove_background_img(img_path, outcome_path):
    try:
        input_image = Image.open(img_path)
        output_image = remove(input_image)
        output_image.save(outcome_path)
        print(f'Background removed successfully. Image saved at {outcome_path}')
    except Exception as error:
        print(f'An error occurred: {error}')
    
def main():
    inputUser = input('Enter the path with the file: ')
    inputUserOutcome = input('Enter the path where you want to save the outcome: ')
    
    remove_background_img(inputUser, inputUserOutcome)
    
if __name__ == '__main__':
    main()