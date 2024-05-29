import os

def copy_file(input_file, output_file):
    try:
        # Abrindo o arquivo de entrada para leitura
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Abrindo o arquivo de saída para escrita
        with open(output_file, 'w') as outfile:
            outfile.write(content)
        
        print(f"Conteúdo copiado de {input_file} para {output_file} com sucesso!")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {input_file} não foi encontrado.")
    except IOError as e:
        print(f"Erro de I/O: {e}")

if __name__ == "__main__":
    # Caminhos dos arquivos de entrada e saída
    input_file = os.path.join('..', 'input', 'input.txt')
    output_file = os.path.join('..', 'output', 'output.txt')
    
    # Chamando a função para copiar o conteúdo
    copy_file(input_file, output_file)