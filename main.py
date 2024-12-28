import os 

def generate_files():
    os.makedirs("generated_files", exist_ok=True)
    for i in range(1, 4):
        file_name = f"generated_files/file{i}.txt"
        with open(file_name, "w") as f:
            f.write(f"This is file {i}\n")
        print(f"Generated: {file_name}")

if __name__ == "__main__": 
    generate_files() 