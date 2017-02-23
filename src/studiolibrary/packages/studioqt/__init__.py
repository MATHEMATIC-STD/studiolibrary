# Copyright 2017 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

from studioqt.vendor.Qt import QtGui, QtCore, QtWidgets, QtUiTools

import os

from studioqt.utils import *
from studioqt.icon import Icon
from studioqt.theme import Theme, ThemesMenu
from studioqt.color import Color
from studioqt.pixmap import Pixmap
from studioqt.resource import Resource
from studioqt.stylesheet import StyleSheet
from studioqt.contextmenu import ContextMenu

from studioqt.decorators import showWaitCursor

from studioqt.imagesequence import ImageSequence
from studioqt.imagesequence import ImageSequenceWidget

from studioqt.widgets.hcolorbar import HColorBar
from studioqt.widgets.messagebox import MessageBox
from studioqt.widgets.toastwidget import ToastWidget
from studioqt.widgets.statuswidget import StatusWidget
from studioqt.widgets.menubarwidget import MenuBarWidget

from studioqt.widgets.searchwidget import SearchWidget
from studioqt.widgets.searchwidget import SearchFilter

from studioqt.widgets.combinedwidget.combinedwidget import CombinedWidget
from studioqt.widgets.combinedwidget.combinedwidgetitem import CombinedWidgetItem
from studioqt.widgets.combinedwidget.combinedwidgetitemgroup import CombinedWidgetItemGroup

from studioqt.widgets.folderswidget import FoldersWidget

# Custom qt actions
from studioqt.actions.slideraction import SliderAction
from studioqt.actions.separatoraction import SeparatorAction

PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH).replace('\\', '/')
PACKAGES_DIRNAME = DIRNAME + "/packages"
RESOURCE_DIRNAME = DIRNAME + "/resource"


global _resource

_resource = None


def resource():
    """
    :rtype: studioqt.Resource
    """
    global _resource

    if not _resource:
        _resource = Resource(dirname=RESOURCE_DIRNAME)

    return _resource


def icon(*args, **kwargs):
    """
    :type name: str
    :type extension: str
    :rtype: QtWidgets.QIcon
    """
    return resource().icon(*args, **kwargs)


def pixmap(*args, **kwargs):
    """
    :type name: str
    :type extension: str
    :rtype: QtWidgets.QPixmap
    """
    return resource().pixmap(*args, **kwargs)
