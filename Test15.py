from sys import stdin

class Soup:

    #Create a new board
    def __init__(self, b):
        self.board = b
        self.words = []

    #Show the created board to the user
    def start(self):
        for row in self.board:
            for letter in row:
                print(letter + " ", end="")
            print()
        self.search()
    
    #Storage the words that the user wants to be searched
    def search(self):
        print()
        print("Enter the quantity of words to search: ")
        quantity = int(stdin.readline())
        print("Enter the words to search")
        for i in range(quantity):
            word = stdin.readline().strip()
            self.words.append(word)
        self.solve()

    #Search the words that the user entered
    def solve(self):
        for word in self.words:
            found = False
            print("Searching " + word)
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                    #Verify if the current letter in the board equals to the first letter in the word to search
                    if self.board[row][column] == word[0]:
                        #If the previous statement is true, the word will be searched in the 3 possible ways
                        if self.vertical(row, column, word):
                            found = True
                        if self.horizontal(row, column, word):
                            found = True
                        if self.diagonal(row, column, word):
                            found = True
            if found == False:
                print(word + " Not found")       
                print()            
 
    #Search word in a vertical flow
    def vertical(self, row, column, word):
        ans = True
        wordPos = 0
        r = row
        c = column
        #Verify that the word can be vertical in the board without surpassing the boundaries
        if len(word) + r - 1 < len(self.board):
            while ans == True and r < len(self.board):
                if wordPos + 1 == len(word) and word[wordPos] == self.board[r][c]:
                    r = len(self.board)
                elif word[wordPos] == self.board[r][c]:
                    r += 1
                    wordPos += 1
                else: 
                    ans = False
        else:
            ans = False
        if ans:
            for i in range(len(word)):
                print(word[i], "- [" + str(row) + ", " + str(column) + "]")
                row += 1
            print()
        return ans

    #Search word in an horizontal flow
    def horizontal(self, row, column, word):
        ans = True
        wordPos = 0
        r = row
        c = column
        #Verify that the word can be horizontal in the board without surpassing the boundaries
        if len(word) + c - 1 < len(self.board[0]):
            while ans == True and c < len(self.board[0]):
                if wordPos + 1 == len(word) and word[wordPos] == self.board[r][c]:
                    c = len(self.board[0])
                elif word[wordPos] == self.board[r][c]:
                    c += 1
                    wordPos += 1
                else: 
                    ans = False
        else:
            ans = False
        if ans:
            for i in range(len(word)):
                print(word[i], "- [" + str(row) + ", " + str(column) + "]")
                column += 1
            print()
        return ans

    #Search word in an diagonal flow
    def diagonal(self, row, column, word):
        ans = True
        wordPos = 0
        r = row
        c = column
        #Verify that the word can be diagonal in the board without surpassing the boundaries
        if len(word) + c - 1 < len(self.board[0]) and len(word) + r - 1 < len(self.board):
            while ans == True and c < len(self.board[0]) and r < len(self.board):
                if wordPos + 1 == len(word) and word[wordPos] == self.board[r][c]:
                    c = len(self.board[0])
                elif word[wordPos] == self.board[r][c]:
                    c += 1
                    r += 1
                    wordPos += 1
                else: 
                    ans = False
        else:
            ans = False
        if ans:
            for i in range(len(word)):
                print(word[i], "- [" + str(row) + ", " + str(column) + "]")
                column += 1
                row += 1
            print()
        return ans

def main():
    print("Enter the soup rows quantity: ")
    print()
    soup = []
    rows = int(stdin.readline())
    for i in range(rows):
        line = stdin.readline()
        soup.append(list(map(str, line.strip().split(" "))))
    
    print("Press 1 to start the game")
    print("Press 0 to finish")
    option = int(stdin.readline())
    print("----------------------------------")
    print("Soup")
    print()
    if option:
        game = Soup(soup)
        game.start()

main()