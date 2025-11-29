import socket
import threading
import sys
from .manager import GestionnaireTaches

HOST = "0.0.0.0"
PORT = 5000
RECV_BUF = 4096
ENC = "utf-8"

class ServeurTaches:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.manager = GestionnaireTaches()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(8)
        print(f"[SERVEUR] écoute sur {self.host}:{self.port}",flush=True)

    def start(self):
        try:
            while True:
                conn, addr = self.sock.accept()
                print(f"[SERVEUR] connexion de {addr}")
                t = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
                t.start()
        except KeyboardInterrupt:
            print("\n[SERVEUR] arrêt demandé.")
        finally:
            self.sock.close()

    def handle_client(self, conn, addr):
        with conn:
            data_buf = b""
            while True:
                try:
                    chunk = conn.recv(RECV_BUF)
                    if not chunk:
                        break
                    data_buf += chunk
                    while b"\n" in data_buf:
                        line, data_buf = data_buf.split(b"\n", 1)
                        line = line.decode(ENC).strip()
                        if not line:
                            continue
                        resp = self.process_command(line)
                        conn.sendall((resp + "\n").encode(ENC))
                except ConnectionResetError:
                    break
                except Exception as e:
                    try:
                        conn.sendall((f"ERROR;{str(e)}\n").encode(ENC))
                    except:
                        pass
                    break
            print(f"[SERVEUR] déconnexion {addr}")

    def process_command(self, line):
        parts = line.split(";")
        cmd = parts[0].upper()

        if cmd == "ADD":
            if len(parts) < 4:
                return "ERROR;ADD requiert 3 champs: titre;description;auteur"
            titre = parts[1]
            description = parts[2]
            auteur = parts[3]
            t = self.manager.ajouter_tache(titre, description, auteur)
            return f"OK;{t.id}"

        elif cmd == "LIST":
            all_tasks = self.manager.lister_taches()
            if not all_tasks:
                return "LIST;"
            items = [t.to_line() for t in all_tasks]
            return "LIST;" + "|".join(items)

        elif cmd == "DEL":
            if len(parts) < 2:
                return "ERROR;DEL requiert id"
            id_ = parts[1]
            removed = self.manager.supprimer_tache(id_)
            if removed:
                return "OK;deleted"
            else:
                return "ERROR;ID introuvable"

        elif cmd == "STATUS":
            if len(parts) < 3:
                return "ERROR;STATUS requiert id;statut"
            id_ = parts[1]
            statut = parts[2]
            if statut not in ("TODO", "DOING", "DONE"):
                return "ERROR;statut invalide (TODO/DOING/DONE)"
            updated = self.manager.changer_statut(id_, statut)
            if updated:
                return "OK;status_changed"
            else:
                return "ERROR;ID introuvable"

        else:
            return "ERROR;Commande inconnue"

if __name__ == "__main__":
    ServeurTaches().start()