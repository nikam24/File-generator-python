import os 
import shutil 

def cleanup_files():
    dir_name = "generated_files" 
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print(f"Deleted: {dir_name}")
    else:
        print(f"{dir_name} does not exist.")

if __name__ == "__main__":
    cleanup_files() 