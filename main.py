import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SignalHandler():
    def onQuit(self, *args, **kv):
        print('Quit')
        sys.exit(0)

class CompilerWindow():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('layout/compiler_screen.glade')
        builder.connect_signals(SignalHandler)

        #mapping objects
        self.main_window = builder.get_object('main_window')
        self.edif_source = builder.get_object('edit_source')
        self.symbol_table = builder.get_object('symbol_table')
        self.lexer_errors = builder.get_object('lexer_errors')
        self.sintatic_errors = builder.get_object('sintatic_errors')
        self.btn_analize = builder.get_object('btn_analize')
        self.btn_clear = builder.get_object('btn_clear')
        self.btn_finish = builder.get_object('btn_finish')

        self.main_window.show_all()
        Gtk.main()

if __name__ == "__main__":
    compilerWindo = CompilerWindow()