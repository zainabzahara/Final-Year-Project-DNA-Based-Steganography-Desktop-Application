import sys
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
import requests
import time

sys.setrecursionlimit(3000)
np.set_printoptions(threshold=sys.maxsize)


class DNAImageSteganography:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("DNA Based Steganography")

        self.setup_gui()
        self.img = None
        self.fln = None
        self.fln3 = None

    def setup_gui(self):
        Tops = tk.Frame(self.root, width=1600, relief=tk.RAISED)
        Tops.pack(side=tk.TOP)

        f1 = tk.Frame(self.root, width=800, height=700, relief=tk.RAISED)
        f1.pack(side=tk.LEFT)

        lblInfo = tk.Label(Tops, font=('helvetica', 30, 'bold'), text="FYP Basic GUI", fg="Black", bd=10, anchor='w')
        lblInfo.grid(row=0, column=0)

        self.Msg = tk.StringVar()
        self.ExMsg = tk.StringVar()

        lblMsg = tk.Label(f1, font=('arial', 16, 'bold'), text="MESSAGE", bd=16, anchor="w")
        lblMsg.grid(row=0, column=0)

        self.txtMsg = tk.Entry(f1, font=('arial', 16, 'bold'), textvariable=self.Msg, bd=10, insertwidth=4, bg="powder blue", justify='right')
        self.txtMsg.grid(row=0, column=1)

        lblExMsg = tk.Label(f1, font=('arial', 16, 'bold'), text="Decoded Message-", bd=16, anchor="w")
        lblExMsg.grid(row=2, column=0)

        self.txtExMsg = tk.Entry(f1, font=('arial', 16, 'bold'), textvariable=self.ExMsg, bd=10, insertwidth=4, bg="powder blue", justify='right')
        self.txtExMsg.grid(row=2, column=1)

        self.lbl = tk.Label(f1)
        self.lbl.grid(row=0, column=2, columnspan=2)

        btnEncode = tk.Button(f1, padx=8, pady=4, bd=16, fg="black", font=('arial', 16, 'bold'), width=7, text="Encode", bg="powder blue", command=self.encode)
        btnEncode.grid(row=3, column=1)

        btnDecode = tk.Button(f1, padx=8, pady=4, bd=16, fg="black", font=('arial', 16, 'bold'), width=7, text="Decode", bg="powder blue", command=self.decode)
        btnDecode.grid(row=4, column=1)

        btnExit = tk.Button(f1, padx=8, pady=4, bd=16, fg="black", font=('arial', 16, 'bold'), width=7, text="Exit", bg="red", command=self.root.quit)
        btnExit.grid(row=4, column=0)

        btnImgBrowser = tk.Button(f1, padx=8, pady=4, bd=16, fg="black", font=('arial', 16, 'bold'), width=7, text="Browser", bg="powder blue", command=self.show_image)
        btnImgBrowser.grid(row=3, column=2)

        btnShare = tk.Button(f1, padx=8, pady=4, bd=16, fg="black", font=('arial', 16, 'bold'), width=7, text="Share", bg="powder blue", command=self.share)
        btnShare.grid(row=4, column=2)

    def show_image(self):
        self.fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
        if self.fln:
            self.img = Image.open(self.fln)
            img1 = self.img.copy()
            img1.thumbnail((150, 150))
            img1 = ImageTk.PhotoImage(img1)
            self.lbl.configure(image=img1)
            self.lbl.image = img1

    def encode(self):
        if not self.img:
            print("No image selected")
            return

        start = time.time()
        message = self.txtMsg.get()
        binary_str = ''.join(format(x, '08b') for x in bytearray(message, 'utf-8'))
        binary_list = [binary_str[i: i + 2] for i in range(0, len(binary_str), 2)]
        DNA_encoding = {"00": "A", "01": "G", "10": "C", "11": "T"}

        DNA_list = [DNA_encoding[num] for num in binary_list]
        DNA_encoded_msg = "".join(DNA_list) + "$t3g0"
        b_message = ''.join([format(ord(i), "08b") for i in DNA_encoded_msg])

        _format = self.img.format.lower()
        if _format != 'png':
            fln1 = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('Image (.png file)', '.png')])
            self.img.save(fln1)
            self.img = Image.open(fln1)

        converted_img = self.img.convert('RGBA')
        width, height = converted_img.size
        array = np.array(list(converted_img.getdata()))

        n = 4
        total_pixels = array.size // n
        req_pixels = len(b_message)

        if req_pixels > total_pixels:
            print("ERROR: Need larger file size")
            return

        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), converted_img.mode)
        self.fln3 = filedialog.asksaveasfile(filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")), defaultextension=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
        if self.fln3:
            enc_img.save(self.fln3.name)
        print("time taken is:", time.time() - start)

    def decode(self):
        if not self.img:
            print("No image selected")
            return

        start = time.time()
        array = np.array(list(self.img.getdata()))
        n = 4
        total_pixels = array.size // n

        hidden_DNA_bits = ''.join([bin(array[p][q])[2:][-1] for p in range(total_pixels) for q in range(0, 3)])
        hidden_DNA_bits = [hidden_DNA_bits[i:i + 8] for i in range(0, len(hidden_DNA_bits), 8)]

        DNA_str = ""
        for i in range(len(hidden_DNA_bits)):
            if DNA_str[-5:] == "$t3g0":
                break
            else:
                DNA_str += chr(int(hidden_DNA_bits[i], 2))

        if "$t3g0" in DNA_str:
            DNA_str = DNA_str[:-5]
        else:
            print("No Hidden Message Found")
            return

        DNA_decoding = {'A': '00', 'G': '01', 'C': '10', 'T': '11'}
        bin_converted_msg = "".join([DNA_decoding[num] for num in DNA_str])

        results_of_ExMsg = bytes([int(bin_converted_msg[i*8:i*8+8], 2) for i in range(len(bin_converted_msg) // 8)]).decode('utf-8')
        self.ExMsg.set(results_of_ExMsg)
        print("time taken is:", time.time() - start)

    def share(self):
        link = "http://192.168.18.97:5000/"
        webbrowser.open(link)
        try:
            myinput = {'email': 'mymail@gmail.com', 'pass': 'mypaass'}
            response = requests.post(link, data=myinput)
            print(response)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    app = DNAImageSteganography(root)
    root.mainloop()
