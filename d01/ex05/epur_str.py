# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    epur_str.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 12:09:41 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 12:22:53 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(' '.join(sys.argv[1].split()))