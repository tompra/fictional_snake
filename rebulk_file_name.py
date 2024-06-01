import os

def rename_files(path, name):  
    try:
        if not path.endswith('/'):
            path += '/'
            
        files = os.listdir(path)
        if not files:
            print(f"No files found the directory: {path}")
            return
        
        for i, fileName in enumerate(files):
            file_extension = os.path.splitext(fileName)[1]
            new_name = f"{name}{i}{file_extension}"
            old_path = os.path.join(path, fileName)
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {fileName} to {new_name}")
        
        print('Renaming completed')
        
    except Exception as error:
        print(f'An error occurred: {error}')
        
def main():
    path = input('Enter the path to the directory: ')
    name = input('Enter the name for the files: ')
    
    rename_files(path, name)

if __name__ == '__main__':
    main()