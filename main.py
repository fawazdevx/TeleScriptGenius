import shutil
from PyQt5.QtCore import Qt
import random
########################################################################
# ==> IMPORT GUI FILE
from ui.ui_interfaceNew import *
from screens.splash import SplashScreen
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.welcome import WelcomeScreen
from screens.gratitude import GratitudeScreen
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import *


########################################################################
# IMPORT CUSTOM WIDGETS
from Custom_Widgets.Widgets import *

app_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

folder_path = os.path.join(app_directory, "userdata_01e4.dat")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' already exists.")

# ==> GLOBAL VARIABLES
counter = 0
# -------------------------------------------------
# SCRIPT COUNT
# -------------------------------------------------
GENERATED_REGISTRY_FILE = os.path.join(folder_path, "generated_scripts.json")



def load_generated_registry():
    if not os.path.exists(GENERATED_REGISTRY_FILE):
        return set()
    try:
        with open(GENERATED_REGISTRY_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()


def save_generated_registry(registry_set):
    with open(GENERATED_REGISTRY_FILE, "w") as f:
        json.dump(list(registry_set), f, indent=2)

shadow_elements = {

    "widget_5", "generated", "success", "templates", "regions"
}




# -------------------------------------------------
# IMPORT GENERATORS
# -------------------------------------------------
# ML10G
from Generators.ML10G.Asaba10G_CP_Script_Generator import Generate_Asaba_CP_Script
from Generators.ML10G.Enugu10G_CP_Script_Generator import Generate_Enugu_CP_Script
from Generators.ML10G.Kano10G_CP_Script_Generator import Generate_Kano_CP_Script
from Generators.ML10G.Owerri10G_CP_Script_Generator import Generate_Owerri_CP_Script
from Generators.ML10G.Asaba10G_CS_Script_Generator import Generate_Asaba_CS_Script
from Generators.ML10G.Enugu10G_CS_Script_Generator import Generate_Enugu_CS_Script
from Generators.ML10G.Kano10G_CS_Script_Generator import Generate_Kano_CS_Script
from Generators.ML10G.Owerri10G_CS_Script_Generator import Generate_Owerri_CS_Script

# Aviat

from Generators.Aviat.AsabaAV_CP_Script_Generator import Generate_AsabaAV_CP_Script
from Generators.Aviat.EnuguAV_CP_Script_Generator import Generate_EnuguAV_CP_Script
from Generators.Aviat.KanoAV_CP_Script_Generator import Generate_KanoAV_CP_Script
from Generators.Aviat.OwerriAV_CP_Script_Generator import Generate_OwerriAV_CP_Script
from Generators.Aviat.AsabaAV_CS_Script_Generator import Generate_AsabaAV_CS_Script
from Generators.Aviat.EnuguAV_CS_Script_Generator import Generate_EnuguAV_CS_Script
from Generators.Aviat.KanoAV_CS_Script_Generator import  Generate_KanoAV_CS_Script
from Generators.Aviat.OwerriAV_CS_Script_Generator import Generate_OwerriAV_CS_Script


GENERATORS = {
    # ML10G
    "ASABA_10G_CP": Generate_Asaba_CP_Script,
    "ENUGU_10G_CP": Generate_Enugu_CP_Script,
    "KANO_10G_CP": Generate_Kano_CP_Script,
    "OWERRI_10G_CP": Generate_Owerri_CP_Script,
    "ASABA_10G_CS": Generate_Asaba_CS_Script,
    "ENUGU_10G_CS": Generate_Enugu_CS_Script,
    "KANO_10G_CS": Generate_Kano_CS_Script,
    "OWERRI_10G_CS": Generate_Owerri_CS_Script,

    # Aviat
    "ASABA_Aviat_CP": Generate_AsabaAV_CP_Script,
    "ENUGU_Aviat_CP": Generate_EnuguAV_CP_Script,
    "KANO_Aviat_CP": Generate_KanoAV_CP_Script,
    "OWERRI_Aviat_CP": Generate_OwerriAV_CP_Script,
    "ASABA_Aviat_CS": Generate_AsabaAV_CS_Script,
    "ENUGU_Aviat_CS": Generate_EnuguAV_CS_Script,
    "KANO_Aviat_CS": Generate_KanoAV_CS_Script,
    "OWERRI_Aviat_CS": Generate_OwerriAV_CS_Script,

}


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        # -------------------------------------------------
        # LOAD SCRIPT COUNT (NEW)
        # -------------------------------------------------
        self.generated_registry = load_generated_registry()
        self.total_scripts_generated = len(self.generated_registry)
        self.ui.totalgenerated.setText(str(self.total_scripts_generated))

        # CONNECT BUTTON ONCE
        self.ui.generateBtn.clicked.connect(self.on_generate_clicked)
        self.ui.generateBtn.setObjectCustomTheme("cyan", "black")
        self.ui.generateBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.expandMenu())
        self.ui.totalgenerated.setText(str(self.total_scripts_generated))

        self.ui.genQuickBtn.setObjectCustomTheme("cyan", "black")
        self.ui.linkQuickBtn.setObjectCustomTheme("cyan", "black")
        self.ui.startQuickBtn.setObjectCustomTheme("cyan", "black")

        # set app icon
        icon_path = "ui/icons/Telescript.ico"
        self.ui.app_icon.setIcon(QIcon(icon_path))

        anim = QPropertyAnimation(self.ui.label, b"geometry")
        anim.setDuration(800)
        anim.setStartValue(QRect(0, 200, 200, 50))
        anim.setEndValue(QRect(100, 100, 200, 50))
        anim.start()

        glow = QGraphicsDropShadowEffect(self.ui.heroCard)
        glow.setBlurRadius(60)
        glow.setOffset(0, 0)
        glow.setColor(QColor(0, 229, 255, 80))
        self.ui.heroCard.setGraphicsEffect(glow)

        # SHADOW EFFECT
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)

        # window config
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(850, 400)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        loadJsonStyle(self, self.ui)  # APPLY JSON STYLESHEET


        # Make placeholder show even with items for Regions
        self.ui.regionBox.lineEdit().setPlaceholderText("Select Region")  # placeholder text
        self.ui.regionBox.setCurrentIndex(-1)  # no item selected
        self.ui.regionBox.lineEdit().setCursor(Qt.PointingHandCursor)

        # Make placeholder show even with items for Regions
        self.ui.tempBox.lineEdit().setPlaceholderText("Select Template")  # placeholder text
        self.ui.tempBox.setCurrentIndex(-1)
        self.ui.tempBox.lineEdit().setCursor(Qt.PointingHandCursor)

        self.ui.sitename.setPlaceholderText("e.g., DL0033")

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        self.ui.regionBox.setFocusPolicy(Qt.StrongFocus)
        self.ui.tempBox.setFocusPolicy(Qt.StrongFocus)

        self.ui.sizeGrip.setVisible(True)

    def on_generate_clicked(self):
        site_name = self.ui.sitename.text().strip().upper()
        region_ui = self.ui.regionBox.currentText().strip()
        script_type_ui = self.ui.tempBox.currentText().strip()

        # Mapping UI selections to GENERATOR keys
        REGION_MAP = {
            # ML10G
            "Asaba": "ASABA",
            "Enugu": "ENUGU",
            "Kano": "KANO",
            "Owerri": "OWERRI",
            # add more if needed
        }

        SCRIPT_MAP = {
            "10G CP ML Scripts": "10G_CP",
            "Aviat CP Scripts": "Aviat_CP",
            "10G CS ML Scripts": "10G_CS",
            "Aviat CS Scripts": "Aviat_CS",
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

            generator_func(site_name, self)

            # ✅ Mark as generated
            self.generated_registry.add(key)
            save_generated_registry(self.generated_registry)

            self.total_scripts_generated = len(self.generated_registry)
            self.ui.totalgenerated.setText(str(self.total_scripts_generated))

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


windows = {}


def show_gratitude():
    windows["gratitude"] = GratitudeScreen()
    windows["gratitude"].show()


def show_welcome():
    windows["welcome"] = WelcomeScreen()
    windows["welcome"].show()


def show_login():
    windows["login"] = LoginScreen()
    windows["login"].show()


def show_register():
    windows["register"] = RegisterScreen()
    windows["register"].show()


def show_main():
    windows["main"] = MainWindow()
    windows["main"].show()


def splash_finished(first_run):
    if first_run:
        show_gratitude()
    else:
        show_login()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    windows["splash"] = SplashScreen(splash_finished)
    windows["splash"].show()

    sys.exit(app.exec_())