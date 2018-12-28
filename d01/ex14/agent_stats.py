# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    agent_stats.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 16:47:00 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 17:02:24 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def create_dic(argv):
    return

def moyenne(dic):
    return

def moyenne_user(dic):
    return

def ecart_moulinette(dic):
    return

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dic = create_dic(sys.argv)
        if sys.argv[1] == "moyenne":
            moyenne(dic)
        elif sys.argv[1] == "moyenne_user":
            moyenne_user(dic)
        elif sys.argv[1] == "ecart_moulinette":
            ecart_moulinette(dic)
