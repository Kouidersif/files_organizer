import os
import shutil
import tkinter as tk
import customtkinter as ctk




class App:
    def __init__(self, root):
        self.user_directory = None  # Initialize the directory variable
        self.root = root
        #Frame Customization
        self.root.title("Files Mover")
        self.root.eval("tk::PlaceWindow . center")
        self.root.geometry("1100x580")
        # Setting an H1
        self.label = ctk.CTkLabel(root, text="Organize your working Envirment", font=("Arial", 26, "bold"))
        self.label.grid(row=0, column=15, padx=10, pady=(10))
        #Ask for Directory
        self.button_ask = ctk.CTkButton(root, text="Select Directory", command=self.get_dir)
        self.button_ask.grid(row=1, column=15, padx=10, pady=10)
        # Add some checkbox to get the files' extensions to move
        self.info_label = ctk.CTkLabel(root, text="Choose files you willing to organize")
        self.info_label.grid(row=2, column=15)
        self.select_option1 = ctk.BooleanVar(root)
        self.option_1 = ctk.CTkCheckBox(root, variable=self.select_option1,text="TXT FILES", command=self.get_selected_files)
        self.select_option2 = ctk.BooleanVar(root)
        self.option_2 = ctk.CTkCheckBox(root, variable=self.select_option2,text="CSV FILES", command=self.get_selected_files)
        self.select_option3 = ctk.BooleanVar(root)
        self.option_3 = ctk.CTkCheckBox(root, variable=self.select_option3,text="PDF FILES", command=self.get_selected_files)
        self.select_option4 = ctk.BooleanVar(root)
        self.option_4 = ctk.CTkCheckBox(root, variable=self.select_option4,text="PNG FILES", command=self.get_selected_files)
        self.select_option5 = ctk.BooleanVar(root)
        self.option_5 = ctk.CTkCheckBox(root, variable=self.select_option5,text="JPG FILES", command=self.get_selected_files)
        self.option_1.deselect(), self.option_2.deselect(), self.option_3.deselect(), self.option_4.deselect(), self.option_5.deselect()
        self.cboxes_row = 3
        self.option_1.grid(row=self.cboxes_row, column=0, pady=10, padx=10) 
        self.option_2.grid(row=self.cboxes_row, column=1, pady=10, padx=10)
        self.option_3.grid(row=self.cboxes_row, column=2, pady=10, padx=10)
        self.option_4.grid(row=self.cboxes_row, column=3, pady=10, padx=10)
        self.option_5.grid(row=self.cboxes_row, column=4, pady=10, padx=10)
        #Start work button :
        start_button = ctk.CTkButton(root, text="Move Files", command=self.move_files)
        start_button.grid(row=4, column=15)
        
    def get_selected_files(self):
        mydict = {}
        if self.select_option1.get(): #represents txt
            mydict[".txt"] = "TXT FILES"
        else:
            mydict.pop(".txt", None)

        if self.select_option2.get(): #represents csv
            mydict[".csv"] = "CSV FILES"
        else:
            mydict.pop(".csv", None)

        if self.select_option3.get(): #represents PDF
            mydict[".pdf"] = "PDF FILES"
        else:
            mydict.pop(".pdf", None)

        if self.select_option3.get(): #represents PNG
            mydict[".png"] = "PNG FILES"
        else:
            mydict.pop(".png", None)

        if self.select_option3.get(): #represents JPG
            mydict[".jpg"] = "JPG FILES"
        else:
            mydict.pop(".jpg", None)
        
        return mydict
    #Ask user for directory where all files are located
    def get_dir(self):
        if self.user_directory is None:
            self.user_directory = ctk.filedialog.askdirectory()
        return self.user_directory
    #Start moving files to its directory accordignly
    def move_files(self):
        if self.user_directory is not None:
            user_select = self.get_selected_files()
            self.user_directory = self.get_dir()
            for folder_name in user_select.values():
                folder = os.path.join(self.user_directory, folder_name)
                if not os.path.exists(folder):
                    os.mkdir(folder)
            files_moved = []
            for file in os.listdir(self.user_directory):
                file_path = os.path.join(self.user_directory, file)
                if os.path.isfile(file_path):
                    files_moved.append(file)
                    get_ext = os.path.splitext(file)[1]
                    if get_ext in user_select:
                        dest_folder = os.path.join(self.user_directory, user_select[get_ext])
                        shutil.move(file_path, dest_folder)
            success_label = ctk.CTkLabel(root, text="All Done!, succesfully moved all files")
            success_label.grid(row=5, column=10, pady=10, padx=10)
            return success_label
        


#run
if __name__ == "__main__":
    root = ctk.CTk()
    App(root)
    root.mainloop()

