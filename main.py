import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class JogoDaVelha(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Jogo da Velha')
        self.setGeometry(100, 100, 300, 300)

        self.turno = 'X'  # Começa com X
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]

        self.botoes = []
        self.inicializarUI()

    def inicializarUI(self):
        for linha in range(3):
            for coluna in range(3):
                botao = QPushButton('', self)
                botao.setGeometry(coluna * 100, linha * 100, 100, 100)
                botao.clicked.connect(lambda _, l=linha, c=coluna: self.jogar(l, c))
                self.botoes.append(botao)

    def jogar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == '':
            self.tabuleiro[linha][coluna] = self.turno
            self.botoes[linha * 3 + coluna].setText(self.turno)
            if self.verificarVitoria():
                self.mostrarMensagem(f'{self.turno} venceu!')
                self.reiniciarJogo()
            elif self.verificarEmpate():
                self.mostrarMensagem('Empate!')
                self.reiniciarJogo()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificarVitoria(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != '':
                return True
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != '':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return True
        return False

    def verificarEmpate(self):
        for linha in self.tabuleiro:
            for marcacao in linha:
                if marcacao == '':
                    return False
        return True

    def reiniciarJogo(self):
        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        for botao in self.botoes:
            botao.setText('')

    def mostrarMensagem(self, mensagem):
        msgBox = QMessageBox()
        msgBox.setText(mensagem)
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = JogoDaVelha()
    jogo.show()
    sys.exit(app.exec_())

