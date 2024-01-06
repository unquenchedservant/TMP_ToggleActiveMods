import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
cwd = os.getcwd()
def getDisplayName(file):
    if "physics" in file:
        return "Winter Mod - Physics"
    elif "clean" in file:
        return "Winter Mod - Clean Roads"
    elif "wheel" in file:
        return "Winter Mod - Frosty Wheels"
    elif "frosty_ats_" in file or "frosty_v9_7.scs" in file:
        return "Winter Mod"
    else:
        display_name = file.replace("INACTIVE_", "")
        display_name = display_name.replace(".scs", "")
        return display_name
def getCurrentFile(file):
    if "physics" in file:
        for file in os.listdir(cwd):
            if "physics" in file:
                return file
    if "clean" in file:
        for file in os.listdir(cwd):
            if "clean" in file:
                return file
    if "wheel" in file:
        for file in os.listdir(cwd):
            if "wheel" in file:
                return file
    if "frosty_ats_" in file or "frosty_v9_7.scs" in file:
        for file in os.listdir(cwd):
            if "frosty_ats_" in file or "frosty_v9_7.scs" in file:
                return file
        
            
def enableAll(vault_of_checkboxes):
    for checkbox in vault_of_checkboxes:
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.setEnabled(True)
    for file in os.listdir(cwd):
        if file.startswith("INACTIVE_"):
            os.rename(file, file.replace("INACTIVE_", ""))

def disableAll(vault_of_checkboxes):
    for checkbox in vault_of_checkboxes:
        checkbox.setCheckState(Qt.CheckState.Unchecked)
    for file in os.listdir(cwd):
        if not file.endswith(".py") and not file.endswith(".exe"):
            if not file.startswith("INACTIVE_"):
                os.rename(file, "INACTIVE_" + file)

def getCheckedState(file):
    if file.startswith("INACTIVE_"):
        return Qt.CheckState.Unchecked
    else:
        return Qt.CheckState.Checked
def updateFileState(file, state, vault_of_checkboxes):
    if state == 2:
        if "frosty_ats_v" in file or "frosty_v9_7.scs" in file:
            for index, checkbox in enumerate(vault_of_checkboxes):
                if index > 0:
                    checkbox.setEnabled(True)
        new_file = file.replace("INACTIVE_", "")
        os.rename(file, new_file)
        file = new_file
    if state == 0:
        if "frosty_ats_v" in file or "frosty_v9_7.scs" in file:
            disableAll(vault_of_checkboxes)
            for index, checkbox in enumerate(vault_of_checkboxes):
                if index > 0: #this is really janky and assumes that the main file is the first one in the list
                    checkbox.setEnabled(False)
        else:
            new_file = "INACTIVE_" + file
            os.rename(file, "INACTIVE_" + file)
            file = new_file
def main():
    while True:
        vault_of_checkboxes = []
        app = QApplication(sys.argv)
        layout = QVBoxLayout()
        w = QWidget()
        w.resize(250, 200)
        w.move(300, 300)
        w.setWindowTitle("Toggle Active")
        for index, file in enumerate(os.listdir(cwd)):
            if file.endswith(".scs"):
                display_name = getDisplayName(file.replace("INACTIVE_", ""))
                widget = QCheckBox()
                widget.setCheckState(getCheckedState(file))
                widget.stateChanged.connect(lambda state, file=getCurrentFile(file): updateFileState(getCurrentFile(file), state, vault_of_checkboxes))
                vault_of_checkboxes.append(widget)
                label = QLabel(display_name)
                vbox = QHBoxLayout()
                vbox.addWidget(widget)
                vbox.addWidget(label)
                layout.addLayout(vbox)
        button_vbox = QVBoxLayout()
        quick_enable_btn = QPushButton("Enable All")
        quick_enable_btn.clicked.connect(lambda: enableAll(vault_of_checkboxes))
        quick_disable_btn = QPushButton("Disable All")
        quick_disable_btn.clicked.connect(lambda: disableAll(vault_of_checkboxes))
        button_vbox.addWidget(quick_enable_btn)
        button_vbox.addWidget(quick_disable_btn)                
        layout.addLayout(button_vbox)        
        w.setLayout(layout)
        w.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
