import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gestor_hp import atualizar_imagem
import os

arquivos_monitorados = {"trex.json", "buzz.json", "ze.json", "festor.json", "renna.json"}

class JSONChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        nome_arquivo = event.src_path.split("\\")[-1]
        if nome_arquivo in arquivos_monitorados:
            print(f"{nome_arquivo} atualizado! rodando script...")
            atualizar_imagem()

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "json")
    event_handler = JSONChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
