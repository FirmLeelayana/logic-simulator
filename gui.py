"""Implement the graphical user interface for the Logic Simulator.

Used in the Logic Simulator project to enable the user to run the simulation
or adjust the network properties.

Classes:
--------
MyGLCanvas - handles all canvas drawing operations.
Gui - configures the main window and all the widgets.
"""
import wx
import wx.glcanvas as wxcanvas
import numpy as np
import math
from OpenGL import GL, GLU, GLUT

from names import Names
from devices import Devices
from network import Network
from monitors import Monitors
from scanner import Scanner
from parse import Parser


class MyGLCanvas(wxcanvas.GLCanvas):
    """Handle all drawing operations.

    This class contains functions for drawing onto the canvas. It
    also contains handlers for events relating to the canvas.

    Parameters
    ----------
    parent: parent window.
    devices: instance of the devices.Devices() class.
    monitors: instance of the monitors.Monitors() class.
    size: size of canvas.

    Public methods
    --------------
    init_gl(self): Configures the OpenGL context.

    render(self, text): Handles all drawing operations.

    draw_cuboid(self, x_pos, z_pos, half_width,
                half_depth, height): Draw a cuboid signal

    on_paint(self, event): Handles the paint event.

    on_size(self, event): Handles the canvas resize event.

    on_mouse(self, event): Handles mouse events.

    render_text(self, text, x_pos, y_pos, z_pos): Handles text drawing
                                           operations.
    """

    def __init__(self, parent, devices, monitors, size):
        """Initialise canvas properties and useful variables."""
        super().__init__(parent, -1, size=size,
                         attribList=[wxcanvas.WX_GL_RGBA,
                                     wxcanvas.WX_GL_DOUBLEBUFFER,
                                     wxcanvas.WX_GL_DEPTH_SIZE, 16, 0])
        GLUT.glutInit()
        self.init = False
        self.context = wxcanvas.GLContext(self)

        self.devices = devices
        self.monitors = monitors
        self.cycles_completed = 0
        self.dotted = False
        self.dimension = True   # 3D by default

        # Constants for OpenGL materials and lights
        self.mat_diffuse = [0.0, 0.0, 0.0, 1.0]
        self.mat_no_specular = [0.0, 0.0, 0.0, 0.0]
        self.mat_no_shininess = [0.0]
        self.mat_specular = [0.5, 0.5, 0.5, 1.0]
        self.mat_shininess = [50.0]
        self.top_right = [1.0, 1.0, 1.0, 0.0]
        self.straight_on = [0.0, 0.0, 1.0, 0.0]
        self.no_ambient = [0.0, 0.0, 0.0, 1.0]
        self.dim_diffuse = [0.5, 0.5, 0.5, 1.0]
        self.bright_diffuse = [1.0, 1.0, 1.0, 1.0]
        self.med_diffuse = [0.75, 0.75, 0.75, 1.0]
        self.full_specular = [0.5, 0.5, 0.5, 1.0]
        self.no_specular = [0.0, 0.0, 0.0, 1.0]

        # Initialise variables for panning
        self.pan_x = 0
        self.pan_y = 0
        self.last_mouse_x = 0  # previous mouse x position
        self.last_mouse_y = 0  # previous mouse y position

        # Initialise the scene rotation matrix
        self.scene_rotate = np.identity(4, 'f')

        # Initialise variables for zooming
        self.zoom = 1
        self.zoom_2d = 1
        self.zoom_3d = 1

        # Offset between viewpoint and origin of the scene
        self.depth_offset = 1000

        # Bind events to the canvas
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.on_mouse)

    def init_gl(self):
        """Configure and initialise the OpenGL context."""
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)  # White canvas

        if self.dimension:  # 3D initialisation
            GL.glViewport(0, 0, size.width, size.height)
            GL.glMatrixMode(GL.GL_PROJECTION)
            GL.glLoadIdentity()
            GLU.gluPerspective(45, size.width / size.height, 10, 10000)

            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()  # lights positioned relative to the viewer
            GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, self.no_ambient)
            GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, self.med_diffuse)
            GL.glLightfv(GL.GL_LIGHT0, GL.GL_SPECULAR, self.no_specular)
            GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, self.top_right)
            GL.glLightfv(GL.GL_LIGHT1, GL.GL_AMBIENT, self.no_ambient)
            GL.glLightfv(GL.GL_LIGHT1, GL.GL_DIFFUSE, self.dim_diffuse)
            GL.glLightfv(GL.GL_LIGHT1, GL.GL_SPECULAR, self.no_specular)
            GL.glLightfv(GL.GL_LIGHT1, GL.GL_POSITION, self.straight_on)
            GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, self.mat_specular)
            GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, self.mat_shininess)
            GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT_AND_DIFFUSE,
                            self.mat_diffuse)
            GL.glColorMaterial(GL.GL_FRONT, GL.GL_AMBIENT_AND_DIFFUSE)

            GL.glDepthFunc(GL.GL_LEQUAL)
            GL.glShadeModel(GL.GL_SMOOTH)
            GL.glDrawBuffer(GL.GL_BACK)
            GL.glCullFace(GL.GL_BACK)
            GL.glEnable(GL.GL_COLOR_MATERIAL)
            GL.glEnable(GL.GL_CULL_FACE)
            GL.glEnable(GL.GL_DEPTH_TEST)
            GL.glEnable(GL.GL_LIGHTING)
            GL.glEnable(GL.GL_LIGHT0)
            GL.glEnable(GL.GL_LIGHT1)
            GL.glEnable(GL.GL_NORMALIZE)

            # Viewing transformation - set the viewpoint back from the scene
            GL.glTranslatef(0.0, 0.0, -self.depth_offset)

            # Modelling transformation - pan, zoom and rotate
            GL.glTranslatef(self.pan_x, self.pan_y, 0.0)
            GL.glMultMatrixf(self.scene_rotate)
            GL.glScalef(self.zoom, self.zoom, self.zoom)

        else:  # 2D initialisation
            GL.glDrawBuffer(GL.GL_BACK)
            GL.glClearColor(1.0, 1.0, 1.0, 0.0)
            GL.glViewport(0, 0, size.width, size.height)
            GL.glMatrixMode(GL.GL_PROJECTION)
            GL.glLoadIdentity()
            GL.glOrtho(0, size.width, 0, size.height, -1, 1)
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()
            GL.glTranslated(self.pan_x, self.pan_y, 0.0)
            GL.glScalef(self.zoom, self.zoom, self.zoom)

    def render(self, text, cycles=0, useful_monitors={}, dotted=None,
               dimension=False):
        """Handle all drawing operations."""
        if cycles > 0:
            self.cycles_completed = cycles
            self.useful_monitors = useful_monitors
        if dotted:
            self.dotted = not self.dotted
        if dimension:
            self.dimension = not self.dimension
            # Save zoom values
            if not self.dimension:
                self.zoom_3d = self.zoom
                self.zoom = self.zoom_2d
            else:
                self.zoom_2d = self.zoom
                self.zoom = self.zoom_3d
            self.init = False
            self.Refresh()
        self.SetCurrent(self.context)
        if not self.init:
            # Configure the viewport, modelview and projection matrices
            self.init_gl()
            self.init = True
        # Get longest monitor name for offset of labels
        margin = self.monitors.get_margin()
        if not margin:
            margin = 0

        if self.dimension:  # 3D Trace
            # Clear everything
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            # Initialise signal parameters
            cycle_width = 20
            monitor_spacing = 30
            range_start = (self.cycles_completed // 2) * -1
            range_end = range_start + self.cycles_completed
            label_offset = range_start * cycle_width - 10 - margin * 8
            x_start = -1 * cycle_width
            y_val = 0
            z_start = cycle_width * (range_start - 0.5)
            z_end = cycle_width * (range_end + 1 - 0.5)
            tick = 3
            if self.cycles_completed > 0:
                # Draw z axis
                GL.glColor3f(0.0, 0.0, 0.0)  # axis trace is black
                GL.glLineWidth(2)
                GL.glBegin(GL.GL_LINES)
                GL.glVertex3f(x_start, y_val, z_start)
                GL.glVertex3f(x_start, y_val, z_end)
                for i in range(self.cycles_completed + 1):
                    GL.glVertex3f(x_start + tick, y_val,
                                  z_start + cycle_width * i)
                    GL.glVertex3f(x_start - tick, y_val,
                                  z_start + cycle_width * i)
                # Draw arrow at end of axis
                GL.glVertex3f(x_start, y_val, z_end)
                GL.glVertex3f(x_start + tick * 2, y_val,
                              z_end - cycle_width / 2)
                GL.glVertex3f(x_start, y_val, z_end)
                GL.glVertex3f(x_start - tick * 2, y_val,
                              z_end - cycle_width / 2)
                GL.glEnd()
                # Add labels for axis
                self.render_text("Time", x_start, y_val, label_offset)
                for i in range(self.cycles_completed + 1):
                    self.render_text(str(i), x_start - 10, y_val,
                                     z_start + cycle_width * i)

                # Draw signals based on specified monitors
                for i in range(len(self.useful_monitors)):
                    key = list(self.useful_monitors.keys())[i]
                    signal_list = self.useful_monitors[key]
                    if i == len(self.useful_monitors) - 1:
                        x_max = i * monitor_spacing
                    for j in range(range_start, range_end):
                        z = j * cycle_width
                        self.render_text(key, i * monitor_spacing,
                                         y_val, label_offset)
                        GL.glColor3f(.051, .702, .62)
                        if signal_list[j - range_start] == self.devices.HIGH:
                            self.draw_cuboid(i * monitor_spacing,
                                             z, 5, 10, 11)
                        elif signal_list[j - range_start] == self.devices.LOW:
                            self.draw_cuboid(i * monitor_spacing,
                                             z, 5, 10, 1)

                # Draw dotted lines on monitors
                if self.dotted:
                    GL.glPushAttrib(GL.GL_ENABLE_BIT)
                    GL.glLineStipple(2, 0x0C0F)
                    GL.glEnable(GL.GL_LINE_STIPPLE)
                    GL.glLineWidth(0.5)
                    GL.glColor3f(.173, .412, .604)
                    GL.glBegin(GL.GL_LINES)
                    for i in range(self.cycles_completed + 1):
                        GL.glVertex3f(x_start, y_val,
                                      z_start + cycle_width * i)
                        GL.glVertex3f(x_max + monitor_spacing, y_val,
                                      z_start + cycle_width * i)
                    GL.glEnd()
                    GL.glPopAttrib()

        else:  # 2D Trace
            # Clear everything
            GL.glClear(GL.GL_COLOR_BUFFER_BIT)
            if self.cycles_completed > 0:
                # Draw x axis
                GL.glColor3f(0.0, 0.0, 0.0)  # axis trace is black
                GL.glLineWidth(2)
                cycle_width = 25
                y_val = 60
                if margin:
                    x_start = 100 + 5 * margin
                else:
                    x_start = 100
                x_end = x_start + cycle_width*(self.cycles_completed + 1)
                tick = 3
                GL.glBegin(GL.GL_LINES)
                GL.glVertex2f(x_start, y_val)
                GL.glVertex2f(x_end, y_val)
                for i in range(self.cycles_completed + 1):
                    GL.glVertex2f(x_start + cycle_width*i, y_val + tick)
                    GL.glVertex2f(x_start + cycle_width*i, y_val - tick)
                # Draw arrow at end of axis
                GL.glVertex2f(x_end, y_val)
                GL.glVertex2f(x_end - 10, y_val + 5)
                GL.glVertex2f(x_end, y_val)
                GL.glVertex2f(x_end - 10, y_val - 5)
                GL.glEnd()
                # Add labels for axis
                self.render_text("Time", 10, y_val - 5)
                for i in range(self.cycles_completed + 1):
                    self.render_text(str(i),
                                     x_start + cycle_width*i - 5,
                                     y_val - 15)

                # Draw signals based on specified monitors
                y_start = y_val + 100
                for i in range(len(self.useful_monitors)):
                    key = list(self.useful_monitors.keys())[i]
                    height = y_start + i*100
                    self.render_text(key, 10, height - 30)
                    self.render_text("1", x_start - 15, height - 5)
                    self.render_text("0", x_start - 15, height - 55)
                    signal_list = self.useful_monitors[key]
                    if i == len(self.useful_monitors) - 1:
                        max_height = height
                    GL.glColor3f(.051, .702, .62)
                    GL.glBegin(GL.GL_LINE_STRIP)
                    for j in range(self.cycles_completed):
                        if signal_list[j] == self.devices.HIGH:
                            GL.glVertex2f((j * cycle_width) + x_start, height)
                            GL.glVertex2f(((j + 1) * cycle_width)
                                          + x_start, height)
                        elif signal_list[j] == self.devices.LOW:
                            GL.glVertex2f((j * cycle_width) + x_start,
                                          height - 50)
                            GL.glVertex2f(((j + 1) * cycle_width)
                                          + x_start, height - 50)
                        elif signal_list[j] == self.devices.RISING:
                            GL.glVertex2f((j * cycle_width) + x_start, height)
                            GL.glVertex2f(((j + 1) * cycle_width)
                                          + x_start, height - 50)
                        elif signal_list[j] == self.devices.FALLING:
                            GL.glVertex2f((j * cycle_width) + x_start,
                                          height - 50)
                            GL.glVertex2f(((j + 1) * cycle_width)
                                          + x_start, height)
                    GL.glEnd()

                # Draw dotted lines on monitors
                if self.dotted:
                    GL.glPushAttrib(GL.GL_ENABLE_BIT)
                    GL.glLineStipple(2, 0x0C0F)
                    GL.glEnable(GL.GL_LINE_STIPPLE)
                    GL.glLineWidth(0.5)
                    GL.glColor3f(.173, .412, .604)
                    GL.glBegin(GL.GL_LINES)
                    for i in range(self.cycles_completed + 1):
                        GL.glVertex2f(x_start + cycle_width*i, y_val)
                        GL.glVertex2f(x_start + cycle_width*i, max_height + 20)
                    GL.glEnd()
                    GL.glPopAttrib()

        # We have been drawing to the back buffer, flush the graphics pipeline
        # and swap the back buffer to the front
        GL.glFlush()
        self.SwapBuffers()

    def draw_cuboid(self, x_pos, z_pos, half_width, half_depth, height):
        """Draw a cuboid, the basic building block for all signals.

        Draw a cuboid at the specified position, with the specified
        dimensions.
        """
        GL.glBegin(GL.GL_QUADS)
        GL.glNormal3f(0, -1, 0)
        GL.glVertex3f(x_pos - half_width, -6, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6, z_pos + half_depth)
        GL.glVertex3f(x_pos - half_width, -6, z_pos + half_depth)
        GL.glNormal3f(0, 1, 0)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos + half_depth)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos + half_depth)
        GL.glNormal3f(-1, 0, 0)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos - half_width, -6, z_pos - half_depth)
        GL.glVertex3f(x_pos - half_width, -6, z_pos + half_depth)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos + half_depth)
        GL.glNormal3f(1, 0, 0)
        GL.glVertex3f(x_pos + half_width, -6, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos + half_depth)
        GL.glVertex3f(x_pos + half_width, -6, z_pos + half_depth)
        GL.glNormal3f(0, 0, -1)
        GL.glVertex3f(x_pos - half_width, -6, z_pos - half_depth)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos - half_depth)
        GL.glVertex3f(x_pos + half_width, -6, z_pos - half_depth)
        GL.glNormal3f(0, 0, 1)
        GL.glVertex3f(x_pos - half_width, -6 + height, z_pos + half_depth)
        GL.glVertex3f(x_pos - half_width, -6, z_pos + half_depth)
        GL.glVertex3f(x_pos + half_width, -6, z_pos + half_depth)
        GL.glVertex3f(x_pos + half_width, -6 + height, z_pos + half_depth)
        GL.glEnd()

    def on_paint(self, event):
        """Handle the paint event."""
        self.SetCurrent(self.context)
        if not self.init:
            # Configure the viewport, modelview and projection matrices
            self.init_gl()
            self.init = True
        self.render("")

    def on_size(self, event):
        """Handle the canvas resize event."""
        # Forces reconfiguration of the viewport, modelview and projection
        # matrices on the next paint event
        self.init = False

    def on_mouse(self, event):
        """Handle mouse events."""
        # Calculate object coordinates of the mouse position
        if event.ButtonDown():
            self.last_mouse_x = event.GetX()
            self.last_mouse_y = event.GetY()

        if event.Dragging():
            if self.dimension:
                # Drag in 3D mode is a rotation
                GL.glMatrixMode(GL.GL_MODELVIEW)
                GL.glLoadIdentity()
                x = event.GetX() - self.last_mouse_x
                y = event.GetY() - self.last_mouse_y
                if event.LeftIsDown():
                    GL.glRotatef(math.sqrt((x * x) + (y * y)), y, x, 0)
                if event.MiddleIsDown():
                    GL.glRotatef((x + y), 0, 0, 1)
                if event.RightIsDown():
                    self.pan_x += x
                    self.pan_y -= y
                GL.glMultMatrixf(self.scene_rotate)
                GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX, self.scene_rotate)
            else:
                # Drag in 2D mode is a translation
                self.pan_x += event.GetX() - self.last_mouse_x
                self.pan_y -= event.GetY() - self.last_mouse_y
            self.last_mouse_x = event.GetX()
            self.last_mouse_y = event.GetY()
            self.init = False

        if event.GetWheelRotation() < 0:
            self.zoom *= (1.0 + (
                event.GetWheelRotation() / (20 * event.GetWheelDelta())))
            self.init = False

        if event.GetWheelRotation() > 0:
            self.zoom /= (1.0 - (
                event.GetWheelRotation() / (20 * event.GetWheelDelta())))
            self.init = False

        self.Refresh()  # triggers the paint event

    def render_text(self, text, x_pos, y_pos, z_pos=0):
        """Handle text drawing operations."""
        GL.glColor3f(0.0, 0.0, 0.0)  # text is black
        GL.glRasterPos3f(x_pos, y_pos, z_pos)
        font = GLUT.GLUT_BITMAP_HELVETICA_12

        for character in text:
            if character == '\n':
                y_pos = y_pos - 20
                GL.glRasterPos3f(x_pos, y_pos, z_pos)
            else:
                GLUT.glutBitmapCharacter(font, ord(character))
        GL.glEnable(GL.GL_LIGHTING)


