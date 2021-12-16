import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    #draw ground
    #ground_height = scene_bottom + 350 ////////////////////////////////
    draw_ground(canvas)
    draw_sky(canvas)
    draw_sun(canvas, 300, 75)
    draw_ocean(canvas)
    draw_fence(canvas, scene_left, scene_top, scene_right, scene_bottom, 20)
    draw_waves(canvas)
    draw_clouds(canvas, scene_left, scene_top, scene_right, scene_bottom, 200)
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 700
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 100
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    #draw grid on top for reference
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

   

    draw_infoboard(canvas)



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

#grid function to help space items on scene
def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10
    # Draw horizonal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

    # Draw Vertical Lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

def draw_fence(canvas, left, top, right, bottom, grid_spacing):
    canvas.create_line(0, 350, 800, 350, width=3, fill="#afaca1")
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top + 330, i, bottom - 120, fill="#afaca1", width=5)

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_ground(canvas):
    canvas.create_rectangle(0, 350, 800, 500, fill="#a06f52")

def draw_ocean(canvas):
    canvas.create_rectangle(0, 100, 800, 350, fill="#3c83d9")

def draw_sky(canvas):
    canvas.create_rectangle(0, 0, 800, 100, fill="#ff7f27")

def draw_sun(canvas, x, y):
    canvas.create_oval(x, y, x + 200, y + 50, fill="#ffca18")

def draw_rock(canvas, x, y):
    canvas.create_oval(x, y)


def draw_infoboard(canvas):
    canvas.create_line(250, 350, 250, 400, fill="brown", width=15)
    canvas.create_rectangle(200, 300, 300, 360, fill="brown")
    canvas.create_rectangle(210, 310, 290, 350, fill="white")
    canvas.create_line(250, 320, 280, 320, fill="black")
    canvas.create_line(250, 325, 280, 325, fill="black")
    canvas.create_line(250, 330, 280, 330, fill="black")
    canvas.create_line(250, 335, 280, 335, fill="black")
    canvas.create_line(250, 340, 280, 340, fill="black")
    canvas.create_line(215, 315, 285, 315, fill="black")
    canvas.create_rectangle(215, 320, 245, 340, fill="white")

def draw_waves(canvas):
    canvas.create_line(20, 110, 750, 110, fill="#202def")
    canvas.create_line(50, 125, 800, 125, fill="#202def")
    canvas.create_line(20, 130, 700, 130, fill="#00a8f3")
    canvas.create_line(50, 140, 750, 140, fill="#202def")
    canvas.create_line(20, 150, 800, 150, fill="#202def")
    canvas.create_line(50, 160, 750, 160, fill="#202def")
    canvas.create_line(20, 170, 800, 170, fill="#202def")
    canvas.create_line(50, 180, 750, 180, fill="#202def")

def draw_clouds(canvas, left, top, right, bottom, grid_spacing):
    for i in range(left, right, grid_spacing):
        canvas.create_oval(i + 20, top + 50, i + 150, bottom - 475, fill="#c3c3c3", outline="#ff7f27")
    

# Call the main function so that
# this program will start executing.
main()