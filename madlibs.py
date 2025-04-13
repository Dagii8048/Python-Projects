def greeting():
    print("Welcome to the Madlibs game!")
    print("You will be asked to enter a series of words.")
    print("At the end, a story will be generated using your words.")

def get_words():
    words = {}
    words["name"] = input("Enter a name: ")
    words["adjective"] = input("Enter an adjective: ")
    words["verb"] = input("Enter a verb: ") 
    words["noun"] = input("Enter a noun: ")
    return words

def generate_story(words):
    story = f"{words['name']} was a {words['adjective']} person. They loved to {words['verb']} and owned a {words['noun']}."
    return story

def main():
    greeting()
    words = get_words()
    story = generate_story(words)
    print(story)
if __name__ == '__main__':
	main()
