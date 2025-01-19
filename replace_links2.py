import os
import io
import re

# Define the target folder containing the files
target_folder = "."

# URLs to remove the hyperlink
remove_links = [
    "https://www.sesameasie.com/episodes/categories/entrepreneurs",
    "https://www.sesameasie.com/episodes/categories/intrapreneurs",
    "https://www.sesameasie.com/episodes/categories/les-plus-%C3%A9cout%C3%A9s",
    "https://www.sesameasie.com/episodes/categories/hong-kong",
    "https://www.sesameasie.com/episodes/categories/chine",
    "https://www.sesameasie.com/episodes/categories/japon"
]

# Base URL to replace
replace_post_links = "https://www.sesameasie.com/post"
replace_with = "https://www.sesameasie.com"

# Iterate through files in the repository
for root, _, files in os.walk(target_folder):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Open the file and read its content
            with io.open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content  # Keep track of the original content

            # Remove hyperlinks for specific URLs but keep the text
            for url in remove_links:
                # Match <a> tags with the specific URL
                content = re.sub(
                    r'<a[^>]+href=["\']%s["\'][^>]*>(.*?)</a>' % re.escape(url),
                    r'\1',
                    content
                )

            # Replace links containing "https://www.sesameasie.com/post"
            content = re.sub(
                r'<a[^>]+href=["\'](https://www\.sesameasie\.com/post[^"\']*)["\'][^>]*>(.*?)</a>',
                r'<a href="%s">\2</a>' % replace_with,
                content
            )

            # Write back the modified content if changes were made
            if content != original_content:
                with io.open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print("Modified: " + file_path)
