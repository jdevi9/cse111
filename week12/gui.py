import tkinter as tk
import number_entry as numy
import math

def main():
    
    # creates Tk root object
    root = tk.Tk()

    # creates window
    frm_main = tk.Frame(root)
    frm_main.master.title('Area of a Circle')
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)

    # fills the window
    populate_main_window(frm_main)

    # starts processing user events
    root.mainloop()

# widgets to fill the window
def populate_main_window(frm_main):
    """Populates the main window 
    Parameter
        frm_main: main window
    return: nothing
    """
    # frm: a frame (window) widget
    # lbl: a label widget that displays text for the user to see
    # ent: an entry widget where a user will type text or numbers
    # btn: a button widget that the user will click

    #creates the label for "radius"
    lbl_radius = tk.Label(frm_main, text='Radius:')

    # user can enter the radius
    ent_radius = numy.FloatEntry(frm_main, 0, 1000000, width=7)

    # label for "area"
    lbl_area = tk.Label(frm_main, text='Area:')

    # displays with answer    
    lbl_area_result = tk.Label(frm_main, width = 7)

    # the clear button
    btn_clear = tk.Button(frm_main, text="Reset")

    lbl_radius.grid(   row=0, column=0, padx=3, pady=3)
    ent_radius.grid(   row=0, column=1, padx=3, pady=3)
    lbl_area.grid(     row=0, column=4, padx=(30,3), pady=3)
    lbl_area_result.grid(   row=0, column=5, padx=3, pady=3)
    btn_clear.grid(    row=1, column=0, padx=3, pady=3)

    def calc(event):
        """Computes the area of a circle from user's 
        input of the radius
        """
        try:
            # get user radius input
            radius = ent_radius.get()
            #compute area of circle
            area_of_circle = math.pi * (radius * radius)
            # displays the answer
            lbl_area_result.config(text=f'{area_of_circle:.2f}')

        except ValueError:
            # clears answer when input box is cleared
            lbl_area_result.config(text='')

    # works only when button pressed
    def clear():
        """Clear input and output"""
        ent_radius.delete(0, tk.END)
        lbl_area_result.config(text='')
        ent_radius.focus()

    # binds calc function to entry box
    ent_radius.bind("<KeyRelease>", calc)

    # binds clear button to clear function
    btn_clear.config(command=clear)
    
    # gives focus to radius entry box
    ent_radius.focus

if __name__ == '__main__':
    main()


