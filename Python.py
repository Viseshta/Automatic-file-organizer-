import os
import shutil    #provides high level file operations
import tkinter as tk     #gui
from tkinter import filedialog,messagebox


#define file types in form of dictionary
filetypes={
    'Images':['.jpg','.jpeg','.png','.gif'],
    'Videos':['.mp4','.mkv','.mpg'],
    'Music':['.mp3','.wav'],
    'Documents':['.pdf','.docx','.txt','.ppt'],
    'Programs':['.exe']
}


def organize_files():                      #fumction whuch runs to organize file
    folder_path=folder_selected.get()      #get selected folder
    if not folder_path:
        messagebox.showwarning('Warning','Please select a folder first.')
        return
    status_label.config(text='Organizing files....Please wait!')
    root.update()
    try:
      count=0
      for file in os.listdir(folder_path):    #get all files in the folder
             file_path=os.path.join(folder_path,file)
             if os.path.isfile(file_path):
                ext=os.path.splitext(file)[1].lower()
                if ext in ['.jpg','.png','.jpeg','.gif']:
                 new_folder=os.path.join(folder_path,'Images')
                elif ext in ['.pdf','.txt','.doc','.docx','.ppt']:
                  new_folder=os.path.join(folder_path,'Documents')
                elif ext in ['.mp3','.wav']:
                  new_folder=os.path.join(folder_path,'Music')
                elif ext in ['.mp4','.mkv','.mpg']:
                  new_folder=os.path.join(folder_path,'Videos')
                elif ext in ['.exe']:
                  new_folder=os.path.join(folder_path,'Programs')
                else:
                    new_folder=os.path.join(folder_path,'Others')
                print(file,'->',ext)
                if not os.path.exists(new_folder):
                  os.makedirs(new_folder)
                shutil.move(file_path,os.path.join(new_folder,file))
                count+=1
      status_label.config(text='Oranizing completed')
      messagebox.showinfo('Done',f'{count} files organized successfully!')
    except Exception as e:
       messagebox.showerror('Error',str(e))
       status_label.config(text='')


# to select folder
def browsefolder():
    path=filedialog.askdirectory()
    folder_selected.set(path)


#GUI
root=tk.Tk()
root.title('File organizer')
root.geometry('600x400')
folder_selected=tk.StringVar()
status_label=tk.Label(root,text='',font=('Ariel',11))
status_label.pack(pady=10)

label=tk.Label(root,text='Select Folder to Organize',font=('Ariel',14))
label.pack(pady=12)
entry=tk.Entry(root,textvariable=folder_selected,width=45)
entry.pack(pady=5)
browse_button=tk.Button(root,text='Browse',command=browsefolder)
browse_button.pack(pady=5)
organize_button=tk.Button(root,text='Organize Files',command=organize_files,bg='green',fg='white')
organize_button.pack(pady=20)

root.mainloop()
