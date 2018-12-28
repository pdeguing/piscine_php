# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    another_world.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/28 08:28:57 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/28 10:15:21 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

def another_world(argv):
    print(re.sub(r'\s+', r' ', argv[1]).strip())

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        another_world(sys.argv)
