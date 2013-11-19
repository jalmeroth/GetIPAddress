import objc
import socket
from AppKit import *
from Foundation import *

class Alert(object):
    
    def __init__(self, messageText):
        super(Alert, self).__init__()
        self.messageText = messageText
        self.informativeText = ""
        self.buttons = []
    
    def displayAlert(self):
        alert = NSAlert.alloc().init()
        alert.setMessageText_(self.messageText)
        alert.setInformativeText_(self.informativeText)
        alert.setAlertStyle_(NSInformationalAlertStyle)
        for button in self.buttons:
            alert.addButtonWithTitle_(button)
        NSApp.activateIgnoringOtherApps_(True)
        self.buttonPressed = alert.runModal()
    
def alert(message="Default Message", info_text="", buttons=["OK"]):    
    ap = Alert(message)
    ap.informativeText = info_text
    ap.buttons = buttons
    ap.displayAlert()
    return ap.buttonPressed
 
def cocoa_dialogs(fn):
    class MainRunner(object):
        def runWithShutdown_(self, timer):
            fn()
            NSApp.stop_(None)
 
        def run(self):
            NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(1, self, 'runWithShutdown:', "", False)                    
                    
    def wrapped():
        NSApplication.sharedApplication()
        MainRunner().run()
        NSApp.run()
        
    return wrapped
 
@cocoa_dialogs
def main():
    """
    def get_ip_address():
        return socket.gethostbyname(socket.gethostname())
    
    def get_hostname():
        return socket.gethostname()

    """
    
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    # print host_name + ': ' + ip_address
    
    if(ip_address == "127.0.0.1"):
        # dialog = 'tell application "System Events" to display dialog "Steck ihn rein, Diggah!" buttons ("OK") default button "OK"'
        # print display(dialog)
        alert("Hinweis", "Steck schon!", ['OK'])
    else:
        # dialog = 'tell application "System Events" to display dialog "IPv4: ' + ip_address + ' " buttons ("OK") default button "OK"'
        # print display(dialog)
        alert("IPv4", str(ip_address), ['OK'])
    
if __name__ == "__main__":
    main()