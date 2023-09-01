import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class SimpleGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and dimensions
        self.setWindowTitle("Simple PyQt6 GUI")
        self.setGeometry(100, 100, 400, 200)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Create a label and button
        self.label = QLabel("Hello, World!")
        self.button = QPushButton("Click Me!")

        # Connect button click event to a function
        self.button.clicked.connect(self.change_label_text)

        # Add label and button to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def change_label_text(self):
        self.label.setText("Button Clicked!")


def main():
    app = QApplication(sys.argv)
    window = SimpleGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
