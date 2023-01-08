from lib.folder_prep import folder_prep
from lib.plot import plot
from lib.choice_maker import (
    choose_gradient,
    choose_color,
    choose_parser,
    choose_what_to_plot,
)
from lib.gui import make_window

import PySimpleGUI as sg


def main():

    plot_path = "./plots/"

    window = make_window(
        sg.theme("DarkAmber"),
    )

    while True:
        event, values = window.read(
            timeout=100,
        )

        if event == sg.WIN_CLOSED or event == "Exit":

            break

        if event == "START":

            try:

                folder_prep(plot_path)

                parser = values["-MESSENGER-"]
                file = values["-CHAT_EXPORT_FILE-"]
                filename = "export"
                year = int(values["-YEAR-"])
                cmap = choose_gradient(values["-HEATMAP_GRADIENT-"])
                color_sunburst = choose_color(values["-SUNBURST_COLOR-"])
                color_radarchart = choose_color(values["-RADARCHART_COLOR-"])
                heatmap = int(values["-HEATMAP-"])
                sunburst = int(values["-SUNBURST-"])
                wordcloud = int(values["-WORDCLOUD-"])
                radarchart = int(values["-RADARCHART-"])
                what_to_plot = choose_what_to_plot(
                    heatmap,
                    sunburst,
                    wordcloud,
                    radarchart,
                )

                parser = choose_parser(
                    parser,
                    file,
                )

                parser.parse_file_into_df()

                condition_df = parser.df.loc[
                    (parser.df["datetime"] >= f"{str(year)}-01-01 00:01")
                    & (parser.df["datetime"] < f"{str(year)}-12-31 23:59")
                ]

                if not condition_df.empty:

                    plot(
                        parser,
                        filename,
                        plot_path,
                        year,
                        cmap,
                        color_sunburst,
                        color_radarchart,
                        what_to_plot,
                    )

                    print("\n\n\n\n[LOG] Done!")

                else:

                    print("\n\n\n\n[LOG] Error - invalid year")

            except AssertionError:

                print("\n\n\n\n[LOG] Error! Check everything and try again")

    return


if __name__ == "__main__":

    main()
