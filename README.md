# ♻️ Smart Trash

O **Smart Trash** é um projeto que utiliza um modelo de detecção de objetos baseado em **YOLO** para identificar e classificar diferentes tipos de materiais recicláveis em tempo real, usando a webcam.

## 📁 Estrutura do Projeto

- `best.pt` — Arquivo do modelo treinado.
- `main.py` — Script principal que executa a detecção de objetos.
- `scripts/maping.py` — Mapeamento de materiais para suas respectivas categorias.

## 📦 Dependências

- Python 3.x
- OpenCV
- Ultralytics YOLO

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/yTheu/smart-trash
   cd smart-trash
   ```

2. Instale as dependências:
   ```bash
   pip install opencv-python ultralytics
   ```

## ▶️ Como Usar

Execute o script principal:
```bash
python main.py
```

A janela de vídeo será exibida com a detecção de objetos em tempo real.  
Pressione `q` para encerrar a execução.

## 🤝 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para enviar **pull requests** com melhorias.
