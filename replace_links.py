import os
import io

# Define the target folder containing the files
target_folder = "."

# Strings to find and replace
old_url = "https://www.sesameasie.com/a-propos"
new_url = "https://www.sesameasie.com/"

# Iterate through files in the repository
for root, _, files in os.walk(target_folder):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with io.open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace the old URL with the new URL
            new_content = content.replace(old_url, new_url)
            
            # Save changes back to the file if replacements were made
            if content != new_content:
                with io.open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print("Modified: " + file_path)
