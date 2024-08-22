import random
import requests
import argparse

def get_poem():
    try:
        response = requests.get("https://poetrydb.org/random")
        poem_data = response.json()[0]
        title = poem_data["title"]
        author = poem_data["author"]
        poem_lines = "\n".join(poem_data["lines"])
        return f"**{title}** by *{author}*\n\n{poem_lines}"
    except Exception as e:
        return "Sorry, I couldn't fetch a poem right now."

def main():
    parser = argparse.ArgumentParser(description="Fetch a random poem")
    parser.add_argument("-p", "--poem", action="store_true", help="Fetch a random poem")
    args = parser.parse_args()

    if args.poem:
        print(get_poem())
    else:
        print("Use -p or --poem to fetch a random poem")

if __name__ == "__main__":
    main()
