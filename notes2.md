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



















