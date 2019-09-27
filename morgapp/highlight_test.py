"""
Syntax Highlight
"""

import tkinter as tk

import tkinter.font as tkFont

myfont = tkFont.Font(family="Helvetica", size=12)


def color_text(edit, tag, word, fg_color="white", bg_color="#282c34"):
    # add a space to the end of the word
    word = word + " "
    edit.insert("end", word)
    end_index = edit.index("end")
    begin_index = "%s-%sc" % (end_index, len(word) + 1)
    edit.tag_add(tag, begin_index, end_index)
    edit.tag_config(tag, foreground=fg_color, background=bg_color)


root = tk.Tk()
root.geometry("600x200")

edit = tk.Text(root)
edit.config(background="#282c34", font=myfont)
edit.pack()

text = "Up the hill went Jack and Jill, down fell Jill and cried!"
# create a list of single words
word_list = text.split()
# print( word_list )  # test

# pick word to be colored
myword1 = "Jack"
myword2 = "Jill"
# create a list of unique tags
tags = ["tg" + str(k) for k in range(len(word_list))]
for ix, word in enumerate(word_list):
    # word[:len(myword)] for word ending with a punctuation mark
    if word[: len(myword1)] == myword1:
        color_text(edit, tags[ix], word, "blue")
    elif word[: len(myword2)] == myword2:
        color_text(edit, tags[ix], word, "red", "yellow")
    else:
        color_text(edit, tags[ix], word)

root.mainloop()
