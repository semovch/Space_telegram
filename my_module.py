import os


def split(link):
    link_ext = os.path.splitext(link)[1]
    return(link_ext)
