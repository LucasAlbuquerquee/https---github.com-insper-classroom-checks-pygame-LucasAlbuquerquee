import funcoes, pygame

def inicializa():
    pygame.init()

    window = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Jogo do Lucas")
    
    return window

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window):
    window.fill((255,0,0))
    pygame.display.update()
    return window

def game_loop(window):
    while True:
        if not recebe_eventos():
            return False
        desenha(window)



def main():
    janela = inicializa()
    executando = True
    while executando:
        executando = recebe_eventos()
        desenha(janela)

    pygame.quit()

if __name__ == "__main__":
    main()

janela = funcoes.inicializa()