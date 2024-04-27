import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import matplotlib.font_manager as fm
import math

prop = fm.FontProperties(fname="fonts/Lugrasimo-Regular.ttf")


def draw_shape(ax, x, y, num):
    # Define hexagon
    hexagon = RegularPolygon(
        (x, y), numVertices=6, radius=0.25, edgecolor="darkgrey", facecolor="none"
    )
    ax.add_patch(hexagon)

    # Add number inside the hexagon
    ax.text(
        x, y, str(num), ha="center", va="center", color="darkgrey", fontproperties=prop
    )


def generate_and_save_page():
    # Size of A4 page in inches
    a4_width_inches = 8.27
    a4_height_inches = 11.69

    # Calculate number of rows and columns based on the number of shapes
    num_shapes = 365
    num_cols = 18
    num_rows = math.ceil(num_shapes / num_cols)

    # Calculate size of each shape
    shape_width = a4_width_inches / num_cols
    # shape_height = a4_height_inches / num_rows
    shape_height = 0.4  # Manually adjust for better spacing

    _, ax = plt.subplots(figsize=(a4_width_inches, a4_height_inches))

    # Draw the big heading
    ax.text(
        a4_width_inches / 2,
        a4_height_inches - 1.0,
        "And counting...",
        ha="center",
        va="center",
        fontsize=42,
        color="darkgrey",
        weight="bold",
        fontproperties=prop,
    )

    # Draw shapes with numbers
    i = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if i < num_shapes:
                x = (col + 0.5) * shape_width

                if row % 2 == 0:  # Even row
                    if col == num_cols - 1:
                        continue
                    x += shape_width / 2
                if row == num_rows - 1:  # Last row
                    x += shape_width

                y = (
                    num_rows - row + 1.5 # Padding
                ) * shape_height  # Reverse rows to start from top
                ax.set_xlim(0, a4_width_inches)
                ax.set_ylim(0, a4_height_inches)
                ax.set_aspect("equal", "box")
                ax.axis("off")
                i += 1
                draw_shape(ax, x, y, i)

    plt.savefig("hexagon_tracker_a4.pdf", dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    generate_and_save_page()
