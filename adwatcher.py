import pyautogui
import time
import glob
import customtkinter as ctk

def adWatcher():
    button.configure(state="disabled")
    slider.configure(state="disabled")
    region = pyautogui.getWindowsWithTitle('BlueStacks App Player 1')
    bluestacks_window = [region[
        0].left,region[0].top,region[0].width,region[0].height]
    ads_number=int(number.cget("text"))
    crosses = glob.glob("./cross_images/cross*.png")
    for i in range(ads_number):
        time.sleep(1)
        print("Starting Ad...")
        playad_location = pyautogui.locateOnScreen("playAd.png", region=(bluestacks_window),confidence=0.8)
        if playad_location is not None:
            pyautogui.click(playad_location)
            print("Ad is playing..")
            region = pyautogui.getWindowsWithTitle('BlueStacks App Player 1')
            bluestacks_window = [region[
                0].left,region[0].top,region[0].width,region[0].height]
            time.sleep(60)
            adFound=False
            for i in range(4):
                for cross in crosses:
                    closead_location = pyautogui.locateOnScreen(cross,region=(bluestacks_window),confidence=0.7,grayscale=True)
                    if closead_location is not None:
                        print("Clicked on X...")
                        pyautogui.moveTo(closead_location)
                        time.sleep(1)
                        pyautogui.mouseDown()
                        pyautogui.mouseUp()
                        region = pyautogui.getWindowsWithTitle('BlueStacks App Player 1')
                        bluestacks_window = [region[
                            0].left,region[0].top,region[0].width,region[0].height]
                        adFound = True
                        break
                print("Looking for another X...")
                time.sleep(5)
            if adFound:
                time.sleep(5)
                region = pyautogui.getWindowsWithTitle('BlueStacks App Player 1')
                bluestacks_window = [region[
                    0].left,region[0].top,region[0].width,region[0].height]
                for i in range(2):
                    ok_location = pyautogui.locateOnScreen("ok.png", region=(bluestacks_window),confidence=0.7)
                    if ok_location is not None:
                        pyautogui.moveTo(ok_location)
                        pyautogui.mouseDown()
                        pyautogui.mouseUp()
                        time.sleep(1)
                print("Ad watched.")
    button.configure(state="normal")
    slider.configure(state="normal")

def test():
    button.configure(state="disabled")
    progressbar = ctk.CTkProgressBar(master=app, orientation="horizontal")
    progressbar.grid(row=3,column=0,padx=20,pady=20,columnspan=2)
    button.configure(state="normal")
def button_function():
    print("button pressed")
def change_slider_val(x):
    number.configure(text=str(int(x)))


ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

app = ctk.CTk()  
app.geometry("400x240")
app.title("IMVU Ad Watcher")
app.grid_columnconfigure(0, weight=1)

text = ctk.CTkLabel(master=app,text="Please select number of ADs you want to watch")
text.grid(row=0,column=0,padx=0, pady=20,sticky="ew",columnspan=2)
number = ctk.CTkLabel(master=app,text="0")
number.grid(row=1,column=1,padx=20,pady=20)
slider = ctk.CTkSlider(master=app,from_=0,to=50,command=lambda x: change_slider_val(x),number_of_steps=50)
slider.set(0)
slider.grid(row=1, column=0, padx=0, pady=20)
button = ctk.CTkButton(master=app, text="Execute", command=adWatcher,text_color="#FFFFFF",font=ctk.CTkFont(family="Trebuchet MS", size=14, weight="bold", slant="roman", underline=False))
button.grid(row=2, column=0, padx=20, pady=20,columnspan=2)


app.mainloop()