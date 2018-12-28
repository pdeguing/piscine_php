# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    one_more_time.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/28 10:17:33 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/28 12:47:32 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re
import datetime
from datetime import timezone

def get_month(month):
    m = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    for word in m:
        if (month == word) or (month == word.capitalize()):
            return m.index(word) + 1
    return -1

def verif_day(day):
    d = ["monday", "tuesday", "wenesday", "thursday", "friday", "saturday", "sunday"]
    for word in d:
        if (day == word) or (day == word.capitalize()):
            return True
    return False

def one_more_time(s1):
    match = re.search(r'([a-zA-Z]*) (\d\d?) ([a-zA-Z]*) (\d\d\d\d) (\d\d):(\d\d):(\d\d)$', s1)
    if match and verif_day(match.group(1)):
        year = int(match.group(4))
        month = get_month(match.group(3))
        day = int(match.group(2))
        hours = int(match.group(5))
        minutes = int(match.group(6))
        seconds = int(match.group(7))
        try:
            d = datetime.datetime(year, month, day, hours, minutes, seconds).replace(tzinfo=timezone.utc)
            print(int(d.timestamp()))
        except ValueError:
            print("Wrong Format")
    else:
        print("Wrong Format")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        one_more_time(sys.argv[1])
