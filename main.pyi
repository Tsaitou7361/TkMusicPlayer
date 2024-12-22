import tkinter as tk
from tkinter import ttk

from os import PathLike
from pathlib import Path

from typing import AnyStr, Any
from typing_extensions import deprecated

import lang


class Config:
    file: Path
    d: dict
    encoding: str

    def __init__(self) -> None: ...

    def get(self, key: AnyStr) -> Any: ...

    def dump(self, key: AnyStr, value: Any) -> None: ...

    def _read(self) -> None: ...

    def _write(self, data: dict = None) -> None: ...


class App(TkinterDnd.Tk):
    _config: Config
    lang: lang.Lang
    current_volume: tk.DoubleVar
    total_length: None
    selected_item: None
    current_playing_file: None
    progress_in_min: tk.StringVar
    is_pinned: tk.BooleanVar
    PROGRAM_NAME: str

    menu: tk.Menu
    menu_bar: tk.Menu
    file_menu: tk.Menu
    scrollbar: ttk.Scrollbar
    _playlist: ttk.Treeview
    progress: ttk.Scale
    volume: ttk.Scale
    _volume_label: ttk.Label

    _choose_file_btn: ttk.Button
    _stop_btn: ttk.Button
    _pause_btn: ttk.Button
    _replay_btn: ttk.Button
    _play_btn: ttk.Button

    def __init__(self) -> None: ...

    def open_setting_file(self) -> None: ...

    @deprecated("This function is deprecated and will be deleted in the future.")
    def icon_validate(self) -> None: ...

    def pin(self) -> None: ...

    @staticmethod
    def time_converter(milliseconds: float) -> str: ...

    def show_context_menu(self, event) -> None: ...

    def move_to_top(self) -> None: ...

    def move_up(self) -> None: ...

    def move_down(self) -> None: ...

    def move_to_bottom(self) -> None: ...

    def on_drop(self, event) -> None: ...

    def delete_selected_item(self) -> None: ...

    def direct_metadata_show(self) -> None: ...

    def show_metadata(self) -> None: ...

    def get_metadata(self) -> dict[str, str] | None: ...

    def update_button_states(self) -> None: ...

    def set_volume(self, event=None) -> None: ...

    def get_process(self) -> None: ...

    def set_process(self, event) -> None: ...

    def choose_file(self, file: PathLike = None) -> None: ...

    def play(self) -> None: ...

    def pause(self) -> None: ...

    def stop(self) -> None: ...

    def check_music_end(self) -> None: ...

    def play_next(self) -> None: ...

    def close(self) -> None: ...

    def restart(self) -> None: ...


class InfoPopup(tk.Tk):
    tree: ttk.Treeview

    def __init__(self, metadata: dict[str, str], lang: lang.Lang) -> None: ...

    def __call__(self, *args, **kwargs) -> InfoPopup: ...

    def open_file(self, event) -> None: ...

if __name__ == '__main__':
    app_dir: PathLike[str]
