import os


def ft_tqdm(lst: range) -> None:
    """
    Takes in an iterable and yields each item one by one
    and displays a progress bar, scaled to the size of the
    terminal
    """
    ter_size = os.get_terminal_size()
    len_digits = len(str(len(lst)))
    bar_width = ter_size.columns - (33 + (len_digits * 2 + 1))
    for i, v in enumerate(lst):
        percent = i / len(lst) * 100
        filled = int((i+1) / len(lst) * bar_width)
        empty = bar_width - filled
        bar = "█" * filled + " " * empty
        total = f"| {i+1:{len_digits}d}/{len(lst)}"
        print(f"{percent:3.0f}%|" + bar + total + "\r", end="",flush=True)
        yield v
