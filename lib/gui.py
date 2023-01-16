import PySimpleGUI as sg
import datetime as dt


def make_window(theme):

    sg.theme(theme)

    select_year = [
        [
            sg.Text("Year to plot:"),
            sg.InputText(
                key="-YEAR-",
                default_text=dt.date.today().year,
                s=(10, 2),
            ),
        ]
    ]

    choose_messenger = [
        [
            sg.OptionMenu(
                [
                    "Telegram - JSON",
                    "Telegram - HTML",
                    "Facebook Messenger",
                    "Signal",
                    "WhatsApp",
                    "Instagram",
                ],
                s=(20, 2),
                default_value="Telegram - JSON",
                key="-MESSENGER-",
            )
        ]
    ]

    graphs_to_plot = [
        [
            sg.Checkbox(
                "Heatmap",
                default=True,
                key="-HEATMAP-",
            ),
            sg.Checkbox(
                "Sunburst",
                default=True,
                key="-SUNBURST-",
            ),
            sg.Checkbox(
                "Wordcloud",
                default=False,
                key="-WORDCLOUD-",
            ),
            sg.Checkbox(
                "Radarchart",
                default=True,
                key="-RADARCHART-",
            ),
        ],
    ]

    file_select = [
        [
            sg.Text("Choose chat export file:"),
            sg.Input(s=(20, 1)),
            sg.FileBrowse(key="-CHAT_EXPORT_FILE-"),
        ],
    ]

    colour_picker_text = [
        [
            sg.Text("Heatmap colour gradient:"),
        ],
        [
            sg.Text("Sunburst graph colour:"),
        ],
        [
            sg.Text("Radarchart graph colour:"),
        ],
    ]

    colour_picker = [
        [
            sg.OptionMenu(
                [
                    "Greys",
                    "Purples",
                    "Blues",
                    "Greens",
                    "Oranges",
                    "Reds",
                    "YellowOrangeBrown",
                    "YellowOrangeRed",
                    "OrangeRed",
                    "PurpleRed",
                    "RedPurple",
                    "BluePurple",
                    "GreenBlue",
                    "PurpleBlue",
                    "YellowGreenBlue",
                    "PurpleBlueGreen",
                    "BlueGreen",
                    "YellowGreen",
                    "Heat",
                ],
                s=(15, 1),
                default_value="Blues",
                key="-HEATMAP_GRADIENT-",
            ),
        ],
        [
            sg.OptionMenu(
                [
                    "Blue",
                    "Green",
                    "Red",
                    "Cyan",
                    "Magenta",
                    "Yellow",
                    "Black",
                    "White",
                    "Orange",
                    "Pink",
                ],
                s=(15, 1),
                default_value="Blue",
                key="-SUNBURST_COLOR-",
            ),
        ],
        [
            sg.OptionMenu(
                [
                    "Blue",
                    "Green",
                    "Red",
                    "Cyan",
                    "Magenta",
                    "Yellow",
                    "Black",
                    "White",
                    "Orange",
                    "Pink",
                ],
                s=(15, 1),
                default_value="Blue",
                key="-RADARCHART_COLOR-",
            ),
        ],
    ]

    graph_file_name = [
        [
            sg.Column([[sg.Text("Graph file name:"),]]),
            sg.Column([[sg.InputText(
                key="-GRAPH_FILE_NAME-",
                s=(15, 2),
                default_text="export",
            ),]])
        ]
    ]

    start_the_process = [
        [
            sg.Button("START"),
        ]
    ]

    status = [
        [
            sg.Multiline(
                size=(40, 2),
                expand_x=True,
                expand_y=True,
                write_only=False,
                reroute_stdout=True,
                reroute_stderr=True,
                echo_stdout_stderr=True,
                autoscroll=True,
                auto_refresh=True,
            ),
        ]
    ]

    layout = [
        [
            sg.Column(choose_messenger),
            sg.Column(select_year),
        ],
        [graphs_to_plot],
        [file_select],
        [
            sg.Column(colour_picker_text),
            sg.Column(colour_picker),
        ],
        [graph_file_name],
        [
            sg.Column(start_the_process),
            sg.Column(status),
        ],
    ]

    window = sg.Window(
        title="Chat Miner",
        layout=layout,
        grab_anywhere=True,
        resizable=True,
        margins=(0, 0),
        use_custom_titlebar=True,
        finalize=True,
        keep_on_top=True,
    )

    return window
