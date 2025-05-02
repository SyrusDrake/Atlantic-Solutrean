"""This is the main file for the Atlantic Solutrean project."""

import gradio as gr
from random import gauss
import math
from time import sleep
import webbrowser

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

#: Max. deviation angle (in degrees). Only values up to 90 degrees are allowed.
max_deviation: int = 90
#: Step size for the deviation angle (in degrees)
step_deviation: int = 5

#: What percentage of calories has to be gathered as opposed to coming from provisions
step_perc_gather: int = 10

#: How many calories are needed per day (based on Mullie et al. 2021)
calories_per_day: int = 3800

#: How often a seal has to be hunted (in days)
seal_hunt_interval: int = 5


def calc_new_distance(daily_distance: float, initial_distance: int, deviation_angle: float) -> int:
    """Calculates the new distance to the destination based on the deviation angle and two known distances.

    The formula is: n = sqrt(a^2 + b^2 - 2ab * cos(theta)), where:
    - n is the new distance to the destination
    - a is the daily distance traveled
    - b is the old distance to the destination
    - theta is the angle of deviation from the direct path

    Args:
        daily_distance (float): The distance traveled in a day (in km).
        initial_distance (int): The initial distance to the destination (in km).
        deviation_angle (float): The angle of deviation from the direct path (in degrees).
    Returns:
        int: The new distance to the destination (in km).
        """
    new_distance = math.sqrt(math.pow(daily_distance, 2) + math.pow(initial_distance, 2) -
                             2 * daily_distance * initial_distance * math.cos(math.radians(deviation_angle)))
    return new_distance


def randomize_angle(max_deviation: int) -> int:
    """Generates a random angle between 0 and the input maximum, following a normal distribution.

        Args:
            max_deviation (int): The maximum deviation angle in degrees.
        Returns:
            int: A random angle between 0 and max_deviation (in degrees).
        """
    mu = 0
    sigma = max_deviation / 3

    while True:
        angle = int(gauss(mu, sigma))
        return angle


def process_inputs(distance: int, speed: float, traveling_hours: int, duration: int, perc_calories: int, hunt_freq: int,  max_deviation: int, verbose: bool) -> str:
    """Processes the inputs and calculates the crossing duration.

    Args:
        distance (int): The distance to be traveled in kilometers.
        speed (float): The speed of the vehicle in knots.
        traveling_hours (int): The number of hours spent traveling each day.
        duration (int): The duration of the sea ice in days.

        perc_calories (int): The percentage of calories that has to be gathered.
        hunt_freq (int): The frequency of hunting seals in days.

        max_deviation (int): The maximum deviation angle in degrees.

        verbose (bool): If True, prints detailed output.

    Returns: 
        str: A message indicating whether the crossing was successful or not.

    """
    crossing_duration: int = 0
    verbose_output: str = ""

    # Convert knots to km/h
    speed_kmh = speed * 1.852
    # Calculates daily distance traveled
    daily_distance = speed_kmh * traveling_hours
    # Store original distance
    original_distance = distance

    # Calculates a hunting frequency based on the percentage of calories that has to be gathered
    # E.g. 100% -> 5 days, 20% -> 25 days
    if perc_calories == 0:
        # If no hunting is assumed, hunt frequency is set to 365 days, which is functionally never
        hunt_freq = 365
    else:
        hunt_freq = int(hunt_freq * (100 / perc_calories))

    while distance > daily_distance:
        crossing_duration += 1
        # Checks if it is time to hunt
        if crossing_duration % hunt_freq == 0:
            if verbose:
                verbose_output += f"Day {crossing_duration}: Time to hunt!\n"

        else:
            current_angle = randomize_angle(max_deviation)
            distance = int(calc_new_distance(
                daily_distance, distance, current_angle))
            if verbose:
                verbose_output += f"Day {crossing_duration}: New distance is {distance} km\n"

    crossing_duration += 1
    if crossing_duration < duration:
        return (f"Successfully covered {original_distance} km in {crossing_duration} days.\n"
                f"Sea ice duration: {duration} days.\n"
                "-------------------------------\n"
                + verbose_output)
    else:
        return (f"Failed to cover {original_distance} km in {crossing_duration} days.\n"
                f"Sea ice duration was only {duration} days.\n"
                "-------------------------------\n"
                + verbose_output)


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
        #: Slider to set the deviation angle
        deviation = gr.Slider(
            label="Max. deviation angle [°]", minimum=0, maximum=max_deviation, step=step_deviation,
            interactive=True)
        #: Slider to set the percentage of calories that has to be gathered
        gather = gr.Slider(
            label="% gathered calories", minimum=0, maximum=100, step=step_perc_gather,
            interactive=True)

        #: Constant numbers have to be passed to the function this way
        hunt_freq = gr.Number(visible=False, value=seal_hunt_interval)

        output = gr.Textbox(label="Output")
        verbose_check = gr.Checkbox(label="Verbose output", value=False)
        run_btn = gr.Button("Run")
        run_btn.click(fn=process_inputs, inputs=[
            distance, speed, hours, duration, gather, hunt_freq, deviation, verbose_check], outputs=output)

    simulation.launch(inbrowser=True)


if __name__ == "__main__":
    gui()
