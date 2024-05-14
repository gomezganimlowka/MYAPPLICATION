# main.py
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDButtonText, MDButton
from kivymd.uix.dialog import MDDialogButtonContainer, MDDialogSupportingText, MDDialogHeadlineText, MDDialog
from kivymd.uix.screen import MDScreen
from pyrebase import pyrebase

Window.size = 310, 550
firebaseConfig = {
    'apiKey': "AIzaSyAiREdW3GDvi3L7VfeKHTV43HC-vCVySpc",
    'authDomain': "endsemester-ff736.firebaseapp.com",
    'databaseURL': 'https://endsemester-ff736-default-rtdb.firebaseio.com/',
    'projectId': "endsemester-ff736",
    'storageBucket': "endsemester-ff736.appspot.com",
    'messagingSenderId': "233584801364",
    'appId': "1:233584801364:web:b98e2f66a5a3e6d7b8dfc1",
    'measurementId': "G-F13YC3MB9N"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class Started(MDScreen):
    Window.clearcolor = (0.5, 0.92, 0.9, 1)


class CreateAccount(MDScreen):
    Window.clearcolor = (0.5, 0.92, 0.9, 1)

    def create(self):
        try:
            username = self.ids.username.text
            password = self.ids.password.text
            confirm = self.ids.confirm.text
            if password == confirm:
                self.user = auth.create_user_with_email_and_password(username, password)
            if self.user:
                self.dialog = MDDialog(
                    MDDialogHeadlineText(
                        text="Account Created.",
                        color='red',
                        halign="center",
                    ),
                    MDDialogSupportingText(
                        text="Plan As Great Planner.",
                        text_color='red',
                        halign="center",
                    ),
                    MDDialogButtonContainer(
                        Widget(),
                        MDButton(

                            MDButtonText(text="OK"),
                            style="text",
                            on_release=self.close_dialog
                        ),
                        spacing="8dp",
                    ),
                )
                self.dialog.open()


        except Exception as e:
            print(e)
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Something is Wrong.",
                    color='red',
                    halign="center",
                ),
                MDDialogSupportingText(
                    text="Wrong Username or Password.",
                    text_color='red',
                    halign="center",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(

                        MDButtonText(text="OK"),
                        style="text",
                        on_release=self.close_dialog
                    ),
                    spacing="8dp",
                ),
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class LogIn(MDScreen):
    Window.clearcolor = (0.5, 0.92, 0.9, 1)

    def credentials(self):
        try:
            username = self.ids.username.text
            password = self.ids.password.text

            user = auth.sign_in_with_email_and_password(username, password)
            if user:
                self.manager.current = 'DashBord'
        except Exception as e:
            print(e)
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Something is Wrong.",
                    color='red',
                    halign="center",
                ),
                MDDialogSupportingText(
                    text="Wrong Username or Password.",
                    text_color='red',
                    halign="center",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(

                        MDButtonText(text="OK"),
                        style="text",
                        on_release=self.close_dialog
                    ),
                    spacing="8dp",
                ),
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class DashBord(MDScreen):
    Window.clearcolor = (0.5, 0.92, 0.9, 1)


class Profile(MDScreen):
    pass


class TestApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


TestApp().run()
