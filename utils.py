import wikipediaapi
import os

def save_wikipedia_page(topic, folder="wikipedia_pages"):
    # Initialize Wikipedia API
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='your-user-agent', language='en')
    
    # Get the page content
    page = wiki_wiki.page(topic)
    
    if not page.exists():
        print(f"Page '{topic}' does not exist on Wikipedia.")
        return

    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)

    # Define the markdown file path
    file_path = os.path.join(folder, f"{topic.replace(' ', '_')}.md")

    # Convert content to markdown-style text
    content = f"# {page.title}\n\n{page.text}"

    # Save as a markdown file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved '{topic}' to {file_path}")

# Example: Save "Hedge fund" Wikipedia page as a Markdown file
save_wikipedia_page("Walleye Capital")
