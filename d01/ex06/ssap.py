# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ssap.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 12:25:28 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 12:38:55 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ssap(av):
    if len(av) < 2:
        return
    words = []
    for arg in av[1:]:
        words.extend(arg.split())
    words.sort()
    for word in words:
        print(word)

if __name__ == "__main__":
    ssap(sys.argv)
