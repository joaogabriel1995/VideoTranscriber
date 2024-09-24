


def createFile(output_file, result):
    with open(output_file, "w", encoding="utf-8") as f:
        # Itera sobre os segmentos e grava o texto com tempos de início e fim no arquivo
        for segment in result['segments']:
            start_time = segment['start']
            end_time = segment['end']
            text = segment['text']
            
            # Escreve os tempos e o texto no arquivo
            f.write(f"Texto: {text}\nInício: {start_time:.2f} segundos\nFim: {end_time:.2f} segundos\n\n")
