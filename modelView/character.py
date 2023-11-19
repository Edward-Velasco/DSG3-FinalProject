class Character:
    def __init__(self, id, name, linkImg, link_vivo, link_muerto, texto_pelea, boton_pelea, id_nxt_node):
        self.id = id
        self.name = name
        self.linkImg = linkImg
        self.link_vivo = link_vivo
        self.link_muerto = link_muerto
        self.texto_pelea = texto_pelea
        self.boton_pelea = boton_pelea
        self. id_nxt_node = id_nxt_node
        self.estado = True

    def matar(self):
        self.estado = False
        