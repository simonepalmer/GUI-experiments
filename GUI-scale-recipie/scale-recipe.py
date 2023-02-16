import re # Regualar expressions
import gi # Gtk

gi.require_version("Gtk", "3.0") 
from gi.repository import Gtk

# I am aware that best practices is to keep GUI in a seperate
# class but I'm a dumb dumb so I just want to figure out how
# to do the actuall task first. Then I can make it look neat.

""" GUI stuff """
def build_gui():

    builder = Gtk.Builder()
    builder.add_from_file("scale.ui")

    window = builder.get_object("window")
    window.show_all()
    window.connect("destroy", Gtk.main_quit)

    Gtk.main()

""" Buttons things """
def on_close_clicked(clicked):
    Gtk.main_quit()

def on_apply_clicked(clicked):
    pass

""" Functions to do the business """
def update_numbers_in_string(input_string, ratio):

    # I have noticed recipies have characters like "½ & ¾" in them
    # sometimes so I should probably build in something that checks
    # for these to replace with 0.5 and 0.75. Not decided if doing
    # in it the same bit as the rest or if trying to sanitize the
    # string beforehand

    numbers = re.findall(r'\d+\.\d+|\d+', input_string)

    updated_numbers = []
    for num in numbers:
        if '.' in num:
            updated_numbers.append(str(float(num) * ratio))
        else:
            updated_numbers.append(str(int(num) * ratio))

    print(numbers)
    print(updated_numbers)

    # I'm keeping both versions right now until I can come along
    # with further testing to know which one, if any, is better

    """ Split with re """
    words = re.findall(r'\b\w+\b|\d+\.\d+|\d+', input_string)

    output_words = []
    for word in words:
        if any(char.isdigit() for char in word):
            for i in range(len(numbers)):
                if numbers[i] in word:
                    word = word.replace(numbers[i], updated_numbers[i])
                    break
        output_words.append(word)

    """ Split with python split """
    # words = input_string.split()
    #
    # output_words = []
    # for word in words:
    #     if any(char.isdigit() for char in word):
    #         for i in range(len(numbers)):
    #             if numbers[i] in word:
    #                 word = word.replace(numbers[i], updated_numbers[i])
    #                 break
    #     output_words.append(word)

    output_string = " ".join(output_words)
    return output_string
    
def take_input_string():
    # Will have a textbox to paste the recipe into
    # until then I will have this to test
    input_string = "a 1  b 2  c 3  d 4  e 1.5  f 2.5  g 0.5  h 0.25"
    return input_string

def give_output(input_string, output_string):
    print("done")

def main():
    build_gui()

    # These will all be run by on_apply_clicked() later
    input_string = take_input_string()
    ratio = 1.5 # Will be decided by radio buttons
    output_string = update_numbers_in_string(input_string, ratio)
    give_output(input_string, output_string)

if __name__ == "__main__":
    main()