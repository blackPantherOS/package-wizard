#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#*http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles K Barcza*
#*************************************************************************************(c)2002-2019********
#	Design, FugionLogic idea and Initial code written by Charles K Barcza in december of 2018 
#       The maintainer of the PackageWizard: Miklos Horvath * hmiki[]blackpantheros.eu
#		(It's not allowed to delete this about label for free usage under GLP3)

from PyQt5.QtCore import QThread, pyqtSignal
import time, ptyprocess
import gettext
_ = gettext.gettext

class PKConInstallerThread(QThread):
    progress_sig = pyqtSignal(int, str)
    error_sig = pyqtSignal(str)
    disable_sig = pyqtSignal()
    result_sig = pyqtSignal(str)
    console_sig = pyqtSignal(bool)
    ask_sig = pyqtSignal(str)
    finish_sig = pyqtSignal()
    clear_sig = pyqtSignal()
    yes_sig = pyqtSignal()
    no_sig = pyqtSignal()

    translations = {
        "Transaction": _("Transaction"),
        "Resolving" : _("Resolving"),
        "Waiting in queue" : _("Waiting in queue"),
        "Starting" : _("Starting"),
        "Querying" : _("Querying"),
        "Loading cache" : _("Loading cache"),
        "Installing" : _("Installing"),
        "Finished" : _("Finished"),
        "The following packages have to be installed" : _("The following packages have to be installed"),
        "Waiting for authentication" : _("Waiting for authentication"),
        "Downloading packages" : _("Downloading packages"),
        "Package:" : _("Package:"),
        "Downloaded" : _("Downloaded"),
        "Installed" : _("Installed"),
        "Proceed with changes" : _("Proceed with changes"),
        "The following packages have to be removed" : _("The following packages have to be removed"),
        "Requesting data" : _("Requesting data"),
        "Removing packages" : _("Removing packages"),
        "Results" : _("Results"),
        "Removed" : _("Removed"),
    } 
    
    def translate(self, text):        
        for key in self.translations:
            if key in text:
                text = text.replace(key, self.translations[key])
        return text
    
    def format_inst_label(self, text):
        # The text of the installation label will be formated here.
        return text
                
    def __init__(self, parent):
        QThread.__init__(self)
        self.parent = parent
        self.progress_sig.connect(self.parent.set_progressbar)
        self.error_sig.connect(self.parent.show_error)
        self.disable_sig.connect(self.parent.hideYesNo)
        self.result_sig.connect(self.parent.installer_sent_message)
        self.console_sig.connect(self.console_switch)
        self.ask_sig.connect(self.parent.installer_ask)
        self.finish_sig.connect(self.parent.installer_finished)
        self.clear_sig.connect(self.parent.clear_label)
        self.yes_sig.connect(self.yes)
        self.no_sig.connect(self.no)
        self.work = False
        self.q = ""
        self.console_visible = False
               
    def console_switch(self, status):
        self.console_visible = status
            
    def set_job(self, pkcon_args, env):
        self.pkg_process = ptyprocess.PtyProcessUnicode.spawn(pkcon_args, env=env)
        self.work = True

    def yes(self):
        self.disable_sig.emit()
        self.clear_sig.emit()
        self.pkg_process.write("y\n")
 
    def no(self):
        self.disable_sig.emit()
        self.clear_sig.emit()
        self.pkg_process.write("n\n")
                    
    def run(self):
        lastline = ""
        percentage = 0
        status = ""
        results = ""
        got_results = False
        while True:
            if self.work:
                try:
                    if "Results:" in lastline:
                        got_results = True
                    buffer = self.pkg_process.read(1)
                    lastline += buffer
                    if got_results:
                        results += buffer
                    if '\n' in lastline:
                        if "Percentage:" in lastline:
                            percentage = int(lastline.strip().split(":")[1])
                            lastline = ""
                            self.progress_sig.emit(percentage, status)
                        elif "Status:" in lastline:
                            status = self.translate(lastline.strip().split(":")[1])
                            lastline = ""
                            self.progress_sig.emit(percentage, status)
                        else:
                            f_line = '{}<br>'.format(self.translate(lastline[:-1]))
                            if "have to be" in lastline or self.q:
                                self.q += f_line
                            self.result_sig.emit(f_line)
                            lastline = ""
                    if '?' in lastline:
                        if self.console_visible:
                            self.ask_sig.emit(self.translate(lastline))
                        else:
                            self.ask_sig.emit(self.format_inst_label(self.q + self.translate(lastline)))                             
                        lastline = ""
                        self.q = ""
                except Exception as e:
                        if "error:" in results.lower():
                            self.error_sig.emit(results)
                        self.finish_sig.emit()
                        self.work = False
#                        result = result[result.index("Results:")+10:]
            else:
                time.sleep(1)
