import os

def search_files(directory, query):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

# Example usage
search_query = input("Enter your_search_query: ")
search_directory = r"C:\Users\Mude\Desktop\collage"

found_files = search_files(search_directory, search_query)

if found_files:
    print("Files found:")
    for file_path in found_files:
        print(file_path)
else:
    print("No matching files found.")
