import tkinter as tk
from typing import Optional

from ui.window_main import WindowMain
from ui.window_create_action_bar_icon import WindowCreateActionBarIcon

class Main:
    def __int__(self):
        self.main_window_view: Optional[WindowMain] = None

    def run(self):
        self.main_window_view = WindowMain()

        self.main_window_view.set_btn_create_action_bar_icon_click_event(self.show_window_create_action_bar_icon)
        # Must be the last method to call
        self.main_window_view.show()

    def show_window_create_action_bar_icon(self):
        window_create_action_bar_icon = WindowCreateActionBarIcon()
        window_create_action_bar_icon.show(self.main_window_view.window)


if __name__ == "__main__":
    Main().run()