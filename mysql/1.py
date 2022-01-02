def buscarArchivo(self, Registro):
        fname, _ = QFileDialog.getOpenFileName(Registro, 'Open File', '', "Image Files (*.jpg *.png)")
        if fname:
            pixmap = QPixmap(fname)
            pixi = pixmap.scaledToWidth(self.foto.width())
            self.foto.setPixmap(pixi)