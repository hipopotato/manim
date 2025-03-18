from manim import *

class SimpleScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)  # Cria um círculo azul
        self.play(Create(circle))  # Anima a criação do círculo
        self.wait(2)  # Espera 2 segundos

# Para rodar este código, salve como 'simple_scene.py' e execute no terminal:
# manim -pql simple_scene.py SimpleScene
