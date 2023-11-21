import urllib.parse

# Read the URL-encoded file
with open('links.tsv', 'r', encoding='utf-8') as file:
    encoded_content = file.read()

# Decode the URL-encoded content
decoded_content = urllib.parse.unquote(encoded_content)

# Write the decoded content to a new .tsv file
with open('decoded_links.tsv', 'w', encoding='utf-8') as new_file:
    new_file.write(decoded_content)