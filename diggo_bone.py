#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
from io import StringIO
import json
import list_files as lf

diggo_dir = '../Diggo-files'

list_of_files = [['Doggo.jpg', 2000],['potato.png',666]]
json_string = lf.json_tree(diggo_dir)
#io = StringIO(json_string)
#files_dic = json.JSONDecoder()
#objs = (files_dic.decode(json_string))
objs = json.loads(json_string)

for key, value in objs.iteritems():
    print(str(key))
    if 'size' in value:
        print(value['size'])

class MainWindow(Gtk.Window):

    def __init__(self):
        # Window Initialization
        Gtk.Window.__init__(self, title='Diggo Bone')
        self.set_default_size(750, 300)
        self.set_border_width(10)
        
        # Components 
        nb = Gtk.Notebook()
        nb.set_tab_pos(Gtk.PositionType.TOP)

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                spacing=10)
        ## Buttons
        loadfolderBtn = Gtk.Button(label='carregar diretorio')
        loadfileBtn = Gtk.Button(label='carregar arquivo')
        sincBtn = Gtk.Button(label='sincronizar com a BeagleBone')
        ## Button Box
        btnBox = Gtk.HButtonBox()
        btnBox.set_border_width(10)

        loadfolderBtn.connect('clicked', self.on_folder_clicked)
        loadfileBtn.connect('clicked', self.on_file_load)
        sincBtn.connect('clicked', self.sincronizar)
        
        self.init_tree_view()
        # Add TreeView to main layout
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(self.files_tree_view)
        layout.pack_start(scrolled_window, True, True, 0)

        btnBox.pack_start(loadfolderBtn, True, True, 0)
        btnBox.pack_start(loadfileBtn, True, True, 0)
        btnBox.pack_start(sincBtn, True, True, 0)
        
        layout.pack_end(btnBox, True, True, 0)
        nb.append_page(layout)
        self.add(nb)

    def init_tree_view(self):
        ## Convert data to ListStore (lists that TreeView can display)
        self.files_list_store = Gtk.TreeStore(str, str)
        
        for key, value in objs.iteritems():
            pair = [str(key), '']
            if 'size' in value:
               pair[1] = value['size']
            self.files_list_store.append(None,pair)
          
        #for item in list_of_files:
         #   self.files_list_store.append(None, list(item))
        ## TreeView is the item that is displayed
        self.files_tree_view = Gtk.TreeView(self.files_list_store)
        
        for i, col_title in enumerate(['Nome', 'Tamanho (em bytes)']):
            # Render means how to draw the data
            renderer = Gtk.CellRendererText()
            # Create columns (title is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            # Add column to TreeView
            self.files_tree_view.append_column(column)
    
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
            size = os.path.getsize(path)
            self.files_list_store.append('./',(path.split('/')[-1], size))
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
        dialog = Gtk.FileChooserDialog("Escolha uma pasta para carregar os arquivos", 
                self, Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Selecionar", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            path = dialog.get_filename()
            name = path.split('/')[-1]
            size = sum([os.path.getsize(f) for f in os.listdir(path) if os.path.isfile(f)])
            files = os.listdir(path)
            folder = self.files_list_store.append(None,[name,size])
            for f in files:
                size = os.path.getsize(path+'/'+f)
                self.files_list_store.append(folder, (f, size))
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()

