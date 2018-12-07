#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

diggo_files = [('Doggo.jpg', 2000),('potato.png',666)]

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Diggo Bone')
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                spacing=10)
        self.add(layout)
        self.set_border_width(10)
        self.set_default_size(500, 300)
        # Convert data to ListStore (lists that TreeView can display)
        self.files_list_store = Gtk.ListStore(str, int)
        for item in diggo_files:
            self.files_list_store.append(list(item))

        # TreeView is the item that is displayed
        files_tree_view = Gtk.TreeView(self.files_list_store)
        
        for i, col_title in enumerate(['Nome', 'Tamanho']):
            # Render means how to draw the data
            renderer = Gtk.CellRendererText()
            # Create columns (title is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            # Add column to TreeView
            files_tree_view.append_column(column)
        # Add TreeView to main layout
        layout.pack_start(files_tree_view, True, True, 0)

        # Grid
        grid = Gtk.Grid()
        #self.add(grid)
        # Box
        self.box = Gtk.Box(spacing=10) 
        # Buttons
        self.loadfolderBtn = Gtk.Button(label='carregar diretório')
        self.loadfileBtn = Gtk.Button(label='carregar arquivo')
        self.sincBtn = Gtk.Button(label='sincronizar com a BeagleBone')
        
        self.loadfolderBtn.connect('clicked', self.on_folder_clicked)
        self.loadfileBtn.connect('clicked', self.on_file_load)
        self.sincBtn.connect('clicked', self.sincronizar)

        #self.add(self.box)
        layout.pack_start(self.loadfolderBtn, True, True, 0)
        layout.pack_start(self.loadfileBtn, True, True, 0)
        layout.pack_start(self.sincBtn, True, True, 0)
    
    def sincronizar(self, widget):
        print('Fazendo upload...')

    def on_file_load(self, widget):
        dialog = Gtk.FileChooserDialog('Selecione um arquivo', None, 
                Gtk.FileChooserAction.OPEN, 
                ('Cancelar', Gtk.ResponseType.CANCEL,
                "Ok", Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            path = dialog.get_filename()
            self.files_list_store.append((path.split(sep='/')[-1], 1234))
        elif response == Gtk. ResponseType.CANCEL:
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

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Escolha uma pasta para carregar os arquivos", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Selecionar", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            path = dialog.get_filename()
            files = os.listdir()
            for f in files:
                self.files_list_store.append((f, 1234))
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()

