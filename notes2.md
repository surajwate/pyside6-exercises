# Creating gui applications with pyside6

## My first Application

The main modules of the Qt are QtWidgets, QtGui and QtCore.

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

#### Storing data

You can store the current state of a widget in a Python variable. You can either store these values as individual variables or use a dictionary if you prefer. In example we store the checked value of our button in a variable called button_is_checked on self.

You can use this same pattern with any PySide6 widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler. In example we're checking the checked state in a pressed handler.

**.isChecked()** returns the check state of the button.

#### Changing the interface

Update our slot methid to modify the button, changing the text and disabling the button so it is no longer chickable. We'll also turn off the checkable state for now.




