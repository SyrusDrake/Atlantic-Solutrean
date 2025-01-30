import gradio as gr

'''
General parameters that define the scenario. These are not the values that are being used but define the available values.
'''
range_distances: list[int] = [500, 4500]
step_distances: int = 500

range_speeds: list[float] = [0.5, 10]
step_speeds: float = 0.5

range_duration: list[int] = [30, 360]
step_duration: int = 30

range_hours: list[int] = [1, 24]
step_hours: int = 1

step_perc_gather: int = 5


def calc_trip_duration(distance: int, duration: int, speed: float, hours: int,  perc_gather: int):

    dist_covered = hours * duration * (speed * 1.852)

    return dist_covered


interface = gr.Interface(
    fn=calc_trip_duration,
    inputs=[
        gr.Slider(label="Distance to cover (km):",
                  minimum=range_distances[0], maximum=range_distances[1], step=step_distances),
        gr.Slider(label="Duration of sea ice (days):",
                  minimum=range_duration[0], maximum=range_duration[1], step=step_duration),
        gr.Slider(label="Speed of boat (kts):",
                  minimum=range_speeds[0], maximum=range_speeds[1], step=step_speeds),
        gr.Slider(label="Avg. hours of travel per day:",
                  minimum=range_hours[0], maximum=range_hours[1], step=step_hours),
        gr.Slider(label="% of calories from freshly gathered food:", step=step_perc_gather, value=50)],
    outputs=[gr.Textbox(label="Distance covered (km):")])

interface.launch()
