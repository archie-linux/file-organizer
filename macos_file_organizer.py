"""
macOS File Organizer App
========================

This macOS app allows users to select a folder and organize files into categories.

Author: Anish
Created: February 2025
"""

import os
import shutil
import random
from Cocoa import (
    NSApplication, NSApp, NSWindow, NSButton, NSTextField, NSSavePanel, NSView,
    NSRect, NSOpenPanel, NSObject
)
from PyObjCTools import AppHelper


# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Executables": [".dmg", ".pkg", ".app", ".exe"]
}

class FileOrganizerApp(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create the main window
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSRect((200, 200), (700, 400)), 15, 2, False
        )
        self.window.setTitle_("File Organizer")
        
        # Label
        self.label = NSTextField.alloc().initWithFrame_(NSRect((50, 200), (400, 30)))
        self.label.setStringValue_("Select a folder to organize:")
        self.label.setEditable_(False)
        self.label.setBordered_(False)
        self.label.setBezeled_(False)
        self.label.setDrawsBackground_(False)
        self.window.contentView().addSubview_(self.label)

        # Select Folder Button
        self.select_button = NSButton.alloc().initWithFrame_(NSRect((50, 150), (150, 40)))
        self.select_button.setTitle_("Select Folder")
        self.select_button.setTarget_(self)
        self.select_button.setAction_("selectFolder:")
        self.window.contentView().addSubview_(self.select_button)

        # Organize Button
        self.organize_button = NSButton.alloc().initWithFrame_(NSRect((250, 150), (150, 40)))
        self.organize_button.setTitle_("Organize Files")
        self.organize_button.setTarget_(self)
        self.organize_button.setAction_("organizeFiles:")
        self.window.contentView().addSubview_(self.organize_button)

        self.selected_folder = None  # Store selected folder path

        self.window.makeKeyAndOrderFront_(None)

        NSApp.activateIgnoringOtherApps_(True)


    def selectFolder_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseDirectories_(True)
        panel.setCanChooseFiles_(False)
        panel.setAllowsMultipleSelection_(False)

        if panel.runModal() == 1:
            self.selected_folder = panel.URLs()[0].path()
            self.label.setStringValue_(f"Selected: {self.selected_folder}")

    def organizeFiles_(self, sender):
        if not self.selected_folder:
            self.label.setStringValue_("Please select a folder first.")
            return

        for filename in os.listdir(self.selected_folder):
            file_path = os.path.join(self.selected_folder, filename)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()

                for category, extensions in FILE_TYPES.items():
                    if file_ext in extensions:
                        category_folder = os.path.join(self.selected_folder, category)
                        os.makedirs(category_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(category_folder, filename))
                        break

        self.label.setStringValue_("✅ Files Organized!")

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = FileOrganizerApp.alloc().init()
    app.setDelegate_(delegate)
    AppHelper.runEventLoop()

