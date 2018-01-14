#!/usr/bin/env python
# Author: Jarrett B. <sircuddles@icloud.com> Made with Slovene pride
# coding: utf-8

from __future__ import absolute_import, division, print_function
from collections import namedtuple
from datetime import datetime as DateTime
from hashlib import md5
import pymysql.cursors

cnx = pymysql.connect(user='root', db='altislife')
cursor = cnx.cursor()

class Player(namedtuple('Player', 'guid steam_id note')):

    def __str__(self):
        return '{0.guid} {0.steam_id} {0.note}'.format(self)


def log(prefix, suffix=''):
    #
    # TODO: Replace with `logging`.
    #
    print(
        '{0} {1:%Y-%m-%d %H:%M:%S} {2}'.format(prefix, DateTime.now(), suffix)
    )


def steam_id_to_guid(steam_id):
    temp = ['BE']
    for _ in xrange(8):
        temp.append(chr(steam_id & 0xFF))
        steam_id >>= 8
    return md5(''.join(temp)).hexdigest()


def iter_players(filename):
    with open(filename) as lines:
        for line in lines:
            yield Player(line[:32], None, line[32:])


def brute_force(guid2player):
    playerIDs = []
    cursor.execute("SELECT * FROM players")
    for (players) in cursor:
        playerIDs.append(int(players[3]))
    for steam_id in playerIDs:
        guid = steam_id_to_guid(steam_id)
        try:
            player = guid2player.pop(guid)
        except KeyError:
            pass
        else:
            log('Found at:', ' {0} {1}'.format(guid, steam_id))
            yield player._replace(steam_id=steam_id)
            if not guid2player:
                break


def print_players(players, label):
    print(label)
    for player in players:
        print(player)


def main():
    log('Start:')
    # File must contain one or more GUIDs. One guid per line
    guid2player = dict(
        (player.guid, player)
        for player in iter_players('GUIDs.txt')
    )
    decoded_players = sorted(
        brute_force(guid2player)
    )


    log('End:')
    print_players(sorted(guid2player.itervalues()), 'Coded list:')
    print_players(decoded_players, 'Decoded list:')


if __name__ == '__main__':
    main()
