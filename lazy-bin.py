import ctypes

def empty_recycle_bin():
    SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
    SHEmptyRecycleBin(None, None, 0)

empty_recycle_bin()
