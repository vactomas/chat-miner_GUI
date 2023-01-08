from chatminer.chatminer.chatparsers import (
    TelegramHtmlParser,
    TelegramJsonParser,
    FacebookMessengerParser,
    SignalParser,
    WhatsAppParser,
)


def choose_parser(
    parser,
    file,
):

    match parser:

        case "Telegram - JSON":
            parser = TelegramJsonParser(file)

        case "Telegram - HTML":
            parser = TelegramHtmlParser(file)

        case "Facebook Messenger":
            parser = FacebookMessengerParser(file)

        case "Signal":
            parser = SignalParser(file)

        case "WhatsApp":
            parser = WhatsAppParser(file)

    return parser


def choose_what_to_plot(
    heatmap,
    sunburst,
    wordcloud,
    radarchart,
):

    what_to_plot = []

    if heatmap == 1:
        what_to_plot.append("HEATMAP")

    if sunburst == 1:
        what_to_plot.append("SUNBURST")

    if wordcloud == 1:
        what_to_plot.append("WORDCLOUD")

    if radarchart == 1:
        what_to_plot.append('RADARCHART')

    return what_to_plot


def choose_gradient(gradient):

    match gradient:

        case "Greys":
            return "Greys"

        case "Purples":
            return "Purples"

        case "Blues":
            return "Blues"

        case "Greens":
            return "Greens"

        case "Oranges":
            return "Oranges"

        case "Reds":
            return "Reds"

        case "YellowOrangeBrown":
            return "YlOrBr"

        case "YellowOrangeRed":
            return "YlOrRd"

        case "OrangeRed":
            return "OrRd"

        case "PurpleRed":
            return "PuRd"

        case "RedPurple":
            return "RdPu"

        case "BluePurple":
            return "BuPu"

        case "GreenBlue":
            return "GnBu"

        case "PurpleBlue":
            return "PuBu"

        case "YellowGreenBlue":
            return "YlGnBu"

        case "BlueGreen":
            return "BuGn"

        case "YellowGreen":
            return "YlGn"

        case "Heat":
            return "hot"


def choose_color(color):

    match color:

        case "Blue":
            return "b"

        case "Green":
            return "g"

        case "Red":
            return "r"

        case "Cyan":
            return "c"

        case "Magenta":
            return "m"

        case "Yellow":
            return "y"

        case "Black":
            return "k"

        case "White":
            return "w"

        case "Orange":
            return "#fa8128"

        case "Pink":
            return "#ff69b4"
