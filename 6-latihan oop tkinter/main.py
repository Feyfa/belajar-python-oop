import tkinter

main_window = tkinter.Tk()

# di python kalo saat akses ke suatu object yang huruf pertama nya besar, itu adalah class
label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")
tombol1 = tkinter.Button(main_window, text="tombol1")

# di python kalo saat akses ke suatu object yang huruf pertama nya kecil, itu adalah method
# method positioning
label1.pack()
label2.pack()
tombol1.pack()

# method untuk menampilkan GUI
main_window.mainloop()