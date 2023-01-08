from lib.STOPWORDS import STOPWORDS
import chatminer.chatminer.visualizations as vis
import matplotlib.pyplot as plt


def plot_heatmap(
    parser,
    year,
    cmap,
):

    fig, ax = plt.subplots(figsize=(9, 3))

    ax = vis.calendar_heatmap(
        parser.df,
        year=year,
        linewidth=1,
        monthly_border=True,
        cmap=cmap,
    )

    return fig


def plot_sunburst(
    parser,
    colour,
):

    fig, ax = plt.subplots(
        figsize=(7, 3),
        subplot_kw={"projection": "polar"},
    )

    ax = vis.sunburst(
        parser.df,
        highlight_max=True,
        # isolines=[400, 800],
        isolines_relative=True,
        ax=ax,
        color=colour,
    )

    return fig


def plot_wordcloud(
    parser,
):

    fig, ax = plt.subplots(figsize=(8, 3))
    kwargs = {
        "background_color": "white",
        "width": 800,
        "height": 300,
        "max_words": 500,
    }

    ax = vis.wordcloud(
        parser.df,
        ax=ax,
        stopwords=STOPWORDS,
        **kwargs,
    )

    return fig


def plot_radarchart(
    parser,
    colour,
):

    vis.radar_factory(
        7,
        frame="polygon",
    )
    vis.radar(
        parser.df,
        ax=None,
    )

    fig, ax = plt.subplots(
        figsize=(7, 3),
        subplot_kw=dict(projection="radar"),
    )

    ax = vis.radar(
        parser.df,
        ax=ax,
        color=colour,
    )

    return fig


def plot(
    parser,
    filename,
    plot_path,
    year,
    cmap,
    colour_sunburst,
    colour_radarchart,
    what_to_plot,
):

    heatmap_fig = ""
    sunburst_fig = ""
    wordcloud_fig = ""
    radarchart_fig = ""

    if "HEATMAP" in what_to_plot:

        heatmap_fig = plot_heatmap(
            parser,
            year,
            cmap,
        )

        file = f"{plot_path}/{filename}_calendar.png"
        heatmap_fig.savefig(file)

    if "SUNBURST" in what_to_plot:

        sunburst_fig = plot_sunburst(
            parser,
            colour_sunburst,
        )

        file = f"{plot_path}/{filename}_sunburst.png"
        sunburst_fig.savefig(file)

    if "WORDCLOUD" in what_to_plot:

        wordcloud_fig = plot_wordcloud(
            parser,
        )

        file = f"{plot_path}/{filename}_wordcloud.png"
        wordcloud_fig.savefig(file)

    if "RADARCHART" in what_to_plot:

        radarchart_fig = plot_radarchart(
            parser,
            colour_radarchart,
        )

        file = f"{plot_path}/{filename}_radarchart.png"

        radarchart_fig.savefig(file)

    return heatmap_fig, sunburst_fig, wordcloud_fig, radarchart_fig
