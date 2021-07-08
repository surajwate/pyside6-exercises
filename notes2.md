# Creating gui applications with pyside6
------------------------------------------------------------------------------------------------

## My first Application

The main [modules of the Qt](https://doc.qt.io/qtforpython/modules.html) are [QtWidgets](https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets), [QtGui](https://doc.qt.io/qtforpython/PySide6/QtGui/index.html#module-PySide6.QtGui) and [QtCore](https://doc.qt.io/qtforpython/PySide6/QtCore/index.html#module-PySide6.QtCore).

In Qt all top level widgets are windows - that is, they don't have a parent and are not nested within another widget or layout. This means you can technically create a window using any widget you like.

What is a window?

- Holds the user-interface of your application
- Every application needs at least one (.. but can have more)
- Application will (by default) exit when last window is closed.

What's the event loop?

The core of every Qt Applications is the QApplication class. Every application needs one - and only one - QApplicaiton object to function. This object holds the event loop of your application - the core loop which governs all user interaction with the GUI.

### QMainWindow

As in Qt any widgets can be windows. If you replace QtWidget with QPushButton.

Like that Qt has a very useful widget - **QMainWindow**. This is a pre-made widget which provides a lot of standard window features you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more.

If you want to create a custom window, the best approach is to subclass QMainWindow and then include the setup for the window in the **init** block. This allows the window behavior to be self contained. We can add our own subclass of QMainWindow - call it MainWindow to keep things simple.

### Sizing windows and widgets

In Qt sizes are defined using a QSize object. This accepts width and height parameteres in that order.
As well as .setFixedSize() you can also call .setMinimumSize() and .setMaximumSize() to set the minimum and maximum sizes respectively. You can use these size methods on any widget.

---------------------------------------------------------------------------------------

## Signals & Slots

We need a way to connect the action of pressing the button to making something happen. In Qt, this is provided by signals and slots.

Signals are notifications emitted by widgets when something happens. That something can be any number of things, from pressing a button, to the text of an input box changing, to the text of the window changing. Many signals are initiated by user action, but this is not a rule.
In addition to notifying about something happening, signals can also send data to provide additional context about what happened.

Slots is the name Qt uses for the receivers of signals. In Python any function (or method) in your application can be used as a slot - simply by connecting the signal to it. If the signal sends data, then the receiving function will receive that data too. Many Qt widgets also have their own built-in slots, meaning you can hook Qt widgets together directly.

### QPushButton Signals

We create a simple custom slot named the_button_was_clicked which accepts the clicked signal from the QPushButton.

#### Receiving data

The signals can also send data to provide more information about what has just happened. The .clicked signal also provide a checked (or toggled) state for the button.
Add a second slot which outputs the checkstate.

### Storing data

You can store the current state of a widget in a Python variable. You can either store these values as individual variables or use a dictionary if you prefer. In example we store the checked value of our button in a variable called button_is_checked on self.

You can use this same pattern with any PySide6 widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler. In example we're checking the checked state in a pressed handler.

**.isChecked()** returns the check state of the button.

### Changing the interface

Update our slot methid to modify the button, changing the text and disabling the button so it is no longer chickable. We'll also turn off the checkable state for now.

Most widgets have their own signals - and the **QMainWindow** we're using for our window is no exception. In this example, we connect the **.windowTitleChanged** signal on the **QMainWindow** to a custom shot method the_window_title_changed. This slot also receives the new window title.

The few things to notice in this example.

Firstly, the **windowTitleChanged** signal is not always emitted when setting the window title. The signal only fires if the new title is changed from the precious one. If you set the same title multiple times, the signal will only be fired the first time.

Secondly, notice how we are able to chanin things together using signals. One thing happening - a button press - can trigger multiple other things to happen in turn. These subsequent effects do not need to know what caused them, but simply follow as a consequence of simple rules. This decoupling of effects from their triggers is one of the concepts to understand when building GUI applications.

### Connecting widgets together directly

When a signal is fired from the widget, our Python method is called and receives the data from the signal. But you don't always need to use a Python function to handle signals - you can also connect Qt widgets directly to one another.

In the example, we add a **QLineEdit** widget and a **QLabel** to the window. In the **init** for the window we connect our line edit **.textChanged** signal to the **.setText** method on the **QLabel**. Now any time the text changes in the **QLineEdit** the **QLabel** will receive that text to it's **.setText** method.

Most Qt widgets have slots available, to which you can connect any signal that emits the same type thatt it accepts. The widget documentation has the slots for each widget listed under "Public Slots". For example, see [QLabel](https://doc.qt.io/qt-5/qlabel.html#public-slots).

--------------------------------------------------------------------------------------------

## Widgets

In Qt widget is the name given to a component of UI that the user can interact with. User interfaces are made up of multiole widgets, arranged within the window. Qt comes with a large selection of widgets available, and even allows you to create your own custom widgets.

The widgets in the widgets_list.py are as follows.

| Widget  | What it does  |
|---|---|
| QCheckbox  | A checkbox  |
| QComboBox  | A dropdown list box  |
| QDateEdit  | For editing dates  |
| QDateTimeEdit  | For editing dates and datetimes  |
| QDial  | Rotatable dial  |
| QDoubleSpinbox  | A number spinner for floats  |
| QFontComboBox  | A list of fonts  |
| QLCDNumber  | A list of fonts  |
| QLabel  | Just a label, not interactive  |
| QLineEdit  | Enter a line of text  |
| QProgressBar  | A progress bar  |
| QPushButton  | A button  |
| QRadioButton  | A group with only one active choice  |
| QSlider  | A slider  |
| QSpinBox  | An integer spinner  |
| QTimeEdit  | For editing times  |

For a full list of the widgets see the [Qt documentation](https://doc.qt.io/qt-6/qtwidgets-module.html).

### QLabel

This is a simple one-line piece of text that you can position in your application. You can set the text by passing in a string as you create it -

~~~python
widget = QLabel("Hello")
~~~

Or, by using the .setText() method -

~~~python
widget = QLabel("1") # The label is created with the text 1
widget.setText("2") # The label now show 2
~~~

You can also adjust font parameters, such as the size or alignment of text in the widget.


The flags available for horizontal alignment are :-

| Flag  | Behavior  |
|---|---|
| Qt.AlignLeft  | Aligns with the left edge.  |
| Qt.AlignRight  | Aligns with the right edge.  |
| Qt.AlignHCenter  | Centers horizontally in the available space.  |
| Qt.AlignJustify  | Justifies the text in the available space.  |

The flags available for vertical alignment are - 

| Flag  | Behavior  |
|---|---|
| Qt.AlignTop  | Aligns with the top.  |
| Qt.AlignBottom  | Aligns with the bottom.  |
| Qt.AlignVCenter  | Centers vertically in the available space.  |

The flags to centers in both directions simultaneously - 

| Flag  | Behavior  |
|---|---|
| Qt.AlignCenter  | Centers horizontally and vertically  |


You can also use QLabel to display an image using the .setPixmap() method. This accepts an pixmap (a pixel array), which you can create by passing an image filename to QPixmap. 

### [QCheckBox](https://github.com/surajwate/pyside6-exercises/blob/d7409e565da967c24f8708b21498ef62aa8a06e0/Widgets/check_box_widget.py)

You can set a checkbox state programmatically using **.setChecked** or **.setCheckState**. The former accepts either **True** or **False** representing cehcked or unchecked respectively. However, with **.setCheckState** you also specify a partially checked state using a **Qt**. namespace flag - 

| Flag  | Behavior  |
|---|---|
| Qt.Checked  | Item is checked  |
| Qt.Unchecked  | Item is unchecked  |
| Qt.PartiallyChecked  | Item is partially checked  |

You may notice that when the script is running the current state number is displayed as an int with checked = 2, unchecked = 0, and partially checked = 1. You don't need to remember these values - they are just the internal value of these respective flags. You can test state using state == **Qt.Checked**.

### [QComboBox](https://github.com/surajwate/pyside6-exercises/blob/d7409e565da967c24f8708b21498ef62aa8a06e0/Widgets/combo_box_widget.py)

The QComboBox is a drop down list, closed by default with an arrow to open it. You can select a single item from the list, with the currently selected iten being shown as a label on the widget. The combo box is suited to selection of a choice from a long list of options.

You can add items to a **QComboBox** by passing a list of strings to **.addItems()**. Items will be added in the order they are provided.

### QListWidget

**QListWidget** is similar to **QComboBox**, except options are presented as a scrollable list of items. It also supports selection of multiple items at once. A QListWidget offers an currentItemChanged signal which sends the QListItem (the element of the list widget), and a currentTextChanged signal which sends the text of the current item.

### QLineEdit

The QLineEdit widget is a simple single-line text editing box, into which users can type input. 

























