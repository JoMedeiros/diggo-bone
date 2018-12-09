import gtk
class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Notebook Demo")
      self.set_default_size(250, 200)
		
      nb = gtk.Notebook()
      nb.set_tab_pos(gtk.POS_TOP)
      vbox = gtk.VBox(False, 5)
		
      vb = gtk.VBox()
      hbox = gtk.HBox(True, 3)
		
      valign = gtk.Alignment(0.5,0.25, 0, 0)
      lbl = gtk.Label("Name of student")
		
      vb.pack_start(lbl, True, True, 10)
      text = gtk.Entry()
		
      vb.pack_start(text, True, True, 10)
      valign.add(vb)
		
      vbox.pack_start(valign)
      nb.append_page(vbox)
      nb.set_tab_label_text(vbox, "Name")
      hb = gtk.HButtonBox()
		
      btn1 = gtk.RadioButton(None,"Degree")
      hb.add(btn1)
		
      btn2 = gtk.RadioButton(btn1,"P.G.")
      hb.add(btn2)
		
      btn3 = gtk.RadioButton(btn1,"Doctorate")
      hb.add(btn3)
		
      nb.append_page(hb)
      nb.set_tab_label_text(hb, "Qualification")
		
      tv = gtk.TextView()
      nb.append_page(tv)
      nb.set_tab_label_text(tv, "about")
		
      self.add(nb)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
if __name__ == '__main__':
    PyApp()
gtk.main()
