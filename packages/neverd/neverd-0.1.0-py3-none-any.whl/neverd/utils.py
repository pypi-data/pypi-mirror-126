
import os
import tkinter as tk


MAP_POS_TO_CURSOR_SYMBOL = {
    'bottom-right': 'bottom_right_corner',
    'top-right': 'top_right_corner',
    'top-left': 'top_left_corner',
    'bottom-left': 'bottom_left_corner',
    'left': 'left_side',
    'right': 'right_side',
    'top': 'top_side',
    'bottom': 'bottom_side'
}


def flatten_list(ls):
    new_list = []
    for ls_ in ls:
        new_list.extend(ls_)

    return new_list


def get_root(widget):
    parent = widget
    while True:
        if parent.master is None:
            return parent
        parent = parent.master


def get_menubar(root):
    if root['menu']:
        for child in root.winfo_children():
            if isinstance(child, tk.Menu):
                menubar = child
                break
    else:
        menubar = tk.Menu()
        root.configure(menu=menubar)

    return menubar


def disable_children(parent):
    for child in parent.winfo_children():
        try:
            child.configure('state')
        except tk.TclError:
            disable_children(child)
            continue

        wtype = child.winfo_class()

        if 'Label' in wtype:
            continue

        elif 'Entry' in wtype:
            state = 'readonly'
        else:
            state = 'disabled'

        child.configure(state=state)
        disable_children(child)


def get_bound_position(canvas, widget_id, x, y, tol=2):
    coords = canvas.bbox(widget_id)
    if coords is None:
        return None

    x1, y1, x2, y2 = coords

    left = _is_left(x1, x, tol)
    right = _is_right(x2, x, tol)
    top = _is_top(y1, y, tol)
    bottom = _is_bottom(y2, y, tol)

    if not left and not right and not top and not bottom:
        return None

    str_out = ''
    for pos, pos_str in zip([bottom, top, right, left],
                            ['bottom', 'top', 'right', 'left']):
        if pos:
            str_out += f'-{pos_str}'

    return str_out[1:]


def _is_left(x1, x, tol):
    return x1 - tol <= x <= x1 + tol


def _is_right(x2, x, tol):
    return x2 - tol <= x <= x + tol


def _is_top(y1, y, tol):
    return y1 - tol <= y <= y1 + tol


def _is_bottom(y2, y, tol):
    return y2 - tol <= y <= y2 + tol


def get_image_path(filename):

    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'images', filename)
