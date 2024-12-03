from PySide2.QtGui import *
from custom_buttons import QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import os
import iconify.path
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from ui_splash_screen_ts import Ui_SplashScreen
from ui_reg_login import Ui_RegScreen
from ui_login import Ui_LoginScreen
import shutil
import sys
# import pyrebase
#
#
# firebaseConfig = {
#     "apiKey": "AIzaSyBiAqEZuVXRedMqfS6EUj29xc1-CBP1cYE",
#   "authDomain": "telescriptgenius.firebaseapp.com",
#   "databaseURL": "https://telescriptgenius-default-rtdb.firebaseio.com",
#   "projectId": "telescriptgenius",
#   "storageBucket": "telescriptgenius.firebasestorage.app",
#   "messagingSenderId": "403559859207",
#   "appId": "1:403559859207:web:f564e9ed4f17738f2a96a2",
#   "measurementId": "G-WJP73TFK5Y"
# }
#
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
########################################################################
# ==> IMPORT GUI FILE
from ui_interface import *
########################################################################
# IMPORT CUSTOM WIDGETS
from Custom_Widgets.Widgets import *
# data {
#     path: font-awesome/solid/globe-africa.svg
# }

# Code to make the software create a directory / folder on the target system
make_dir = os.path.expanduser('~/.iconify/font-awesome/solid')
os.makedirs(make_dir, exist_ok=True)
icon_to_path = "images/globe-africa.svg"
destination_path = os.path.expanduser(r'~/.iconify/font-awesome/solid')
shutil.copy(icon_to_path, destination_path)

# ==> GLOBAL VARIABLES
counter = 0

shadow_elements = {

    "frame_60", "frame_64", "frame_68", "frame_72", "widget_3", "frame_23", "frame_27", "frame_28",
    "frame_31", "frame_32", "frame_34", "frame_35"
}

