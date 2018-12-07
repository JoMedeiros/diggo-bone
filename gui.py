#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Lista de arquivos de teste
files = [('doge.jpg','5.5 MB'),
         ('doggo.png','2.6 MB'),
         ('another_doggo.gif','3.8 MB')]

class Handler:
    def __init__(self, builder):
        self.builder = builder
        files_tree_view = builder.get_object("ftv")

        files_list_store = Gtk.ListStore(str, str)
        
        for f in files:
            files_list_store.append(list(f))
        #files_tree_view = Gtk.TreeView(files_list_store)
        files_tree_view.set_reorderable(files_tree_view)

        for i, col_title in enumerate(['Nome','Tamanho']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            files_tree_view.append_column(column) 

    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

    def on_file_chooser(self, button):
        print('TODO: abrir file choose')

    def on_file_clicked(self, widget):
        print('Escolhendo os file')
        dialog = Gtk.FileChooserDialog('Selecione um arquivo', None, 
                Gtk.FileChooserAction.OPEN, 
                ('Cancelar', Gtk.ResponseType.CANCEL,
                "Ok", Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print('You clicked the OK button')
            print('File selected' + dialog.get_filename())
        elif response == Gtk. ResponseType.CANCEL:
            print('Saindo')
            dialog.destroy()
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

builder = Gtk.Builder()
builder.add_from_file("view.glade")
builder.connect_signals(Handler(builder))

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()

