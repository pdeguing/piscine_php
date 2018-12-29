# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loupe.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/28 14:34:10 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/28 14:59:23 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

def edit_link(match):
	return (match.group(1) + match.group(2).upper() + match.group(3))	

def loupe(filename):
	with open(filename) as f:
		read_data = f.read()
	new = re.sub(r'(<a.*?title=")(.*?)(">)|(<a.*?>)(.*?)(<)', edit_link, read_data)
	new = re.sub(r'(<a.*?>)(.*?)(<)', edit_link, new)
	print(new)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loupe(sys.argv[1])
