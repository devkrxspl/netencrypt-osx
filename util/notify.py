# Modified code from https://github.com/vtr0n/npyscreen/blob/master/npyscreen/utilNotify.py
# that allows me to resize notify_confirm windows and change display offset

# Imports
import textwrap;

from npyscreen import wgmultiline, fmPopup;

# Functions
def _prepare_message(message):
    if isinstance(message, list) or isinstance(message, tuple):
        return "\n".join([ s.rstrip() for s in message])
        #return "\n".join(message)
    else:
        return message;

def _wrap_message_lines(message, line_length):
    lines = []
    for line in message.split('\n'):
        lines.extend(textwrap.wrap(line.rstrip(), line_length))
    return lines

def notify_confirm(message, title="Message", form_color='STANDOUT', wrap=True, wide=False, editw = 0, width=60, height=10, relx=10, rely=2):

    # Modifying default size of popup
    fmPopup.Popup.DEFAULT_COLUMNS = width;
    fmPopup.Popup.DEFAULT_LINES = height;

    fmPopup.Popup.SHOW_ATX = relx;
    fmPopup.Popup.SHOW_ATY = rely;

    message = _prepare_message(message)
    if wide:
        F = fmPopup.PopupWide(name=title, color=form_color)
    else:
        F   = fmPopup.Popup(name=title, color=form_color)
    F.preserve_selected_widget = True
    mlw = F.add(wgmultiline.Pager,)
    mlw_width = mlw.width-1
    if wrap:
        message = _wrap_message_lines(message, mlw_width)
    else:
        message = message.split("\n")
    mlw.values = message
    F.editw = editw
    F.edit()