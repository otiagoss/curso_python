from PIL import Image

if __name__ == "__main__":
  #abre imagem para leitura
  imagem = Image.open('imagem.jpg')
  
  #Converte a imagem para Preto e Branco,
  #removendo a luminosodade ("L" => lightness)
  imagem_preto_branco = imagem.convert("L")
  
  #Salva a nova imagem
  imagem_preto_branco.save('imagem-pb.jpg')
  
  #abre a imagem
  imagem_preto_branco.show()  
  