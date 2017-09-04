# Moving on with Exceptions


# Let's wrap our previous code in a function
def count_words(filename):
    """ Count the approximate number of words in a file."""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        """ failing silently """
        pass
    else:
        # Count the approximate number of words in the file
        words = contents.strip()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = "resources/chapter_10/alice.txt"
count_words(filename)

# Working with multiple files
filenames = ['alice.txt', 'shubham.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words("resources/chapter_10/" + filename)
