# coding=utf-8
"""Ce fichier ce charge de traiter les commandes envoyées par les joueurs connectés"""
from classesentitee import *
from json import dumps


def mouvement(idjoueur: str, direction: str, joueurs: Dict, combat: List) -> bool:
    """Cette fonction permet a un joueur de se déplacer"""
    if int(idjoueur) in joueurs.keys():
        joueur = joueurs[int(idjoueur)]
        if not joueur.combat:
            if direction == "right":
                directionmouv = Mouvements.DROITE
            elif direction == "left":
                directionmouv = Mouvements.GAUCHE
            elif direction == "up":
                directionmouv = Mouvements.HAUT
            elif direction == "down":
                directionmouv = Mouvements.BAS
            else:
                return False
            return MAPS.get(joueur.map).move(joueur, directionmouv, combat)
    return False


def connexion(client, ids: int, joueurs: Dict) -> Tuple[int, Dict]:
    """Cette fonction est appellée quand un joueur se connecte"""
    joueur = Joueur(ids)
    joueurs[ids] = joueur
    map = MAPS.get(joueur.map)
    map.actif = True
    map.joueurs[ids] = joueur
    client.send(str(ids).encode())
    ids += 1
    return ids, joueurs


def carte(id_joueur: str, joueurs: Dict) -> str:
    """Cette fonction est appellée quand le joueur arrive sur une carte et lui transmet des informations"""
    if int(id_joueur) in joueurs.keys():
        joueur = joueurs[int(id_joueur)]
        mobgroups = []
        for mobsgroups in MAPS.get(joueur.map).mobsgroups:
            temp = {"level": mobsgroups.level, "mobs": []}
            for mob in mobsgroups.mobgroup:
                temp["mobs"].append((mob.name, mob.map_coords))
            mobgroups.append(temp)
        temp = []
        for players in MAPS.get(joueur.map).joueurs.values():
            temp.append({"name": players.name, "classe": str(players.classe), "position": players.map_coords})
        return dumps({"map": joueur.map, "mobs": mobgroups, "joueurs": temp, "position": joueur.map_coords})


def commandecarte(message: List, client, ids: int, joueurs: Dict, combats: List) -> Tuple[int, Dict]:
    """Cette fonction effectue toute le commandes liés a la carte (mouvement,objets a affichager,...)"""
    if message[0] == "move" and len(message) == 3:
        client.send(str(mouvement(message[1], message[2], joueurs, combats)).encode())
    elif message[0] == "carte" and len(message) == 2:
        client.send(str(carte(message[1], joueurs)).encode())
    elif message[0] == "connect" and len(message) == 1:
        ids, joueurs = connexion(client, ids, joueurs)
    elif message[0] == "quitter" and len(message) == 2:
        if int(message[1]) in joueurs:
            joueur = joueurs[int(message[1])]
            if not joueur.combat:
                del MAPS.get(joueur.map).joueurs[int(joueur.id)]
                del joueurs[int(joueur.id)]

    return ids, joueurs


def entitee_combat(id: int, joueurs: Dict) -> str:
    """Cette fonction transmet au joueur toute les informations sur un combat"""
    joueur = joueurs[int(id)]
    mobs = []
    if joueur.combat:
        for mob in joueur.combat.mobgroup:
            mobs.append((mob.name, mob.combat_coords, mob.var_attributs.hp))
        temp = []
        for players in joueur.combat.players:
            temp.append({"name": players.name, "classe": str(players.classe), "position": players.combat_coords})
        actif = False
        if joueur == joueur.combat.current:
            actif = True
        return dumps({"mobs": mobs, "joueurs": temp, "actif": actif, "position": joueur.combat_coords,
                      "vie": joueur.var_attributs.hp, "action": joueur.var_attributs.ap})
    return dumps({"": False})

def mouvement_combat(idjoueur: str, direction: str, joueurs: Dict):
    """Cette fonction sert a se déplacer si on est en combat"""
    if int(idjoueur) in joueurs.keys():
        joueur = joueurs[int(idjoueur)]
        if joueur.combat:
            if direction == "right":
                directionmouv = Mouvements.DROITE
            elif direction == "left":
                directionmouv = Mouvements.GAUCHE
            elif direction == "up":
                directionmouv = Mouvements.HAUT
            elif direction == "down":
                directionmouv = Mouvements.BAS
            else:
                return False
            return joueur.combat.move(joueur, directionmouv)


def lancer_sort(joueur: str, sort: str, cible: Tuple[int, int], joueurs: Dict):
    """Cette fonction permet aux joueurs de lancer des sorts"""
    if int(joueur) in joueurs.keys():
        fin_combat = False
        joueur = joueurs[int(joueur)]
        sort = SPELLS.get(joueur.classe.spells[sort])
        if sort.verif_conditions(joueur, cible):
            cibles = sort.liste_case(joueur, cible)
            for i in joueur.combat.queue:
                if i.combat_coords in cibles:
                    fin_combat = fin_combat or sort.appliquer_effet(i)
            return fin_combat
    return False


def commandecombat(message: List, client, joueurs: Dict):
    """Cette fonction efffectue toute les commandes liée au combat (attaque,déplacement,...)"""
    if message[0] == "carte" and len(message) == 2:
        client.send(str(entitee_combat(int(message[1]), joueurs)).encode())
    elif message[0] == "move" and len(message) == 3:
        client.send(str(mouvement_combat(message[1], message[2], joueurs)).encode())
    elif message[0] == "sort" and len(message) == 5:
        client.send(str(lancer_sort(message[1], message[2], (int(message[3]), int(message[4])), joueurs)).encode())
    elif message[0] == "endturn" and len(message) == 2:
        if int(message[1]) in joueurs.keys():
            joueurs[int(message[1])].combat.end_turn()
    elif message[0] == "quitter" and len(message) == 2:
        if int(message[1]) in joueurs:
            joueur = joueurs[int(message[1])]
            if joueur.combat:
                joueur.var_attributs.hp = -1
                combat = joueur.combat
                combat.players.remove(joueur)
                combat.joueurs_morts.append(joueur)
                combat.queue.remove(joueur)
                if len(combat.players) == 0:
                    combat.fin(False)
    return joueurs