class Gui(wx.Frame):
    """Configure the main window and all the widgets.

    This class provides a graphical user interface for the Logic Simulator and
    enables the user to change the circuit properties and run simulations.

    Parameters
    ----------
    title: title of the window.
    path: path of definition file
    names: instance of the names.Names() class.
    devices: instance of the devices.Devices() class.
    network: instance of the network.Network() class.
    monitors: instance of the monitors.Monitors() class.

    Public methods
    --------------
    on_menu(self, event): Event handler for the file menu.

    on_run_button(self, event): Event handler for when the user clicks the run
                                button.

    on_continue_button(self, event): Event handler for when the user clicks the
                                     continue button.

    on_quit_button(self, event): Event handler for when the user clicks the
                                 quit button.

    toggle_switch(self, switch_id): Event handler for when the user toggles
                                    a switch.

    on_remove_button(self, monitor): Event handler for when the user clicks a
                                     clear button.

    on_add_monitor_button(self, event): Event handler for when the user clicks
                                        the add monitor button.

    on_dotted_button(self, event): Event handler for when the user clicks the
                                   add dotted lines button.

    on_dimension_button(self, event): Event handler for when the user clicks
                                      the dimension button.

    build_gui_monitor_dictionary(self): Converts monitors.dictionary to
                                        a more useful dictionary for the GUI.
    """

    def __init__(self, title, path, names, devices, network, monitors):
        """Initialise GUI properties and useful variables."""
        self.names = names
        self.devices = devices
        self.monitors = monitors
        self.network = network

        self.cycles_completed = 0  # number of simulation cycles completed
        self.monitored_list = self.monitors.get_signal_names()[0]
        self.not_monitored_list = self.monitors.get_signal_names()[1]

        """Initialise widgets and layout."""
        super().__init__(parent=None, title=title, size=(800, 600))

        # Configure the file menu
        fileMenu = wx.Menu()
        menuBar = wx.MenuBar()
        fileMenu.Append(wx.ID_ANY, _(u"&New definition file..."))
        fileMenu.Append(wx.ID_ABOUT, _(u"&About"))
        menuBar.Append(fileMenu, _(u"&File"))
        self.SetMenuBar(menuBar)

        # Set Scrollable canvas
        self.scrollable = wx.ScrolledCanvas(self, wx.ID_ANY)
        self.scrollable.SetSizeHints(200, 200)
        length, height = 800, 600
        self.scrollable.SetScrollbars(10, 10, length//10, height//10)

        # Canvas for drawing signals
        self.canvas = MyGLCanvas(self.scrollable, devices,
                                 monitors, wx.Size(length, height))

        # Configure sizers for window
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.side_sizer = wx.BoxSizer(wx.VERTICAL)

        # Configure the widgets for side_sizer
        self.text_cycles = wx.StaticText(self, wx.ID_ANY, _(u"Cycles:"))
        self.spin = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1)
        self.run_button = wx.Button(self, wx.ID_ANY, _(u"Run"))
        self.continue_button = wx.Button(self, wx.ID_ANY, _(u"Continue"))
        self.quit_button = wx.Button(self, wx.ID_ANY, _(u"Quit"))
        self.text_switches = wx.StaticText(self, wx.ID_ANY, _(u"Switches:"))
        self.text_monitors = wx.StaticText(self,
                                           wx.ID_ANY, _(u"Monitor Points:"))
        self.dotted_button = wx.Button(self,
                                       wx.ID_ANY, _(u"Toggle dotted lines"))
        self.dimension_button = wx.Button(self, wx.ID_ANY,
                                          _(u"Switch to 2D Monitors"))

        # Configure sizer children for side_sizer
        self.item_cycles = wx.BoxSizer(wx.HORIZONTAL)
        self.item_run = wx.BoxSizer(wx.HORIZONTAL)
        self.item_text_switches = wx.BoxSizer(wx.HORIZONTAL)
        self.item_switches = wx.BoxSizer(wx.VERTICAL)
        self.item_text_monitors = wx.BoxSizer(wx.HORIZONTAL)
        self.item_monitors = wx.BoxSizer(wx.VERTICAL)
        self.item_dotted = wx.BoxSizer(wx.HORIZONTAL)

        # Configure sizer children for monitor_window
        self.monitor_dropdown = wx.BoxSizer(wx.HORIZONTAL)

        # Configure item_cycles sizer, child to side_sizer
        self.item_cycles.Add(self.text_cycles, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        self.item_cycles.Add(self.spin, 3, wx.ALL, 5)

        # Configure item_run sizer, child to side_sizer
        self.item_run.Add(self.run_button, 1, wx.ALL, 5)
        self.item_run.Add(self.continue_button, 1, wx.ALL, 5)
        self.item_run.Add(self.quit_button, 1, wx.ALL, 5)

        # Configure item_text_switches sizer, child to side_sizer
        self.item_text_switches.Add(self.text_switches, 1, wx.ALL, 5)

        # Configure scrollable switch_window, child to side_sizer
        self.switch_window = wx.ScrolledWindow(self, style=wx.VSCROLL)
        self.switch_window.SetSizer(self.item_switches)
        self.switch_window.SetScrollRate(10, 10)
        self.switch_window.SetAutoLayout(True)
        switches = self.devices.find_devices(self.devices.SWITCH)

        for switch_id in switches:
            self.switch_subitem = wx.BoxSizer(wx.HORIZONTAL)
            self.item_switches.Add(self.switch_subitem, 0, 0, 0)
            label = self.names.get_name_string(switch_id)
            self.switch_text = wx.StaticText(self.switch_window,
                                             wx.ID_ANY,
                                             label)
            switch_state = self.devices.get_device(switch_id).switch_state

            if switch_state == 0:
                self.switch_button = wx.Button(self.switch_window,
                                               wx.ID_ANY, _(u"OFF"))
                self.switch_button.SetBackgroundColour(wx.Colour(255, 69, 0))
            else:
                self.switch_button = wx.Button(self.switch_window,
                                               wx.ID_ANY, _(u"ON"))
                self.switch_button.SetBackgroundColour(wx.Colour(42, 145, 52))
            self.switch_button.Bind(wx.EVT_BUTTON,
                                    self.toggle_switch(switch_id))
            self.switch_subitem.Add(self.switch_text, 1,
                                    wx.ALIGN_CENTER | wx.ALL, 5)
            self.switch_subitem.Add(self.switch_button, 0, wx.ALL, 5)

        # Configure item_text_monitors sizer, child to side_sizer
        self.item_text_monitors.Add(self.text_monitors, 1, wx.ALL, 5)

        # Configure scrollable monitor_window, child to side_sizer
        self.monitor_window = wx.ScrolledWindow(self, style=wx.VSCROLL)
        self.monitor_window.SetSizer(self.item_monitors)
        self.monitor_window.SetScrollRate(10, 10)
        self.monitor_window.SetAutoLayout(True)
        self.monitor_combo = wx.ComboBox(self.monitor_window,
                                         wx.ID_ANY,
                                         choices=self.not_monitored_list,
                                         style=wx.CB_READONLY)
        self.add_monitor_button = wx.Button(self.monitor_window,
                                            wx.ID_ANY, _(u"Add Monitor"))
        self.item_monitors.Add(self.monitor_dropdown, 0, 0, 0)
        self.monitor_dropdown.Add(self.add_monitor_button, 0, wx.LEFT, 5)
        self.monitor_dropdown.Add(self.monitor_combo, 1, wx.LEFT, 5)

        self.monitored_list = self.monitors.get_signal_names()[0]
        for monitor in self.monitored_list:
            self.monitor_subitem = wx.BoxSizer(wx.HORIZONTAL)
            self.item_monitors.Add(self.monitor_subitem, 0, 0, 0)
            self.new_monitor_text = wx.StaticText(self.monitor_window,
                                                  wx.ID_ANY, monitor)
            self.new_monitor_button = wx.Button(self.monitor_window,
                                                wx.ID_ANY, _(u"Clear"))
            self.new_monitor_button.SetBackgroundColour(wx.Colour(255, 69, 0))
            self.new_monitor_button.Bind(wx.EVT_BUTTON,
                                         self.on_remove_button(monitor))
            self.monitor_subitem.Add(self.new_monitor_button, 0, wx.ALL, 5)
            self.monitor_subitem.Add(self.new_monitor_text,
                                     1, wx.ALIGN_CENTER | wx.ALL, 5)

        # Configure item_dotted sizer, child to side_sizer
        self.item_dotted.Add(self.dotted_button, 0, wx.ALL, 5)
        self.item_dotted.Add(self.dimension_button, 0, wx.ALL, 5)

        # Add main_sizer children
        self.main_sizer.Add(self.scrollable, 1, wx.EXPAND + wx.TOP, 5)
        self.main_sizer.Add(self.side_sizer, 0, wx.ALL, 5)

        # Add side_sizer children
        self.side_sizer.Add(self.item_cycles, 1, wx.ALL, 5)
        self.side_sizer.Add(self.item_run, 1, wx.ALL, 5)
        self.side_sizer.Add(self.item_text_switches, 1, wx.ALL, 5)
        self.side_sizer.Add(self.switch_window, 3, wx.EXPAND | wx.ALL, 5)
        self.side_sizer.Add(self.item_text_monitors, 1, wx.ALL, 5)
        self.side_sizer.Add(self.monitor_window, 3, wx.EXPAND | wx.ALL, 5)
        self.side_sizer.Add(self.item_dotted, 1, wx.ALL, 5)

        # Bind events to widgets
        self.Bind(wx.EVT_MENU, self.on_menu)
        self.run_button.Bind(wx.EVT_BUTTON, self.on_run_button)
        self.continue_button.Bind(wx.EVT_BUTTON, self.on_continue_button)
        self.quit_button.Bind(wx.EVT_BUTTON, self.on_quit_button)
        self.add_monitor_button.Bind(wx.EVT_BUTTON, self.on_add_monitor_button)
        self.dotted_button.Bind(wx.EVT_BUTTON, self.on_dotted_button)
        self.dimension_button.Bind(wx.EVT_BUTTON, self.on_dimension_button)

        # Set GUI properties
        self.run_button.SetBackgroundColour(wx.Colour(42, 145, 52))
        self.continue_button.SetBackgroundColour(wx.Colour(175, 238, 238))
        self.quit_button.SetBackgroundColour(wx.Colour(255, 69, 0))

        self.SetSizeHints(1000, 600)
        self.SetSizer(self.main_sizer)
        sizer_window = self.main_sizer.GetContainingWindow()
        sizer_window.SetBackgroundColour(wx.Colour(22, 219, 147))

    def on_menu(self, event):
        """Handle the event when the user selects a menu item."""
        Id = event.GetId()
        if Id == wx.ID_EXIT:
            self.Close(True)
        if Id == wx.ID_ABOUT:
            wx.MessageBox(_(u"Logic Simulator\nScanner by Firm Leelayana\n"
                            "Parser by Sense Sunyabhisithkul\n"
                            "GUI Skeleton by Mojisola Agboola\n"
                            "GUI by Shazril Suhail\n2021"),
                          _(u"About the Logic Simulator"),
                          wx.ICON_INFORMATION | wx.OK)
        else:
            names = Names()
            devices = Devices(names)
            network = Network(names, devices)
            monitors = Monitors(names, devices, network)
            openFileDialog = wx.FileDialog(self, _(u"Open txt file"), "", "",
                                           wildcard="TXT files (*.txt)|*.txt",
                                           style=wx.FD_OPEN +
                                           wx.FD_FILE_MUST_EXIST)
            if openFileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = openFileDialog.GetPath()
            scanner = Scanner(path, names)
            parser = Parser(names, devices, network, monitors, scanner)
            if parser.parse_network():
                self.main_sizer.GetContainingWindow().Close()
                app = wx.App()
                gui = Gui("Logic Simulator", path, names, devices, network,
                          monitors)
                gui.Show(True)
                app.MainLoop()
            else:
                full_error_message = "".join(parser.error_messages)
                error_app = wx.App()
                error = ErrorWindow("Error!", full_error_message)
                error.Show(True)
                error_app.MainLoop()

    def on_run_button(self, event):
        """Handle the event when the user clicks the run button."""
        self.cycles_completed = 0
        cycles = self.spin.GetValue()
        self.monitored_list = self.monitors.get_signal_names()[0]
        self.monitors.reset_monitors()
        self.devices.cold_startup()
        for _ in range(cycles):
            if self.network.execute_network():
                self.monitors.record_signals()
                self.cycles_completed += 1
        self.useful_monitors = self.build_gui_monitor_dictionary()
        self.canvas.render("", self.cycles_completed, self.useful_monitors)

    def on_continue_button(self, event):
        """Handle the event when the user clicks the continue button."""
        if self.cycles_completed > 0:
            cycles = self.spin.GetValue()
            self.monitored_list = self.monitors.get_signal_names()[0]
            for _ in range(cycles):
                if self.network.execute_network():
                    self.monitors.record_signals()
                    self.cycles_completed += 1
            self.useful_monitors = self.build_gui_monitor_dictionary()
            self.canvas.render("", self.cycles_completed,
                               self.useful_monitors)

    def on_quit_button(self, event):
        """Handle the event when the user clicks the run button."""
        self.main_sizer.GetContainingWindow().Close()

    def toggle_switch(self, switch_id):
        """Handle the event when the user toggles a switch."""
        def switch_change(event):
            switch_object = event.GetEventObject()
            if switch_object.GetLabel() == _(u"ON"):
                current_state = 1
            else:
                current_state = 0
            new_state = 1 - current_state
            self.devices.set_switch(switch_id, new_state)
            if new_state == 0:
                switch_object.SetBackgroundColour(wx.Colour(255, 69, 0))
                switch_object.SetLabel(_(u"OFF"))
            else:
                switch_object.SetBackgroundColour(wx.Colour(42, 145, 52))
                switch_object.SetLabel(_(u"ON"))
        return switch_change

    def on_remove_button(self, monitor):
        """Handle the event when the user clicks a remove button."""
        def on_button_click(event):
            subitem = event.GetEventObject().GetContainingSizer()
            self.item_monitors.Hide(subitem)
            self.item_monitors.Remove(subitem)
            [device_id, output_id] = self.devices.get_signal_ids(monitor)
            self.monitors.remove_monitor(device_id, output_id)
            self.not_monitored_list = self.monitors.get_signal_names()[1]
            self.monitor_combo.SetItems(self.not_monitored_list)
            self.item_monitors.Layout()
            self.main_sizer.Layout()
        return on_button_click

    def on_add_monitor_button(self, event):
        """Handle the event when the user clicks the add monitor button."""
        monitor = self.monitor_combo.GetStringSelection()
        if monitor:
            [device_id, output_id] = self.devices.get_signal_ids(monitor)
            self.monitors.make_monitor(device_id,
                                       output_id, self.cycles_completed)
            self.not_monitored_list = self.monitors.get_signal_names()[1]
            self.monitor_combo.SetItems(self.not_monitored_list)

            self.monitor_subitem = wx.BoxSizer(wx.HORIZONTAL)
            self.item_monitors.Add(self.monitor_subitem, 0, 0, 0)

            self.new_monitor_text = wx.StaticText(self.monitor_window,
                                                  wx.ID_ANY,
                                                  monitor)
            self.new_monitor_button = wx.Button(self.monitor_window,
                                                wx.ID_ANY, _(u"Clear"))
            self.new_monitor_button.SetBackgroundColour(wx.Colour(255, 69, 0))
            self.new_monitor_button.Bind(wx.EVT_BUTTON,
                                         self.on_remove_button(monitor))
            self.monitor_subitem.Add(self.new_monitor_button, 0, wx.ALL, 5)
            self.monitor_subitem.Add(self.new_monitor_text,
                                     1, wx.ALIGN_CENTER | wx.ALL, 5)
            self.main_sizer.Layout()

    def on_dotted_button(self, event):
        """Handle the event when the user clicks the add dotted line button."""
        self.canvas.render("Dotted lines toggled", dotted=True)

    def on_dimension_button(self, event):
        """Handle the event when the user clicks the dimension button."""
        button_object = event.GetEventObject()
        if button_object.GetLabel() == _(u"Switch to 2D Monitors"):  # 3D Mode
            button_object.SetLabel(_(u"Switch to 3D Monitors"))
        else:
            button_object.SetLabel(_(u"Switch to 2D Monitors"))
        self.canvas.render("", dimension=True)

    def build_gui_monitor_dictionary(self):
        """Convert monitors.dictionary to a more useful dictionary."""
        new_dict = {}
        for device_id, output_id in self.monitors.monitors_dictionary:
            monitor_name = self.devices.get_signal_name(device_id, output_id)
            value = self.monitors.monitors_dictionary[(device_id, output_id)]
            new_dict[monitor_name] = value
        return new_dict


class ErrorWindow(wx.Frame):
    """Configure the error window and its widgets.

    This class provides a Error Message Dialog for the Logic Simulator and
    enables tells the user the location of errors.

    Parameters
    ----------
    title: title of the window.
    error_message: multi-line string containing error message
    Public methods
    --------------
    on_quit_button(self, event): Event handler for when the user clicks the
                                 quit button.
    """

    def __init__(self, title, error_message):
        """Initialise GUI properties and useful variables."""
        lines = error_message.splitlines()
        max_length = 0
        for line in lines:
            max_length = max(max_length, len(line))
        length = 300 + max_length * 6
        height = 200
        size = (length, height)

        """Initialise widgets and layout."""
        super().__init__(parent=None, title=title, size=size)

        # Set up sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Read-only textbox with fixed-width font
        self.text_box = wx.TextCtrl(self, value=error_message, size=size,
                                    style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.text_box.SetFont(wx.Font(11, wx.MODERN,
                                      wx.NORMAL, wx.NORMAL, False))

        # Button to close window
        self.button = wx.Button(self, wx.ID_ANY, "OK")
        self.button.Bind(wx.EVT_BUTTON, self.on_quit_button)

        # Add widgets
        self.sizer.Add(self.text_box, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.sizer.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        # Set window properties
        self.SetSizeHints(length, height + 100)
        self.SetSizer(self.sizer)
        sizer_window = self.sizer.GetContainingWindow()
        sizer_window.SetBackgroundColour(wx.Colour(255, 69, 0))

    def on_quit_button(self, event):
        """Handle the event when the user clicks the run button."""
        self.sizer.GetContainingWindow().Close()
