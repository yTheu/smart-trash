# Smart Trash

O projeto Smart Trash utiliza um modelo de detecção de objetos para identificar e classificar diferentes tipos de materiais recicláveis em tempo real usando a webcam.

## Estrutura do Projeto


- `best.pt`: Arquivo do modelo treinado.
- `main.py`: Script principal que executa a detecção de objetos.
- `scripts/maping.py`: Mapeamento de materiais para suas respectivas categorias.

## Dependências

- Python 3.x
- OpenCV
- Ultralytics YOLO

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/yTheu/smart-trash/
    cd smart-trash
    ```

2. Instale as dependências:

    ```sh
    pip install opencv-python ultralytics
    ```

## Uso

1. Coloque o arquivo do modelo treinado `best.pt` na raiz do projeto.
2. Execute o script principal:

    ```sh
    python main.py
    ```

3. A detecção de objetos será exibida em uma janela de vídeo. Pressione `q` para sair.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
