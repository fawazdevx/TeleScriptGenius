# Telescript21012025@
import shutil
from PyQt5.QtCore import Qt

########################################################################
# ==> IMPORT GUI FILE
from ui_interfaceNew import *

########################################################################
# IMPORT CUSTOM WIDGETS
from Custom_Widgets.Widgets import *
# data {
#     path: font-awesome/solid/globe-africa.svg
# }

# # Code to make the software create a directory / folder on the target system
make_dir = os.path.expanduser('~/.iconify/font-awesome/solid')
os.makedirs(make_dir, exist_ok=True)
icon_to_path = "images/globe-africa.svg"
destination_path = os.path.join(make_dir, "globe-africa.svg")
shutil.copy(icon_to_path, destination_path)

app_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
# Define the folder path inside the app installation folder
folder_path = os.path.join(app_directory, "userdata_01e4.dat")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' already exists.")

# ==> GLOBAL VARIABLES
counter = 0

shadow_elements = {

    "frame_60", "frame_64", "frame_68", "frame_72", "widget_3", "frame_23", "frame_27", "frame_28",
    "frame_31", "frame_32", "frame_34", "frame_35"
}


# ML10G
from Generators.ML10G.Asaba10G_CP_Script_Generator import Generate_Asaba_CP_Script
from Generators.ML10G.Enugu10G_CP_Script_Generator import Generate_Enugu_CP_Script
from Generators.ML10G.Kano10G_CP_Script_Generator import Generate_Kano_CP_Script
from Generators.ML10G.Owerri10G_CP_Script_Generator import Generate_Owerri_CP_Script

# Aviat

from Generators.Aviat.AsabaAV_CP_Script_Generator import Generate_AsabaAV_CP_Script
from Generators.Aviat.EnuguAV_CP_Script_Generator import Generate_EnuguAV_CP_Script
from Generators.Aviat.KanoAV_CP_Script_Generator import Generate_KanoAV_CP_Script
from Generators.Aviat.OwerriAV_CP_Script_Generator import Generate_OwerriAV_CP_Script

# Step 2: Map them
GENERATORS = {
    # ML10G
    "ASABA_10G_CP": Generate_Asaba_CP_Script,
    "ENUGU_10G_CP": Generate_Enugu_CP_Script,
    "KANO_10G_CP": Generate_Kano_CP_Script,
    "OWERRI_10G_CP": Generate_Owerri_CP_Script,

    # Aviat
    "ASABA_Aviat_CP": Generate_AsabaAV_CP_Script,
    "ENUGU_Aviat_CP": Generate_EnuguAV_CP_Script,
    "KANO_Aviat_CP": Generate_KanoAV_CP_Script,
    "OWERRI_Aviat_CP": Generate_OwerriAV_CP_Script,

}


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # CONNECT BUTTON ONCE
        self.ui.generateBtn.clicked.connect(self.on_generate_clicked)

        # window config
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(850, 600)

        self.ui.generateBtn.setObjectTheme(2)
        self.ui.generateBtn.setObjectCustomTheme("orange", "black")

        # Make placeholder show even with items for Regions
        self.ui.regionBox.setEditable(True)  # make it editable
        self.ui.regionBox.lineEdit().setPlaceholderText("Select Region")  # placeholder text
        self.ui.regionBox.setCurrentIndex(-1)  # no item selected
        self.ui.regionBox.lineEdit().setReadOnly(True)  # optional: prevent typing

        # Make placeholder show even with items for Regions
        self.ui.tempBox.setEditable(True)  # make it editable
        self.ui.tempBox.lineEdit().setPlaceholderText("Select Template")  # placeholder text
        self.ui.tempBox.setCurrentIndex(-1)  # no item selected
        self.ui.tempBox.lineEdit().setReadOnly(True)  # optional: prevent typing

        self.ui.sitename.setPlaceholderText("e.g., DL0033")

    def on_generate_clicked(self):
        site_name = self.ui.sitename.text().strip().upper()
        region_ui = self.ui.regionBox.currentText().strip()
        script_type_ui = self.ui.tempBox.currentText().strip()

        # Map UI selections to GENERATOR keys
        REGION_MAP = {
            # ML10G
            "Asaba": "ASABA",
            "Enugu": "ENUGU",
            "Kano": "KANO",
            "Owerri": "OWERRI",
            # add more if needed
        }

        SCRIPT_MAP = {
            "ML10G CP ML Scripts": "10G_CP",
            "Aviat CP Scripts": "Aviat_CP",
            # add more templates if needed
        }

        region_key = REGION_MAP.get(region_ui, region_ui.upper())
        script_key = SCRIPT_MAP.get(script_type_ui, script_type_ui.upper())

        key = f"{region_key}_{script_key}"
        print("Mapped key:", key)

        self.generate_script(site_name, region_key, script_key)

    def generate_script(self, site_name, region, script_type):
        key = f"{region}_{script_type}"
        print("Selected key:", key)

        if key not in GENERATORS:
            self.showNotification(f"❌ No generator found for {key}")
            return

        generator_func = GENERATORS[key]

        try:
            file_path = generator_func(site_name, self)

            if not file_path:
                # generator already showed error
                return

            self.showNotification(
                f"✅ {script_type} has been Generated for {site_name} with required details from LLDs provided."
            )

        except Exception as e:
                self.showNotification(f"❌ {str(e)}")

    def showNotification(self, message):
        self.ui.notificationMssg.setText(message)
        self.ui.popupNotificationContainer.setVisible(True)  # Show the container

###############
# EXECUTE APP
###############


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
##########################
# END===>
##########################
