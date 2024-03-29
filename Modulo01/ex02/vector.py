# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/24 12:28:07 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/24 16:29:49 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = self.get_shape()
    def __str__(self):
        return str(self.values)
    def get_shape(self):
        filas = len(self.values)
        columnas = len(self.values[0])
        if columnas == 1:
            (1, filas)
        else: 
            (columnas, 1)
        return(filas, columnas) 
        
    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError ("Shaper vector no son iguales")
        result = 0
        for i in range(self.shape[1]):
            result += self.values[0][i] * other.values[0][1]
        return result
    def T(self):
        values_T = [[self.values[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])]
        return Vector(values_T)
    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shaper vector no son iguales")
        values = [[self.values[i][j] + other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(values)
    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shaper vector no son iguales")
        values = [[self.values[i][j] - other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(values)
    def __mul__(self, scalar):
        values = [[self.values[i][j] * scalar for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(values)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    def __truediv__(self, scalar):
        values = [[self.values[i][j] / scalar for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(values)
    def __rtruediv__(self, scalar):
        raise ArithmeticError("Vectors cannot be divided by scalars from the right.")