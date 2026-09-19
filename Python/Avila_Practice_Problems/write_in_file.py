import os
import os

def get_path_depth(path):
    path = os.path.normpath(path)
    return len(path.split(os.sep))


def generate_dir_report(path, report_file_path):

    main_path_depth = get_path_depth(path)

    with open(report_file_path, "w") as out:
        for root, dirs, files in sorted(os.walk(path)):
            dir_indent = (get_path_depth(root) - main_path_depth - 1) * 2
            file_indent = dir_indent + 2

            if root == path:
                out.write("+ " + os.path.basename(root) + "\n")
            else:
                out.write(" " * dir_indent + "|-+ " + os.path.basename(root) + "\n")

            for file_name in sorted(files):
                out.write(" " * file_indent + "|-- " + file_name + "\n")



def generate_dir_report(path, report_file_path, show_files=True):

    main_path_depth = get_path_depth(path)

    with open(report_file_path, "w") as out:
        for root, dirs, files in sorted(os.walk(path)):
            dir_indent = (get_path_depth(root) - main_path_depth - 1) * 2
            file_indent = dir_indent + 2

            if root == path:
                out.write("+ " + os.path.basename(root) + "\n")
            else:
                out.write(" " * dir_indent + "|-+ " + os.path.basename(root) + "\n")

            if show_files:

                for file_name in sorted(files):
                    out.write(" " * file_indent + "|-- " + file_name + "\n")


import os

def get_path_depth(path):
    path = os.path.normpath(path)
    return len(path.split(os.sep))


def generate_dir_report(
    path,
    report_file_path,
    show_files=True,
    num_files=False,
    file_size=False,
    hl=None
):

    main_path_depth = get_path_depth(path)

    with open(report_file_path, "w") as out:
        for root, dirs, files in sorted(os.walk(path)):
            dir_indent = (get_path_depth(root) - main_path_depth - 1) * 2
            file_indent = dir_indent + 2

            if root == path:
                prefix = "+ "
            else:
                prefix = " " * dir_indent + "|-+ "

            if num_files:
                out.write(
                    prefix
                    + os.path.basename(root)
                    + f" ({len(files)} files)\n"
                )
            else:
                out.write(
                    prefix
                    + os.path.basename(root)
                    + "\n"
                )

            if show_files:
                for file_name in sorted(files):

                    highlight = ""

                    if hl is not None:
                        extension = os.path.splitext(file_name)[1][1:]

                        if extension == hl:
                            highlight = " <--"

                    if file_size:
                        size = os.path.getsize(
                            os.path.join(root, file_name)
                        )

                        out.write(
                            " " * file_indent
                            + "|-- "
                            + file_name
                            + f" ({size} bytes)"
                            + highlight
                            + "\n"
                        )
                    else:
                        out.write(
                            " " * file_indent
                            + "|-- "
                            + file_name
                            + highlight
                            + "\n"
                        )