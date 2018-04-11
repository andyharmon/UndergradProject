from DoClassification import do_classification
from datetime import datetime
import Tkinter as tk
from tkFileDialog import askopenfilename

root = tk.Tk()
root.withdraw()

data_file_name = askopenfilename(title="Select data File")

try:
    do_classification(data_file_name)
    print(str(datetime.now().time()) + ": done")
except IOError:
    print(str(datetime.now().time()) + ": error on filenames, are you sure they are valid filenames?")

