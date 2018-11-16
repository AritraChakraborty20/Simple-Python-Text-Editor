import sys, os

v = sys.version

if "2.7" in v:
	from Tkinter import *
	import tkFileDialog
elif "3" in v:
	from tkinter import *
	from tkinter import filedialog

root = Tk()
root.title("Text Editor")
text = Text(root)
text.grid()
lsum = Label(root, text = 'Out put:')
lsum.grid(column=0, sticky=W, pady=4)


def saveas():
	global text,save
	t = text.get("1.0", "end-1c")
	save = filedialog.asksaveasfilename()
	file1 = open(save, "w+")
	file1.write(t)
	file1.close()
def run():
	global save
	code = "python3 "
	lsum["text"] = "" + str((os.popen(code+save).read()))

button = Button(root, text = "Save", command = saveas)
run = Button(root, text = "RUN", command = run)
button.grid()
run.grid()
root.mainloop()