########################################################################
# MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):

    # 10G ML
    #####################################################################
    # AsabaCP Script Generator Function
    ####################################################################
    script_generated_asaba_cp = Signal(str)

    def on_generate_asaba_cp_button_clicked(self):
        sites_name = self.ui.sites_Acp_Input.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from Asaba10G_CP_Script_Generator import Generate_Asaba_CP_Script
        _, file_name = Generate_Asaba_CP_Script(sites_name, self)
        self.add_asabacp_script(file_name)
        self.add_asabacp_script_page(file_name)
        self.script_generated_asaba_cp.emit(sites_name)

    def setup_connections_asaba_cp(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genACPBtn.clicked.connect(self.on_generate_asaba_cp_button_clicked)
        self.ui.genACPBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Acp_Input.returnPressed.connect(self.on_generate_asaba_cp_button_clicked)

    def add_asabacp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_asabacp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()

    #####################################################################
    # AsabaCS Script Generator Function
    ####################################################################
    script_generated_asaba_cs = Signal(str)

    def on_generate_asaba_cs_button_clicked(self):
        CP_ID = self.ui.sites_Acp_Input.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from Asaba10G_CS_Script_Generator import Generate_Asaba_CS_Script
        Generate_Asaba_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_asabacs_script(file_name)
        # self.add_asabacs_script_page(file_name)
        self.script_generated_asaba_cs.emit(CP_ID)

    def setup_connections_asaba_cs(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genACSBtn.clicked.connect(self.on_generate_asaba_cs_button_clicked)
        self.ui.genACSBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Acp_Input.returnPressed.connect(self.on_generate_asaba_cs_button_clicked)

    def add_asabacs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_asabacs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # EnuguCP Script Generator Function
    ####################################################################
    script_generated_enugu_cp = Signal(str)

    def on_generate_enugu_cp_button_clicked(self):
        sites_name = self.ui.sites_Ecp_Input.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from Enugu10G_CP_Script_Generator import Generate_Enugu_CP_Script
        _, file_name = Generate_Enugu_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_enugucp_script(file_name)
        self.add_enugucp_script_page(file_name)
        self.script_generated_enugu_cp.emit(sites_name)

    def setup_connections_enugu_cp(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genECPBtn.clicked.connect(self.on_generate_enugu_cp_button_clicked)
        self.ui.genECPBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ecp_Input.returnPressed.connect(self.on_generate_enugu_cp_button_clicked)

    def add_enugucp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_enugucp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # EnuguCS Script Generator Function
    ####################################################################
    script_generated_enugu_cs = Signal(str)

    def on_generate_enugu_cs_button_clicked(self):
        CP_ID = self.ui.sites_Ecp_Input.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from Enugu10G_CS_Script_Generator import Generate_Enugu_CS_Script
        Generate_Enugu_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_enugucs_script(file_name)
        # self.add_enugucs_script_page(file_name)
        self.script_generated_enugu_cs.emit(CP_ID)

    def setup_connections_enugu_cs(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genECSBtn.clicked.connect(self.on_generate_enugu_cs_button_clicked)
        self.ui.genECSBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ecp_Input.returnPressed.connect(self.on_generate_enugu_cs_button_clicked)

    def add_enugucs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_enugucs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # KanoCP Script Generator Function
    ####################################################################
    script_generated_kano_cp = Signal(str)

    def on_generate_kano_cp_button_clicked(self):
        sites_name = self.ui.sites_Kcp_Input.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from Kano10G_CP_Script_Generator import Generate_Kano_CP_Script
        _, file_name = Generate_Kano_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_kanocp_script(file_name)
        self.add_kanocp_script_page(file_name)
        self.script_generated_kano_cp.emit(sites_name)

    def setup_connections_kano_cp(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genKCPBtn.clicked.connect(self.on_generate_kano_cp_button_clicked)
        self.ui.genKCPBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Kcp_Input.returnPressed.connect(self.on_generate_kano_cp_button_clicked)

    def add_kanocp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_kanocp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # KanoCS Script Generator Function
    ####################################################################
    script_generated_kano_cs = Signal(str)

    def on_generate_kano_cs_button_clicked(self):
        CP_ID = self.ui.sites_Kcp_Input.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from Kano10G_CS_Script_Generator import Generate_Kano_CS_Script
        Generate_Kano_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_kanocs_script(file_name)
        # self.add_kanocs_script_page(file_name)
        self.script_generated_kano_cs.emit(CP_ID)

    def setup_connections_kano_cs(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genKCSBtn.clicked.connect(self.on_generate_kano_cs_button_clicked)
        self.ui.genKCSBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Kcp_Input.returnPressed.connect(self.on_generate_kano_cs_button_clicked)

    def add_kanocs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_kanocs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # OwerriCP Script Generator Function
    ####################################################################
    script_generated_owerri_cp = Signal(str)

    def on_generate_owerri_cp_button_clicked(self):
        sites_name = self.ui.sites_Ocp_Input.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from Owerri10G_CP_Script_Generator import Generate_Owerri_CP_Script
        _, file_name = Generate_Owerri_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_owerricp_script(file_name)
        self.add_owerricp_script_page(file_name)
        self.script_generated_owerri_cp.emit(sites_name)

    def setup_connections_owerri_cp(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genOCPBtn.clicked.connect(self.on_generate_owerri_cp_button_clicked)
        self.ui.genOCPBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ocp_Input.returnPressed.connect(self.on_generate_owerri_cp_button_clicked)

    def add_owerricp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_owerricp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  # Setting the height of the widget as needed
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # OwerriCS Script Generator Function
    ####################################################################
    script_generated_owerri_cs = Signal(str)

    def on_generate_owerri_cs_button_clicked(self):
        CP_ID = self.ui.sites_Ocp_Input.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from Owerri10G_CS_Script_Generator import Generate_Owerri_CS_Script
        _, file_name = Generate_Owerri_CS_Script(CP_ID, self)  # We only care about the file_name
        self.add_owerrics_script(file_name)
        self.add_owerrics_script_page(file_name)
        self.script_generated_owerri_cs.emit(CP_ID)

    def setup_connections_owerri_cs(self):
        # Connecting the button click event to the on_generate_button_clicked method
        self.ui.genOCSBtn.clicked.connect(self.on_generate_owerri_cs_button_clicked)
        self.ui.genOCSBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ocp_Input.returnPressed.connect(self.on_generate_owerri_cs_button_clicked)

    def add_owerrics_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_owerrics_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()

# Aviat
    #####################################################################
    # AsabaCP Script Generator Function
    ####################################################################
    script_generated_asabaav_cp = Signal(str)

    def on_generate_asabaav_cp_button_clicked(self):
        sites_name = self.ui.sites_Acp_InputAV.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from AsabaAV_CP_Script_Generator import Generate_AsabaAV_CP_Script
        _, file_name = Generate_AsabaAV_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_asabaav_cp_script(file_name)
        self.add_asabaav_cp_script_page(file_name)
        self.script_generated_asabaav_cp.emit(sites_name)

    def setup_connections_asabaav_cp(self):
        self.ui.genACPBtnAV.clicked.connect(self.on_generate_asabaav_cp_button_clicked)
        self.ui.genACPBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Acp_InputAV.returnPressed.connect(self.on_generate_asabaav_cp_button_clicked)

    def add_asabaav_cp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_asabaav_cp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # AsabaCS Script Generator Function
    ####################################################################
    script_generated_asabaav_cs = Signal(str)

    def on_generate_asabaav_cs_button_clicked(self):
        CP_ID = self.ui.sites_Acp_InputAV.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from AsabaAV_CS_Script_Generator import Generate_AsabaAV_CS_Script
        Generate_AsabaAV_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_asabaav_cs_script(file_name)
        # self.add_asabaav_cs_script_page(file_name)
        self.script_generated_asabaav_cs.emit(CP_ID)

    def setup_connections_asabaav_cs(self):
        self.ui.genACSBtnAV.clicked.connect(self.on_generate_asabaav_cs_button_clicked)
        self.ui.genACSBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Acp_InputAV.returnPressed.connect(self.on_generate_asabaav_cs_button_clicked)

    def add_asabaav_cs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_asabaav_cs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # EngugCP Script Generator Function
    ####################################################################
    script_generated_enuguav_cp = Signal(str)

    def on_generate_enuguav_cp_button_clicked(self):
        sites_name = self.ui.sites_Ecp_InputAV.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from EnuguAV_CP_Script_Generator import Generate_EnuguAV_CP_Script
        _, file_name = Generate_EnuguAV_CP_Script(sites_name, self)
        self.add_enuguav_cp_script(file_name)
        self.add_enuguav_cp_script_page(file_name)
        self.script_generated_enuguav_cp.emit(sites_name)

    def setup_connections_enuguav_cp(self):
        self.ui.genECPBtnAV.clicked.connect(self.on_generate_enuguav_cp_button_clicked)
        self.ui.genECPBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ecp_InputAV.returnPressed.connect(self.on_generate_enuguav_cp_button_clicked)

    def add_enuguav_cp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_enuguav_cp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # EnuguCS Script Generator Function
    ####################################################################
    script_generated_enuguav_cs = Signal(str)

    def on_generate_enuguav_cs_button_clicked(self):
        CP_ID = self.ui.sites_Ecp_InputAV.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from EnuguAV_CS_Script_Generator import Generate_EnuguAV_CS_Script
        Generate_EnuguAV_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_enuguav_cs_script(file_name)
        # self.add_enuguav_cs_script_page(file_name)
        self.script_generated_enuguav_cs.emit(CP_ID)

    def setup_connections_enuguav_cs(self):
        self.ui.genECSBtnAV.clicked.connect(self.on_generate_enuguav_cs_button_clicked)
        self.ui.genECSBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ecp_InputAV.returnPressed.connect(self.on_generate_enuguav_cs_button_clicked)

    def add_enuguav_cs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_enuguav_cs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # KanoCP Script Generator Function
    ####################################################################
    script_generated_kanoav_cp = Signal(str)

    def on_generate_kanoav_cp_button_clicked(self):
        sites_name = self.ui.sites_Kcp_InputAV.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from KanoAV_CP_Script_Generator import Generate_KanoAV_CP_Script
        _, file_name = Generate_KanoAV_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_kanoav_cp_script(file_name)
        self.add_kanoav_cp_script_page(file_name)
        self.script_generated_kanoav_cp.emit(sites_name)

    def setup_connections_kanoav_cp(self):
        self.ui.genKCPBtnAV.clicked.connect(self.on_generate_kanoav_cp_button_clicked)
        self.ui.genKCPBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Kcp_InputAV.returnPressed.connect(self.on_generate_kanoav_cp_button_clicked)

    def add_kanoav_cp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_kanoav_cp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # KanoCS Script Generator Function
    ####################################################################
    script_generated_kanoav_cs = Signal(str)

    def on_generate_kanoav_cs_button_clicked(self):
        CP_ID = self.ui.sites_Kcp_InputAV.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from KanoAV_CS_Script_Generator import Generate_KanoAV_CS_Script
        Generate_KanoAV_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_kanoav_cs_script(file_name)
        # self.add_kanoav_cs_script_page(file_name)
        self.script_generated_kanoav_cs.emit(CP_ID)

    def setup_connections_kanoav_cs(self):
        self.ui.genKCSBtnAV.clicked.connect(self.on_generate_kanoav_cs_button_clicked)
        self.ui.genKCSBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Kcp_InputAV.returnPressed.connect(self.on_generate_kanoav_cs_button_clicked)

    def add_kanoav_cs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_kanoav_cs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # OwerriCP Script Generator Function
    ####################################################################
    script_generated_owerriav_cp = Signal(str)

    def on_generate_owerriav_cp_button_clicked(self):
        sites_name = self.ui.sites_Ocp_InputAV.text()
        sites_name = sites_name.strip().upper()
        print("Generate Button Clicked. Site Name:", sites_name)
        # imports
        from OwerriAV_CP_Script_Generator import Generate_OwerriAV_CP_Script
        _, file_name = Generate_OwerriAV_CP_Script(sites_name, self)  # We only care about the file_name
        self.add_owerriav_cp_script(file_name)
        self.add_owerriav_cp_script_page(file_name)
        self.script_generated_owerriav_cp.emit(sites_name)

    def setup_connections_owerriav_cp(self):
        self.ui.genOCPBtnAV.clicked.connect(self.on_generate_owerriav_cp_button_clicked)
        self.ui.genOCPBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ocp_InputAV.returnPressed.connect(self.on_generate_owerriav_cp_button_clicked)

    def add_owerriav_cp_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_owerriav_cp_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #####################################################################
    # CS Script Generator Function
    ####################################################################
    script_generated_owerriav_cs = Signal(str)

    def on_generate_owerriav_cs_button_clicked(self):
        CP_ID = self.ui.sites_Ocp_InputAV.text()
        CP_ID = CP_ID.strip().upper()
        print("Generate Button Clicked. Site Name:", CP_ID)
        # imports
        from OwerriAV_CS_Script_Generator import Generate_OwerriAV_CS_Script
        Generate_OwerriAV_CS_Script(CP_ID, self)  # We only care about the file_name
        # self.add_owerriav_cs_script(file_name)
        # self.add_owerriav_cs_script_page(file_name)
        self.script_generated_owerriav_cs.emit(CP_ID)

    def setup_connections_owerriav_cs(self):
        self.ui.genOCSBtnAV.clicked.connect(self.on_generate_owerriav_cs_button_clicked)
        self.ui.genOCSBtnAV.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.sites_Ocp_InputAV.returnPressed.connect(self.on_generate_owerriav_cs_button_clicked)

    def add_owerriav_cs_script(self, script_content):
        if script_content not in self.recent_scripts:
            script_widget = QLabel(script_content)
            script_widget.setFixedHeight(50)
            self.ui.verticalLayout_33.addWidget(script_widget)
            self.ui.verticalLayout_33.update()
            self.recent_scripts.append(script_content)
            with open('recent_script_names.txt', 'a') as f:
                f.write(script_content + '\n')

    def add_owerriav_cs_script_page(self, script_content):
        script_widgets = QLabel(script_content)
        script_widgets.setFixedHeight(50)  
        self.ui.verticalLayout_38.addWidget(script_widgets)
        self.ui.verticalLayout_38.update()
    #########################################################################

    def load_recent_scripts(self):
        try:
            with open('recent_script_names.txt', 'r') as f:
                self.recent_scripts = [line.strip() for line in f.readlines()]
                print("Loaded scripts:", self.recent_scripts)
                for script_content in self.recent_scripts:
                    self.add_asabacp_script_page(script_content)
                    self.add_asabacp_script(script_content)
                    # self.add_enugucp_script_page(script_content)
                    # self.add_enugucs_script_page(script_content)
                    # self.add_kanocp_script_page(script_content)
                    # self.add_kanocs_script_page(script_content)
                    # self.add_owerricp_script_page(script_content)
                    # self.add_owerrics_script_page(script_content)
                    # self.add_asabaav_cp_script_page(script_content)
                    # self.add_asabaav_cs_script_page(script_content)
                    # self.add_enuguav_cp_script_page(script_content)
                    # self.add_enuguav_cs_script_page(script_content)
                    # self.add_kanoav_cp_script_page(script_content)
                    # self.add_kanoav_cs_script_page(script_content)
                    # self.add_owerriav_cp_script_page(script_content)
                    # self.add_owerriav_cs_script_page(script_content)
        except FileNotFoundError:
            pass

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.recent_scripts = []
        self.load_recent_scripts()

        # self.ui.logoutBtn.clicked.connect(self.logout)  # Connect logout button to logout function

    # def logout(self):
    #     try:
    #         os.remove("user_session.json")  # Remove the session file on logout
    #     except FileNotFoundError:
    #         pass
    #     self.login = LoginScreen()  # Return to the login screen
    #     self.login.show()
    #     self.close()

    # FOR 10G ML
        # ASABA
        self.setup_connections_asaba_cp()
        self.setup_connections_asaba_cs()
        # ENUGU
        self.setup_connections_enugu_cp()
        self.setup_connections_enugu_cs()
        # KANO
        self.setup_connections_kano_cp()
        self.setup_connections_kano_cs()
        # OWERRI
        self.setup_connections_owerri_cp()
        self.setup_connections_owerri_cs()

    # FOR AVIAT
        # ASABA
        self.setup_connections_asabaav_cp()
        self.setup_connections_asabaav_cs()
        # ENUGU
        self.setup_connections_enuguav_cp()
        self.setup_connections_enuguav_cs()
        # KANO
        self.setup_connections_kanoav_cp()
        self.setup_connections_kanoav_cs()
        # OWERRI
        self.setup_connections_owerriav_cp()
        self.setup_connections_owerriav_cs()

        # set app icon
        icon_path = "icons/Telescript.ico"
        self.ui.app_icon.setIcon(QIcon(icon_path))

        # SHADOW EFFECT
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setMinimumSize(850, 600)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        loadJsonStyle(self, self.ui)  # APPLY JSON STYLESHEET

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        # self.show()

        # Create new button
        # button = QPushButton("name")
        # button.setText("Login")
        # button.setObjectTheme(2)
        # self.ui.gridLayout.addWidget(button, 2, 1, 1, 1)

        self.ui.closeNotificationBtn.setObjectTheme(6)
        # FOR LEFT MENU
        self.ui.menuBtn.setObjectTheme(6)
        self.ui.genBtn.setObjectTheme(6)
        self.ui.homeBtn.setObjectTheme(6)
        self.ui.scriptsBtn.setObjectTheme(6)
        self.ui.regionsBtn.setObjectTheme(6)
        # FOR CENTER MENU
        self.ui.moreMenuBtn.setObjectTheme(6)
        self.ui.notificationBtn.setObjectTheme(6)
        self.ui.profileMenuBtn.setObjectTheme(6)
        # FOR RIGHT MENU
        self.ui.minimize_window_btn.setObjectTheme(6)
        self.ui.restore_window_btn.setObjectTheme(6)
        self.ui.close_window_btn.setObjectTheme(6)
        # FOR SETTINGS MENU
        self.ui.settingsBtn.setObjectTheme(6)
        self.ui.helpBtn.setObjectTheme(6)
        self.ui.infoBtn.setObjectTheme(6)
        # FOR TEMP PAGE
        self.ui.ml10GBtn.setObjectTheme(4)
        self.ui.routerBtn.setObjectTheme(2)
        self.ui.aviatBtn.setObjectTheme(3)
        self.ui.linkBtn.setObjectTheme(4)

        self.ui.backrsBtn.setObjectTheme(4)
        self.ui.backlcBtn.setObjectTheme(4)
        ###############################################################
        self.ui.view_script.setObjectTheme(13)

        # FOR ML REGIONS PAGE
        self.ui.backRBtn.setObjectTheme(13)
        self.ui.aRegBtn.setObjectTheme(6)
        self.ui.eRegBtn.setObjectTheme(6)
        self.ui.kRegBtn.setObjectTheme(6)
        self.ui.oRegBtn.setObjectTheme(6)
        # FOR ASABA PAGE
        self.ui.backABtn.setObjectCustomTheme("orange", "black")
        self.ui.genACPBtn.setObjectTheme(2)
        self.ui.genACSBtn.setObjectTheme(3)
        # FOR ENUGU PAGE
        self.ui.backEBtn.setObjectCustomTheme("green", "black")
        self.ui.genECPBtn.setObjectTheme(5)
        self.ui.genECSBtn.setObjectTheme(6)
        # FOR KANO PAGE
        self.ui.backKBtn.setObjectTheme(6)
        self.ui.genKCPBtn.setObjectTheme(8)
        self.ui.genKCSBtn.setObjectTheme(9)
        # FOR OWERRI PAGE
        self.ui.backOBtn.setObjectCustomTheme("purple", "black")
        self.ui.genOCPBtn.setObjectTheme(11)
        self.ui.genOCSBtn.setObjectTheme(12)
        ###################################################################
        # FOR AVIAT REGIONS PAGE
        self.ui.backAVRBtn.setObjectTheme(13)
        self.ui.aRegBtnAV.setObjectTheme(6)
        self.ui.eRegBtnAV.setObjectTheme(6)
        self.ui.kRegBtnAV.setObjectTheme(6)
        self.ui.oRegBtnAV.setObjectTheme(6)
        # FOR ASABA PAGE
        self.ui.backABtnAV.setObjectCustomTheme("orange", "black")
        self.ui.genACPBtnAV.setObjectTheme(2)
        self.ui.genACSBtnAV.setObjectTheme(3)
        # FOR ENUGU PAGE
        self.ui.backEBtnAV.setObjectCustomTheme("green", "black")
        self.ui.genECPBtnAV.setObjectTheme(5)
        self.ui.genECSBtnAV.setObjectTheme(6)
        # FOR KANO PAGE
        self.ui.backKBtnAV.setObjectTheme(7)
        self.ui.genKCPBtnAV.setObjectTheme(8)
        self.ui.genKCSBtnAV.setObjectTheme(9)
        # FOR OWERRI PAGE
        self.ui.backOBtnAV.setObjectCustomTheme("purple", "black")
        self.ui.genOCPBtnAV.setObjectTheme(11)
        self.ui.genOCSBtnAV.setObjectTheme(12)

        self.ui.getStartBtn.setObjectCustomTheme("blue", "dark-blue")
        self.ui.ml10GBtn.setObjectCustomTheme("blue", "dark-blue")
        self.ui.routerBtn.setObjectCustomTheme("blue", "dark-blue")
        self.ui.aviatBtn.setObjectCustomTheme("blue", "dark-blue")
        self.ui.linkBtn.setObjectCustomTheme("blue", "dark-blue")

        # FOR ML10G
        self.ui.genACPBtn.setObjectCustomTheme("orange", "black")
        self.ui.genACSBtn.setObjectCustomTheme("orange", "black")
        self.ui.genECPBtn.setObjectCustomTheme("green", "black")
        self.ui.genECSBtn.setObjectCustomTheme("green", "black")
        self.ui.genKCPBtn.setObjectCustomTheme("blue", "black")
        self.ui.genKCSBtn.setObjectCustomTheme("blue", "black")
        self.ui.genOCPBtn.setObjectCustomTheme("purple", "black")
        self.ui.genOCSBtn.setObjectCustomTheme("purple", "black")

        # FOR AVIAT
        self.ui.genACPBtnAV.setObjectCustomTheme("orange", "black")
        self.ui.genACSBtnAV.setObjectCustomTheme("orange", "black")
        self.ui.genECPBtnAV.setObjectCustomTheme("green", "black")
        self.ui.genECSBtnAV.setObjectCustomTheme("green", "black")
        self.ui.genKCPBtnAV.setObjectCustomTheme("blue", "black")
        self.ui.genKCSBtnAV.setObjectCustomTheme("blue", "black")
        self.ui.genOCPBtnAV.setObjectCustomTheme("purple", "black")
        self.ui.genOCSBtnAV.setObjectCustomTheme("purple", "black")

        self.ui.app_icon.setObjectTheme(6)

        self.ui.copyBtn.setObjectTheme(9)
        self.ui.aRegBtn.setObjectAnimateOn("hover")
        # self.ui.aRegBtn.setObjectAnimateOn("click")
        self.ui.aRegBtn._animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
        self.ui.eRegBtn.setObjectAnimateOn("hover")
        # self.ui.aRegBtn.setObjectAnimateOn("click")
        self.ui.eRegBtn._animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
        self.ui.kRegBtn.setObjectAnimateOn("hover")
        # self.ui.aRegBtn.setObjectAnimateOn("click")
        self.ui.kRegBtn._animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
        self.ui.oRegBtn.setObjectAnimateOn("hover")
        # self.ui.aRegBtn.setObjectAnimateOn("click")
        self.ui.oRegBtn._animation.setEasingCurve(QtCore.QEasingCurve.InQuad)

        # FOR ML10G
        iconify(
            self.ui.aRegBtn, icon="font-awesome:solid:globe-africa", color="orange", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.eRegBtn, icon="font-awesome:solid:globe-africa", color="green", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.kRegBtn, icon="font-awesome:solid:globe-africa", color="blue", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.oRegBtn, icon="font-awesome:solid:globe-africa", color="purple", size=64,
            animation="breathe", animateOn="hover",
        )

        # FOR AVIAT
        iconify(
            self.ui.aRegBtnAV, icon="font-awesome:solid:globe-africa", color="orange", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.eRegBtnAV, icon="font-awesome:solid:globe-africa", color="green", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.kRegBtnAV, icon="font-awesome:solid:globe-africa", color="blue", size=64,
            animation="breathe", animateOn="hover",
        )
        iconify(
            self.ui.oRegBtnAV, icon="font-awesome:solid:globe-africa", color="purple", size=64,
            animation="breathe", animateOn="hover",
        )

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET SIZE
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        self.ui.view_script.clicked.connect(self.open_file)

        self.ui.copyBtn.clicked.connect(self.copy_script)
        self.ui.sizeGrip.setVisible(True)

        # Connect the "Copy File" button to the copy_file slot
    def copy_script(self):
        # Get the source file path using QFileDialog
        options = QFileDialog.Options()
        source_file, _ = QFileDialog.getOpenFileName(self, "Select Source File", "",
                                                     "All Files (*);;Text Files (*.txt)", options=options)
        if not source_file:
            return  # User canceled the operation

        # Get the destination file path using QFileDialog
        destination_file, _ = QFileDialog.getSaveFileName(self, "Save As", "", "All Files (*);;Text Files (*.txt)",
                                                          options=options)
        if not destination_file:
            return  # User canceled the operation

        try:
            shutil.copy(source_file, destination_file)
            QMessageBox.information(self, "Success", "File copied successfully!")
            # message = f"File copied successfully!."
            # self.showNotification(message)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error copying file: {e}")
            # error_message = f"Error copying file {e}."
            # self.showNotification(error_message)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
                self.ui.viewscriptEdit.setPlainText(text)

    def showNotification(self, message):
        self.ui.notificationMssg.setText(message)
        self.ui.popupNotificationContainer.setVisible(True)  # Show the container

class SplashScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 255))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.splash_screen_progress)
        self.timer.start(35)

        # CHANGE SPLASH DESCRIPTION
        # INITIAL TEXT
        self.ui.description.setText("<strong>WELCOME</strong> TO PARACHRONOS")

        # CHANGE TEXT
        QtCore.QTimer.singleShot(1500, lambda: self.ui.description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.description.setText("<strong>INITIALIZING</strong> APPLICATION"))

        # SHOW WINDOW
        self.show()

    # SPLASH SCREEN FUNCTION
    def splash_screen_progress(self):
        global counter

        # SETTING VALUE TO PROGRESSBAR
        self.ui.progressBar.setValue(counter)

        # CLOSING SPLASH SCREEN AND OPENING MAIN UI
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN UI
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE PROGRESS BAR COUNTER
        counter += 1
#
#     def check_login_status(self):
#         try:
#             with open("user_session.json", "r") as session_file:
#                 user_data = json.load(session_file)
#                 user_id = user_data.get("user_id", None)
#                 if user_id:  # If user is logged in, open the main window
#                     self.main = MainWindow()
#                     self.main.show()
#                 else:
#                     self.show_login_screen()  # Else show login screen
#         except FileNotFoundError:
#             self.show_login_screen()  # If session file not found, show login screen
#
#     def show_login_screen(self):
#         self.login = LoginScreen()
#         self.login.show()
#
#
# # LOGIN SCREEN CLASS
# class LoginScreen(QMainWindow):
#
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self)
#         self.ui = Ui_LoginScreen()  # UI for Login
#         self.ui.setupUi(self)
#
#         self.ui.loginBtn.clicked.connect(self.login)
#         self.ui.regBtn.clicked.connect(self.show_register_screen)
#
#     def login(self):
#         email = self.ui.emailInput.text()
#         password = self.ui.passwordInput.text()
#         try:
#             user = auth.sign_in_with_email_and_password(email, password)
#             with open("user_session.json", "w") as session_file:
#                 json.dump({"user_id": user['localId']}, session_file)
#             self.main = MainWindow()
#             self.main.show()
#             self.close()
#         except Exception as e:
#             QMessageBox.warning(self, "Login Failed", str(e))
#
#     def show_register_screen(self):
#         self.register = RegScreen()
#         self.register.show()
#         self.close()
#
#
# # REGISTRATION SCREEN CLASS
# class RegScreen(QMainWindow):
#
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self)
#         self.ui = Ui_RegScreen()  # UI for Register
#         self.ui.setupUi(self)
#
#         self.ui.regBtn.clicked.connect(self.register)
#
#     def register(self):
#         email = self.ui.emailInput.text()
#         password = self.ui.passwordInput.text()
#         try:
#             auth.create_user_with_email_and_password(email, password)
#             QMessageBox.information(self, "Success", "Account created successfully!")
#             self.login = LoginScreen()
#             self.login.show()
#             self.close()
#         except Exception as e:
#             QMessageBox.warning(self, "Registration Failed", str(e))


########################################################################

########################################################################
# EXECUTE APP
########################################################################
# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    window = SplashScreen()
    window.show()
    sys.exit(app.exec_())
########################################################################
# END===>
########################################################################
