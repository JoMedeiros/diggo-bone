#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
from io import StringIO
import json
import shutil
import time
import list_files as lf

diggo_dir = '../Diggo-files'
def sinc_dir():
    while (True):
        self.json_string = lf.json_tree(diggo_dir)
        self.objs = json.loads(self.json_string)
    
class MainWindow(Gtk.Window):

    def __init__(self):
        # Login Window
        login = Gtk.Window(title="Login")
        login.set_default_size(200,200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.add(Gtk.Label('Nome: '))
        vbox.add(Gtk.Entry())
        vbox.add(Gtk.Label('Senha: '))
        vbox.add(Gtk.Entry(visibility=False))
        loginBtn = Gtk.Button('Entrar')
        loginBtn.connect('clicked', lambda widget: login.close())
        vbox.add(loginBtn)
        login.add(vbox)
        login.show_all()
        login.connect("destroy", Gtk.main_quit)
        Gtk.main()
        # Login closed
        self.json_string = lf.json_tree(diggo_dir)
        self.objs = json.loads(self.json_string)

        # Main Window Initialization
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
        localreloadBtn = Gtk.Button(label='atualizar alteracoes')
        deleteBtn = Gtk.Button(label='deletar')

        loadfolderBtn.connect('clicked', self.on_folder_clicked)
        loadfileBtn.connect('clicked', self.on_file_load)
        sincBtn.connect('clicked', self.sincronizar)
        localreloadBtn.connect('clicked', self.local_reload)
        deleteBtn.connect('clicked', self.delete)        
        self.init_tree_view()
        # Add TreeView to main layout
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.add(self.files_tree_view)
        layout.pack_start(self.scrolled_window, True, True, 0)

        grid = Gtk.Grid()
        grid.attach(loadfolderBtn,0,0,1,1)
        grid.attach(loadfileBtn,1,0,1,1)
        grid.attach(sincBtn, 0,1,1,1)
        grid.attach(localreloadBtn, 1,1,1,1)
        grid.attach(deleteBtn,0,2,1,1)
        layout.pack_end(grid, False, False, 0)
        nb.append_page(layout)
        self.add(nb)

    def init_tree_view(self):
        ## Convert data to ListStore (lists that TreeView can display)
        self.files_list_store = Gtk.TreeStore(str, str, str)
        
        self.rec_add_node(None, self.objs)
        self.files_tree_view = Gtk.TreeView(self.files_list_store)
        self.files_tree_view.get_selection().connect(
                'changed', self.on_changed)
        for i, col_title in enumerate(['Nome', 'Tamanho (em bytes)', 'Alterado em']):
            # Render means how to draw the data
            renderer = Gtk.CellRendererText()
            # Create columns (title is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            # Add column to TreeView
            self.files_tree_view.append_column(column)
        print('tree view loaded') 

    def sincronizar(self, widget):
        # This function must send JSON object to server
        print('Fazendo upload...')

    def on_file_load(self, widget):
        dialog = Gtk.FileChooserDialog('Selecione um arquivo', None, 
                Gtk.FileChooserAction.OPEN, 
                ('Cancelar', Gtk.ResponseType.CANCEL,
                "Ok", Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            # @TODO : Add file in the JSON object
            path = dialog.get_filename()
            size = os.path.getsize(path)
            name = path.split('/')[-1]
            shutil.copy(path,diggo_dir)
            timestamp = time.time()
            self.files_list_store.append(None,[name, str(size)+' bytes', str(timestamp)])
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
        # @TODO : Add files in the JSON object
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
    
    def rec_add_node(self, root, jsobj):
        for key, value in jsobj.iteritems():
            if type(value) in [str,int,float]:
                return
            pair = [str(key), '', value['date']]

            if 'size' in value: # It's a file
               pair[1] = value['size']
               self.files_list_store.append(root,pair)
            elif 'children' in value: # It's a dir
                nr = self.files_list_store.append(root,pair)
                self.rec_add_node(nr, value['children'])
        
    def local_reload(self, widget):
        self.json_string = lf.json_tree(diggo_dir)
        self.objs = json.loads(self.json_string)
        self.files_list_store.clear()
        self.rec_add_node(None, self.objs)
        self.files_tree_view = Gtk.TreeView(self.files_list_store)
        for i, col_title in enumerate(['Nome', 'Tamanho (em bytes)', 'Alterado em']):
            # Render means how to draw the data
            renderer = Gtk.CellRendererText()
            # Create columns (title is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(i)
            # Add column to TreeView
            self.files_tree_view.append_column(column)
        print('reload')

    def delete(self, widget):
        print('@TODO deletando arquivo')
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL, "Tem certeza que deseja deletar?")
        dialog.format_secondary_text(
            "O arquivo sera deletado do diretorio local, mas so sera deletado da BBB quando clicar em sincronizar.")
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Delentando arquivo")
            if self.sel and os.path.exists(diggo_dir+'/'+self.sel):
                os.remove(diggo_dir+'/'+self.sel)
            self.local_reload(widget)
            dialog.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancelando...")
            dialog.destroy()

    def on_changed(self, selection):
        (model, iter) = selection.get_selected()
        if iter is not None:
            self.sel = (str(model[iter][0]))

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()

