from kivy.lang import Builder
from kivy.app import App

Builder.load_string('''
<Filechooser>: 

    label: label 

    # Providing the orentation 
    orientation: 'vertical'

    # Creating the File list / icon view 

    BoxLayout: 

        # Creating list view one side 
        FileChooserListView: 
            canvas.before: 
                Color: 
                    rgb: .4, .5, .5
                Rectangle: 
                    pos: self.pos 
                    size: self.size 
            on_selection: root.select(*args) 

        # Creating Icon view other side 
        FileChooserIconView: 
            canvas.before: 
                Color: 
                    rgb: .5, .4, .5
                Rectangle: 
                    pos: self.pos 
                    size: self.size 
            on_selection: root.select(*args) 

    # Adding label 
    Label: 
        id: label 
        size_hint_y: .1
        canvas.before: 
            Color: 
                rgb: .5, .5, .4
            Rectangle: 
                pos: self.pos 
                size: self.size
''')


class Filechooser(App):
    def select(self, *args):
        try:
            self.label.text = args[1][0]
        except:
            print("A")
            pass


Filechooser().run()
