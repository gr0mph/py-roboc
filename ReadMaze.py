#!/usr/bin/python3
# -*-coding:Utf-8 -*

import DictBlock
from block.Block import Block

class ReadMaze:

    def __init__(self, name):
        """ Lis le fichier Maze 
        à partir du nom qui est donne 
        et du repertoire file-maze

        Cree les blocks - obstacles dans la liste self.maze
        Cette classe contient le framework iteration
        """       
        self.name = name
        self.read()
        self.position = (-1,0)
        
    def save(self):
        """
        Sauvegarde du fichier
        """
        try:
            with open("file-maze/00-tmp-maze.txt", "w") as fileMaze:
                index = 0                
                for block in self.maze:
                    if index == self.ligne:
                        index = 0
                        fileMaze.write('\n')
                    
                    if block == None:
                        fileMaze.write('-')
                    else:
                        fileMaze.write(block.abbrevation)
                    index = index + 1

        except TypeError:
            pass

    def read(self):
        """
        Lecture du fichier passer en parametre dans le init
        Necessaire car maintenant des blocks peuvent changer
        """
        try:
            with open(self.name, "r") as fileMaze:
                self.maze = []
                self.colonne = 0
                self.ligne = 0
                a = 0
                b = 0
                for line in fileMaze:
                    for x in line:
                        if x == '\n':
                            a = 0
                            b = b + 1
                            continue
                        x = DictBlock.dict_Block[x]
                        if x:
                            block = x(a,b)
                            self.maze.append(block)
                        else:
                            self.maze.append(None)
                        a = a + 1
                    
                    self.colonne = len(line.strip())
                    self.ligne = self.ligne + 1

        except TypeError:
            pass

    def __iter__(self):
        return self

    def __next__(self):
        a, b = self.position
        if a + 1 == self.colonne and b + 1 == self.ligne :
            raise StopIteration
        elif a + 1 == self.colonne :
            a = 0
            b = b + 1
        else :
            a = a + 1
        self.position = (a,b)
        return self.position

    def brick(self, position) :
        """
        Renvois le block demande a la position demandee
        Si pas de block renvois None
        """
        (a,b) = position
        index = b * self.colonne + a
        return self.maze[index]

    def replace(self, position) :
        """
        Remplace un block - obstacle par un autre block
        """        
        (a,b) = position
        index = b * self.colonne + a
        block = self.maze[index]
        alterable = block.alterable
        self.maze[index] = DictBlock.dict_Block[alterable]
        if self.maze[index]:
            self.maze[index] = self.maze[index](a,b)

    

# Main inclus issu
if __name__ == "__main__" :
    test = ReadMaze("file-maze/01-maze.txt")
    print()
    for (a,b) in test :
        if a == 0 :
            print("{:2d}".format(b) , end = " ")
        print("{:2d}".format(a) , end = " ")
        if a + 1 == test.colonne :
            print()
        #print( (test.brick( (a,b) )) )
    print()

    test.save()


