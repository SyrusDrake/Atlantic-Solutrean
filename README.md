# Across Icy Atlantic

The purpose of this project is to simulate a hypothetical Atlantic Ocean crossing by Solutrean hunters. The idea was primarily inspired by the paper ["Solutrean Seal Hunters?"](https://www.journals.uchicago.edu/doi/abs/10.3998/jar.0521004.0070.404) by Kelly M. Phillips (2014) and the book ["Across Atlantic Ice"](https://www.ucpress.edu/books/across-atlantic-ice/paper) by Dennis J. Stanford and Bruce A. Bradley (2012). 

# Project Goals

This application was written as a supplement to a seminar paper written in 2024/2025. The goal is not to offer a comprehensive and scientifically accurate simulation of a hypothetical crossing, but to offer an alternative to the model proposed by Phillips (2014), whose parameters can be adjusted by the user, as they seem fit (within reason). 

# Assumptions

- The crossing is assumed to be a one-way trip, with no return.
- The crossing is assumed to be somewhat deliberate. Hunting is only performed for immediate needs, and direction of travel never points more than 90° away from the destination.
- Maximum distance is assumed to be 4500 km, which is the distance from the former European coast during the LGM, to what is today Nova Scotia, measured as a "rump line" of constant bearing at 270°.
- Maximum boat speed is 10 knots, although this is highly unlikely. A speed of 2-3 knots can be assumed. 
- Maximum sea ice duration is 360 days. Even during the height of the LGM, maximum sea ice duration for an average year is assumed to have been 90 days.
- A daily caloric intake of 3800 kcal is assumed, based on [Mullie et al. (2021)](https://www.tandfonline.com/doi/full/10.1080/22423982.2021.1932184)
- To sustain this caloric intake, one seal has to be hunted every 6 days, based on [Wenzel (1991)](https://www.degruyter.com/document/doi/10.3138/9781442670877/html)

# Usage

Upon launch, the application will run in the default browser. The simulation parameters can be adjusted via sliders. By default, the result will be displayed as a duration taken to cover the selected distance, compared to the available time. If "verbose" is checked, activity (hunting or traveling) as well as remaining distance for each day is printed out. 

# Installation

The application is provided as an executable for either Windows or Linux. The source code is available on GitHub. Python 3 has to be installed, as well as the gradio library. 
The default web browser will launch automatically. To manually open the interface, open a web browser and navigate to http://localhost:7860
