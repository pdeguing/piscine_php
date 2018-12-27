# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_is_sort.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 14:21:59 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 14:40:59 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_is_sort(tab):
    if all(tab[i] <= tab[i + 1] for i in range(len(tab) - 1)):
        return 1
    return 0

if __name__ == "__main__":
    tab = ["!/@#;^", "42", "Hello world", "salut", "zzzzeZZ"]

    if ft_is_sort(tab):
        print("Le tableau est trie")
    else:
        print("Le tableau n'est pas trie")
