import tkinter as tk
from typing import Optional, Callable
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

class WindowMain:

    def __init__(self):
        self.window: Optional[tk.Tk] = None

        self.btn_create_launcher_icon: Optional[tk.Button] = None
        self.btn_create_action_bar_icon: Optional[tk.Button] = None
        self.btn_create_tab_icon: Optional[tk.Button] = None
        self.btn_create_notification_icon: Optional[tk.Button] = None
        self.btn_create_menu_icon: Optional[tk.Button] = None
        self.btn_create_dialog_icon: Optional[tk.Button] = None
        self.btn_create_list_icon: Optional[tk.Button] = None

        self._btn_create_launcher_icon_callable: Optional[Callable] = None
        self._btn_create_action_bar_icon_callable: Optional[Callable] = None
        self._btn_create_tab_icon_callable: Optional[Callable] = None
        self._btn_create_notification_icon_callable: Optional[Callable] = None
        self._btn_create_menu_icon_callable: Optional[Callable] = None
        self._btn_create_dialog_icon_callable: Optional[Callable] = None
        self._btn_create_list_icon_callable: Optional[Callable] = None

    def show(self):
        self.window = TkinterDnD.Tk()
        self.window.title("Android Asset Alchemy")
        self.window.geometry("400x400")

        image = Image.open("assets/img/icon256.png")
        image = image.resize((150, 150))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.window, image=photo)
        label.pack()

        widthInChars = 25

        self.btn_create_launcher_icon = tk.Button(self.window,
                                                  text="Create Launcher Icon",
                                                  width=widthInChars,
                                                  command=self._btn_create_launcher_icon_callable)
        self.btn_create_launcher_icon.pack()

        self.btn_create_action_bar_icon = tk.Button(self.window,
                                                    text="Create Action Bar/Toolbar Icon",
                                                    width=widthInChars,
                                                    command=self._btn_create_action_bar_icon_callable)
        self.btn_create_action_bar_icon.pack()

        self.btn_create_tab_icon: Optional[tk.Button] = tk.Button(self.window,
                                                                  text="Create Tab Icon",
                                                                  width=widthInChars,
                                                                  command=self._btn_create_tab_icon_callable)
        self.btn_create_tab_icon.pack()

        self.btn_create_notification_icon: Optional[tk.Button] = tk.Button(self.window,
                                                                           text="Create Notification Icon",
                                                                           width=widthInChars,
                                                                           command=self._btn_create_notification_icon_callable)
        self.btn_create_notification_icon.pack()

        self.btn_create_menu_icon: Optional[tk.Button] = tk.Button(self.window,
                                                                   text="Create Menu/Navigation Icon",
                                                                   width=widthInChars,
                                                                   command=self._btn_create_menu_icon_callable)
        self.btn_create_menu_icon.pack()

        self.btn_create_dialog_icon: Optional[tk.Button] = tk.Button(self.window,
                                                                     text="Create Dialog/Alert Icon",
                                                                     width=widthInChars,
                                                                     command=self._btn_create_dialog_icon_callable)
        self.btn_create_dialog_icon.pack()

        self.btn_create_list_icon: Optional[tk.Button] = tk.Button(self.window,
                                                                   text="Create List/Content Icon",
                                                                   width=widthInChars,
                                                                   command=self._btn_create_list_icon_callable)
        self.btn_create_list_icon.pack()

        self.window.mainloop()


    def set_btn_create_launcher_icon_click_event(self, callable: Callable):
        self._btn_create_launcher_icon_callable = callable

    def set_btn_create_action_bar_icon_click_event(self, callable: Callable):
        self._btn_create_action_bar_icon_callable = callable

    def set_btn_create_tab_icon_click_event(self, callable: Callable):
        self._btn_create_tab_icon_callable = callable

    def set_btn_create_notification_icon_click_event(self, callable: Callable):
        self._btn_create_notification_icon_callable = callable

    def set_btn_create_menu_icon_click_event(self, callable: Callable):
        self._btn_create_menu_icon_callable = callable

    def set_btn_create_dialog_icon_click_event(self, callable: Callable):
        self._btn_create_dialog_icon_callable = callable

    def set_btn_create_list_icon_click_event(self, callable: Callable):
        self._btn_create_list_icon_callable = callable

