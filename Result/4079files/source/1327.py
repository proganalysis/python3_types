# coding=utf-8
"""Fichier principal du serveur"""
import pygame
from commandes import *
import socket
import select


def lire_message():
    """Lorenzo doit le faire"""
    clients_connectes = []
    connexion = socket.socket()
    connexion.bind(('', 12800))
    connexion.listen(5)
    while True:
        messages = []
        connexions_demandees, wlist, xlist = select.select([connexion], [], [], 0.05)
        for c in connexions_demandees:
            connexion_avec_client, infos_connexion = c.accept()
            clients_connectes.append(connexion_avec_client)

        if len(clients_connectes) > 0:
            clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
            clients_connectes = clients_connectes[-5:]
            for client in clients_a_lire:
                try:
                    temp = client.recv(1024)
                    temp = temp.decode()
                    messages.append((temp, client))
                except ConnectionResetError:
                    pass
                except ConnectionAbortedError:
                    pass
        yield messages


def boucle(commandes, combats: List, ids: int, joueurs: Dict, joueurs_a_supprimer: List) -> Tuple[
    int, Dict, List, List]:
    """Boucle principale du serveur"""
    messages = next(commandes)
    for demande in messages:
        text = demande[0]
        text = text.split(":")
        if len(text) > 1:
            if text[0] == "carte":
                ids, joueurs = commandecarte(text[1:len(text)], demande[1], ids, joueurs, combats)
            elif text[0] == "combat":
                joueurs = commandecombat(text[1:len(text)], demande[1], joueurs)

    for i in MAPS.maps.values():
        if i.actif:
            i.update()
    to_del = []
    for i in combats:
        if i.actif:
            i.update()
        else:
            to_del.append(i)
    for i in to_del:
        combats.remove(i)
    return ids, joueurs, combats, joueurs_a_supprimer


def main():
    """Fonction principale du programme"""
    commandes = lire_message()
    ids = 0
    joueurs = {}
    combats = []
    joueurs_a_supprimer = []
    print("Démarage terminé")
    while True:
        ids, joueurs, combats, joueurs_a_supprimer = boucle(commandes, combats, ids, joueurs, joueurs_a_supprimer)
        pygame.time.Clock().tick(42)


main()
