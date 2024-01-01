import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
cwd = os.getcwd()
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
    if "frosty_ats_" in file:
        for file in os.listdir(cwd):
            if "frosty_ats_" in file:
                return file
def getCheckedState(file):
    if file.startswith("INACTIVE_"):
        return Qt.CheckState.Unchecked
    else:
        return Qt.CheckState.Checked
def updateFileState(file, state):
    full_path = os.path.join(cwd, file)
    print(file)
    print(state)
    if state == 2:
        new_file = file.replace("INACTIVE_", "")
        os.rename(file, new_file)
        file = new_file
    if state == 0:
        new_file = "INACTIVE_" + file
        os.rename(file, "INACTIVE_" + file)
        file = new_file
def main():
    while True:
        app = QApplication(sys.argv)
        layout = QVBoxLayout()
        w = QWidget()
        w.resize(250, 200)
        w.move(300, 300)
        w.setWindowTitle("Toggle Active")
        for index, file in enumerate(os.listdir(cwd)):
            if file.endswith(".scs"):
                display_name = file.replace("INACTIVE_", "")
                widget = QCheckBox()
                widget.setCheckState(getCheckedState(file))
                widget.stateChanged.connect(lambda state, file=getCurrentFile(file): updateFileState(getCurrentFile(file), state))
                label = QLabel(display_name)
                vbox = QHBoxLayout()
                vbox.addWidget(widget)
                vbox.addWidget(label)
                layout.addLayout(vbox)
        w.setLayout(layout)
        w.show()
        sys.exit(app.exec())

# Get the current working directory

if __name__ == "__main__":
    main()
'''

cwd = os.getcwd()
if len(sys.argv) == 1:
    for file in os.listdir(cwd):
        if not file.endswith(".py") and not file.endswith(".exe"):
            if file.startswith("INACTIVE_"):
                os.rename(file, file.replace("INACTIVE_", ""))
            else:
                os.rename(file, "INACTIVE_" + file)
else:
    for arg in sys.argv[1:]:
        if arg == "--active":
            for file in os.listdir(cwd):
                if file.startswith("INACTIVE_"):
                    os.rename(file, file.replace("INACTIVE_", ""))
        if arg == "--inactive":
            for file in os.listdir(cwd):
                if not file.endswith(".py") and not file.endswith(".exe"):
                    if not file.startswith("INACTIVE_"):
                        os.rename(file, "INACTIVE_" + file)    
        if arg == "--physics":
            for file in os.listdir(cwd):
                if "physics" in file:
                    if file.startswith("INACTIVE_"):
                        os.rename(file, file.replace("INACTIVE_", ""))
                    else:
                        os.rename(file, "INACTIVE_" + file)
        if arg == "--clean":
            for file in os.listdir(cwd):
                if "clean" in file:
                    if file.startswith("INACTIVE_"):
                        os.rename(file, file.replace("INACTIVE_", ""))
                    else:
                        os.rename(file, "INACTIVE_" + file)
        if arg == "--wheel":
            for file in os.listdir(cwd):
                if "wheel" in file:
                    if file.startswith("INACTIVE_"):
                        os.rename(file, file.replace("INACTIVE_", ""))
                    else:
                        os.rename(file, "INACTIVE_" + file)
        if arg == "--main":
            for file in os.listdir(cwd):
                if "frosty_ats_" in file:
                    if file.startswith("INACTIVE_"):
                        os.rename(file, file.replace("INACTIVE_", ""))
                    else:
                        os.rename(file, "INACTIVE_" + file)
'''