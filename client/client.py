import socket

ENC = "utf-8"
RECV_BUF = 4096

def send_and_recv(sock, msg):
    sock.sendall((msg + "\n").encode(ENC))
    data = b""
    while not data.endswith(b"\n"):
        chunk = sock.recv(RECV_BUF)
        if not chunk:
            break
        data += chunk
    return data.decode(ENC).strip()

def menu():
    print("\n--- MENU ---")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Supprimer une tâche")
    print("4. Changer le statut")
    print("5. Quitter")

def main():
    host = input("Adresse du serveur (ex: 127.0.0.1): ").strip() or "127.0.0.1"
    port_s = input("Port (ex: 5000): ").strip() or "5000"
    try:
        port = int(port_s)
    except:
        print("Port invalide")
        return

    try:
        sock = socket.create_connection((host, port))
    except Exception as e:
        print("Impossible de se connecter:", e)
        return

    print("[CLIENT] connecté à", host, port)
    try:
        while True:
            menu()
            c = input("Choix: ").strip()
            if c == "1":
                titre = input("Titre: ").strip()
                desc = input("Description: ").strip()
                auteur = input("Auteur: ").strip()
                resp = send_and_recv(sock, f"ADD;{titre};{desc};{auteur}")
                print("->", resp)

            elif c == "2":
                resp = send_and_recv(sock, "LIST")
                if resp == "LIST;":
                    print("(aucune tâche)")
                    continue
                if not resp.startswith("LIST;"):
                    print("->", resp)
                    continue
                _, data = resp.split(";", 1)
                for item in data.split("|"):
                    if not item:
                        continue
                    id_, titre, description, statut, auteur = item.split(";", 4)
                    print(f"{id_} | {titre} | {statut} | {auteur}")
            elif c == "3":
                id_ = input("ID complet: ").strip()
                resp = send_and_recv(sock, f"DEL;{id_}")
                print("->", resp)
            elif c == "4":
                id_ = input("ID complet: ").strip()
                statut = input("Nouveau statut (TODO/DOING/DONE): ").strip().upper()
                resp = send_and_recv(sock, f"STATUS;{id_};{statut}")
                print("->", resp)
            elif c == "5":
                print("Quit")
                break
            else:
                print("Choix invalide")
    finally:
        sock.close()

if __name__ == "__main__":
    main()