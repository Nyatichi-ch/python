# Create, read, modify, and save a text file
# Define the filename
filename = 'my_file.txt'

#create and write to the file
with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This line contains old_text that will be replaced.\n")
    file.write("Goodbye, World!\n")

# Read the file
with open(filename, 'r') as file:
    lines = file.readlines()

# Modify the content
modified_lines = []
for line in lines:
    if "old_text" in line:
        modified_lines.append(line.replace("old_text", "new_text"))
    else:
        modified_lines.append(line)
    
# Write the modified content back to the file
with open(filename, 'w') as file:
    file.writelines(modified_lines)

print(f"File '{filename}' has been created, modified, and saved.")




# Error handling
try:
    with open('no_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")


    
