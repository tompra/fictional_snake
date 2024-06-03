from rembg import remove
from PIL import Image
import os

def remove_background_img(img_path, outcome_path):
    try:
        if not os.path.isfile(img_path):
            raise FileNotFoundError(f'Input file does not exist: {img_path}')
        
        input_image = Image.open(img_path)
        output_image = remove(input_image)

        os.makedirs(os.path.dirname(outcome_path), exist_ok=True)
        output_image.save(outcome_path)
        print(f'Background removed successfully. Image saved at {outcome_path}')
    except Exception as error:
        print(f'An error occurred: {error}')
    
def main():
    inputUser = input('Enter the path with the file: ').strip()
    inputUserOutcome = input('Enter the path where you want to save the outcome: ').strip()
    
    remove_background_img(inputUser, inputUserOutcome)
    
if __name__ == '__main__':
    main()