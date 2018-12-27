# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_split.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 11:12:02 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 12:02:00 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_split(s1):
    if s1 is not str:
        return
    words = s1.split()
    words.sort()
    return words 

"""
if __name__ == '__main__':
    for word in ft_split(18):
        print(word)
"""
