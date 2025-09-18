def get_word_count(book_text):
        word_list = book_text.split()
        return len(word_list)

def get_char_count(book_text):
    lower_case = book_text.lower()
    character_dict = {}
    for character in lower_case:
        # run through each letter and count the occurrences 
        # update the dict every time
        if character in character_dict:
             character_dict[character] += 1
        else:
             character_dict[character] = 1
    return character_dict
#############################################
### Helper function ###
def sort_on(c):
     return c["num"]

def sort_list(char_count):
     # Convert the dictionary into a list of dictionaries, one for each character.
     # Each dictionary will have a 'character' and a 'num' key.
     unsorted_list = []
     for character in char_count:
          unsorted_list.append({"character": character, "num": char_count[character]})

    # Sort the list using the 'num' key in each dictionary.
    # The 'key' argument tells the sort function what value to use for sorting.
    # 'reverse=True' sorts from highest to lowest.
     unsorted_list.sort(reverse=True, key=sort_on)
     return unsorted_list
# Using lambda function
#     unsorted_list.sort(reverse=True, key=lambda d: d["num"])
#     return unsorted_list





                    