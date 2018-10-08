#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:30:28 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# To do list:
# 	- not, and, xor, or in conclusions
# 	- double implies (if and only if)
# 	- nand, nor, exnor
#	- config that supports english_conditions

import sys
sys.path.extend(["./src/", "./src/parser/", "./src/graph/"])

from Parser import Parser
from Lexer import Lexer
from Graph import Graph

def main():
	if len(sys.argv) != 2:
		exit("\033[1;32m[Usage] \033[1;37m./expert_system.py file")
	try:
		lexer = Lexer(sys.argv[1])
		parser = Parser(lexer.config)
		graph = Graph(lexer.config)
		graph.solve()
	except Exception as ex:
		exit(ex)

if __name__== "__main__":
	main()
