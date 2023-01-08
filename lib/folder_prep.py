import os


def folder_prep(
    plot_path,
):

    try:

        os.mkdir(plot_path)

    except FileExistsError:

        return

    return
