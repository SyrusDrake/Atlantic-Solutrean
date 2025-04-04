"""This is the main file for the Atlantic Solutrean project."""

import gradio as gr

#: How much distance has to be travelled (in km)
range_distances: list[int] = [500, 4500]
#: Step size for the distance (in km)
step_distances: int = 500

#: How fast the vehicle can go (in knots, for ease of use)
range_speeds: list[float] = [0.5, 10]
# : Step size for the speed (in knots)
step_speeds: float = 0.5

#: Duration of the sea ice in days
range_duration: list[int] = [30, 360]
#: Step size for the duration (in days)
step_duration: int = 30

#: How many hours are spent on traveling each day
range_hours: list[int] = [1, 24]
#: Step size for the hours (in hours)
step_hours: int = 1

#: What percentage of calories has to be gathered as opposed to coming from provisions
step_perc_gather: int = 10


def calc_crossing_duration(distance: int, speed: float, traveling_hours: int) -> int:
    """Calculates the crossing duration based on distance and speed.

    Args:
        distance (int): The distance to be traveled in kilometers.
        speed (float): The speed of the vehicle in knots.
        traveling_hours (int): The number of hours spent traveling each day.

    Returns:
        int: The crossing duration in days, rounded to the nearest whole number.
    """
    # Convert knots to km/h
    speed_kmh = speed * 1.852
    # Calculate time in hours
    time_hours = distance / speed_kmh
    # Calculate time in days, considering the hours spent traveling each day (rounded to the nearest whole number)
    time_days = round(time_hours / traveling_hours)

    return time_days


def gui():
    """Draws the GUI for the Atlantic Solutrean project.

    Returns:
        None
    """

    with gr.Blocks() as simulation:
        gr.Markdown("# Atlantic Crossing")  # : Title of the app
        #: Slider to set the distance
        distance = gr.Slider(
            label="Distance [km]", minimum=range_distances[0], maximum=range_distances[1], step=step_distances,
            interactive=True)
        #: Slider to set the speed of the boat
        speed = gr.Slider(
            label="(Max.) Speed [kts]", minimum=range_speeds[0], maximum=range_speeds[1], step=step_speeds,
            interactive=True)
        #: Slider to set the duration of the sea ice
        duration = gr.Slider(
            label="Duration of sea ice [days]", minimum=range_duration[0], maximum=range_duration[1], step=step_duration,
            interactive=True)
        #: Slider to set the hours spent on traveling each day
        hours = gr.Slider(
            label="Hours spent traveling each day", minimum=range_hours[0], maximum=range_hours[1], step=step_hours,
            interactive=True)
        #: Slider to set the percentage of calories that has to be gathered
        gather = gr.Slider(
            label="% gathered calories", minimum=0, maximum=100, step=step_perc_gather,
            interactive=True)

        output = gr.Textbox(label="Output")
        test_btn = gr.Button("Test")
        test_btn.click(fn=calc_crossing_duration, inputs=[
                       distance, speed, hours], outputs=output)

    simulation.launch()


if __name__ == "__main__":
    gui()
