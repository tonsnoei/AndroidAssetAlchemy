import os
import tkinter as tk
from tkinter import messagebox, filedialog

from tkinterdnd2 import DND_FILES, TkinterDnD
from typing import Optional

from dependencies import Dependencies
from enums.android_file_size import AndroidFileSize
from services.image.image_converter import ImageConverter
from services.image.models.size import Size


class WindowCreateActionBarIcon:
    def __init__(self):
        self.drop_label = None
        self.drop_frame = None
        self.browse_button = None
        self.directory_entry = None
        self.directory_entry_label = None
        self.directory_var = None

    def __int__(self):
        self.window: Optional[tk.Toplevel] = None

    def show(self, parent: TkinterDnD.Tk):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Action Bar/Toolbar Icon")
        self.window.geometry("400x400")

        self.window.transient(parent)  # Verbind met hoofdvenster
        self.window.grab_set()  # Blokkeert interactie met hoofdvenster

        # Entry field for directory path
        # Label
        self.directory_entry_label = tk.Label(self.window, text="Export Directory:")
        self.directory_entry_label.pack()

        # Input
        self.directory_var = tk.StringVar()
        self.directory_entry = tk.Entry(self.window, textvariable=self.directory_var, width=30)
        self.directory_entry.pack()

        # Browse button
        self.browse_button = tk.Button(self.window, text="Browse", command=self._browse_directory)
        self.browse_button.pack()

        self.drop_frame = tk.Frame(self.window, width=200, height=200, bg="lightgray", relief="sunken", borderwidth=1)
        self.drop_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.drop_label = tk.Label(self.drop_frame,
                                  text="📁 Drop your image file here.\n(png, webp with background transparancy)",
                                  bg='lightgray',
                                  font=('Arial', 14),
                                  justify='center')
        self.drop_label.pack(expand=True)

        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.on_drop)


    def on_drop(self, event):
        files: [str] = self.window.tk.splitlist(event.data)
        self.handle_files(files)

    def handle_files(self, files: [str]):

        file = files[0]
        output_dir = self.directory_var.get()

        if not output_dir:
            self._show_dialog_no_export_dir()
            return

        if len(files) > 1:
            self._show_dialog_too_many_files()
            return

        if not self._image_converter.is_supported(file):
            self._show_dialog_unsupported_file(file)
            return

        image_size: Size = self._image_converter.get_size(file)
        if not image_size.is_square():
            self._show_dialog_not_square(file, image_size)
            return

        self._ensure_dir(output_dir, AndroidFileSize.MDPI)
        self._ensure_dir(output_dir,AndroidFileSize.HDPI)
        self._ensure_dir(output_dir,AndroidFileSize.XHDPI)
        self._ensure_dir(output_dir,AndroidFileSize.XXHDPI)
        self._ensure_dir(output_dir,AndroidFileSize.XXXHDPI)

        self._create_image(file, AndroidFileSize.MDPI)
        self._create_image(file, AndroidFileSize.HDPI)
        self._create_image(file, AndroidFileSize.XHDPI)
        self._create_image(file, AndroidFileSize.XXHDPI)
        self._create_image(file, AndroidFileSize.XXXHDPI)

        self._show_dialog_success()



    def _create_image(self, in_file_path: str, android_file_size: AndroidFileSize):
        out_file_path = self._create_out_filename(in_file_path, android_file_size)
        size: Size = self._get_image_size(android_file_size)
        self._image_converter.resize(in_file_path, out_file_path, size)

    def _get_image_size(self, android_file_size: AndroidFileSize) -> Size:
        if android_file_size == AndroidFileSize.MDPI:
            return Size(24, 24)
        elif android_file_size == AndroidFileSize.HDPI:
            return Size(48, 48)
        elif android_file_size == AndroidFileSize.XHDPI:
            return Size(72, 72)
        elif android_file_size == AndroidFileSize.XXHDPI:
            return Size(96, 96)
        elif android_file_size == AndroidFileSize.XXXHDPI:
            return Size(144, 144)
        else:
            return Size(24, 24)

    def _create_out_filename(self, in_file_path: str, androidFileSize: AndroidFileSize) -> str:
        result : str =  str(os.path.join(self.directory_var.get(), androidFileSize.value, os.path.basename(in_file_path)))
        result = os.path.splitext(result)[0] + ".png"
        return result

    def _ensure_dir(self, dir: str, android_file_size: AndroidFileSize):
        final_dir = os.path.join(dir, android_file_size.value)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

    def _show_dialog_unsupported_file(self, file: str) -> None:
        messagebox.showerror(
            title="Not support file",
            message=f"The file {file} must be of type .png or .webp."
        )

    def _show_dialog_no_export_dir(self):
        messagebox.showerror(
            title="No export directory",
            message="Please select an export directory."
        )

    def _show_dialog_success(self):
        messagebox.showinfo(
            title="Success",
            message="The action bar icon has been created successfully."
        )

    def _browse_directory(self):
        """Open directory selection dialog and update the entry field"""
        directory = filedialog.askdirectory(
            title="Select Directory",
            initialdir=self.directory_var.get() if self.directory_var.get() else "/"
        )

        if directory:  # Only update if a directory was selected
            self.directory_var.set(directory)

    @property
    def _image_converter(self) -> ImageConverter:
        return Dependencies.instance().image_converter

    def _show_dialog_too_many_files(self):
        messagebox.showerror(
            title="Too many files",
            message="Drop only one file."
        )

    def _show_dialog_not_square(self, file, size: Size):
        messagebox.showerror(
            title="Not square file",
            message=f"The file {file} ({size.width}px, {size.height}px) must be square. Width and height must be the same."
        )