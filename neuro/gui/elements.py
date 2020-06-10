from qtpy.QtWidgets import (
    QDoubleSpinBox,
    QPushButton,
    QCheckBox,
    QLabel,
    QSpinBox,
    QComboBox,
)


def add_combobox(layout, label, items, row, column=0):
    combobox = QComboBox()
    combobox.addItems(items)
    layout.addWidget(QLabel(label), row, column)
    layout.addWidget(combobox, row, column + 1)
    return combobox


def add_button(
    label,
    layout,
    connected_function,
    row,
    column,
    visibility=True,
    minimum_width=0,
):
    button = QPushButton(label)
    button.setVisible(visibility)
    button.setMinimumWidth(minimum_width)
    layout.addWidget(button, row, column)
    button.clicked.connect(connected_function)
    return button


def add_checkbox(layout, default, label, row, column=0):
    box = QCheckBox()
    box.setChecked(default)
    layout.addWidget(QLabel(label), row, column)
    layout.addWidget(box, row, column + 1)
    return box


def add_float_box(
    layout, default, minimum, maximum, label, step, row, column=0
):
    box = QDoubleSpinBox()
    box.setMinimum(minimum)
    box.setMaximum(maximum)
    box.setValue(default)
    box.setSingleStep(step)
    layout.addWidget(QLabel(label), row, column)
    layout.addWidget(box, row, column + 1)
    return box


def add_int_box(layout, default, minimum, maximum, label, row, column=0):
    box = QSpinBox()
    box.setMinimum(minimum)
    box.setMaximum(maximum)
    # Not always set if not after min & max
    box.setValue(default)
    layout.addWidget(QLabel(label), row, column)
    layout.addWidget(box, row, column + 1)
    return box