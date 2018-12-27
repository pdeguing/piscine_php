# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ssap2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 15:28:20 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 15:28:25 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

"""
    Please note that ## will not be send as input by bash/sh
"""

def ssap(av):
    if len(av) < 2:
        return
    words = []
    for arg in av[1:]:
        words.extend(arg.split())
    words.sort(key=str.lower)
    numbers = []
    others = []
    for word in words:
        if word[0].isalpha():
            print(word)
        elif word[0].isdigit():
            numbers.append(word)
        else:
            others.append(word)
    for number in numbers:
        print(number)
    for other in others:
        print(other)

if __name__ == "__main__":
    ssap(sys.argv)
