import threading
import time
import pygame
import matplotlib.pyplot as plt

dosyaislem = open("islem.txt", "w")
zaman = open("time.txt", "w")
f = open('sudoku.txt', 'r')
matris = [[int(num) for num in line.split(',')] for line in f]
matris2 = [[int(num) for num in line.split(',')] for line in f]

pygame.font.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("SAMURAI SUDOKU COZUCU")
x = 0
y = 0
dif = 700 // 21
val = 0
x1 = []

font1 = pygame.font.SysFont("comicsans", 20)
font2 = pygame.font.SysFont("comicsans", 10)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


def draw():
    for i in range(21):
        for j in range(21):

            if matris[i][j] != 0:
                pygame.draw.rect(screen, (186, 122, 255), (j * dif, i * dif, dif + 1, dif + 1))
                if matris[i][j] == -1:
                    pygame.draw.rect(screen, (10, 0, 0), (j * dif, i * dif, dif + 1, dif + 1))
                if (matris[i][j] != -1):
                    val = font1.render(str(matris[i][j]), 1, (0, 0, 0))
                    screen.blit(val, (
                        1 + j * dif + (dif // 2 - val.get_width() // 2),
                        3 + i * dif + (dif // 2 - val.get_height() // 2)))
    for i in range(22):
        if i % 3 == 0:
            thick = 3
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif + 1), (750 + 2, i * dif + 1), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif + 1, 0), (i * dif + 1, 750), thick)
        else:
            thick = 1
            pygame.draw.line(screen, (0, 0, 0), (3, i * dif + 1), (750, i * dif + 1), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif + 1, 3), (i * dif + 1, 750), thick)


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


def tahmin(matris, row, column, number, x):
    if x == 1:
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if matris[y0 + i][x0 + j] == number:
                    return False

        # sol ust
        if row < 9 and column < 9:
            if row == 6 and column == 6 or row == 6 and column == 7 or row == 6 and column == 8 or row == 7 and column == 6 \
                    or row == 7 and column == 7 or row == 7 and column == 8 or row == 8 and column == 6 or row == 8 and column == 7 or row == 8 and column == 8:
                for i in range(0, 9):
                    if matris[row][i] == number:
                        return False

                for i in range(6, 15):
                    if matris[row][i] == number:
                        return False

                for i in range(6, 15):
                    if matris[i][column] == number:
                        return False

                for i in range(0, 9):
                    if matris[i][column] == number:
                        return False

            else:
                for i in range(0, 9):
                    if matris[row][i] == number:
                        return False

                for i in range(0, 9):
                    if matris[i][column] == number:
                        return False


        # sag üst
        elif row < 9 and column >= 12:
            if row == 6 and column == 12 or row == 6 and column == 13 or row == 6 and column == 14 or row == 7 and column == 12 \
                    or row == 7 and column == 13 or row == 7 and column == 14 or row == 8 and column == 12 or row == 8 and column == 13 or row == 8 and column == 14:
                for i in range(6, 15):
                    if matris[row][i] == number:
                        return False

                for i in range(12, 21):
                    if matris[row][i] == number:
                        return False

                for i in range(6, 15):
                    if matris[i][column] == number:
                        return False

                for i in range(0, 9):
                    if matris[i][column] == number:
                        return False

            else:
                for i in range(12, 21):
                    if matris[row][i] == number:
                        return False

                for i in range(0, 9):
                    if matris[i][column] == number:
                        return False

        # sol alt
        elif row >= 12 and column < 9:
            if row == 12 and column == 6 or row == 12 and column == 7 or row == 12 and column == 8 or row == 13 and column == 6 \
                    or row == 13 and column == 7 or row == 13 and column == 8 or row == 14 and column == 6 or row == 14 and column == 7 or row == 14 and column == 8:
                for i in range(0, 9):
                    if matris[row][i] == number:
                        return False

                for i in range(6, 15):
                    if matris[row][i] == number:
                        return False

                for i in range(12, 21):
                    if matris[i][column] == number:
                        return False

                for i in range(6, 15):
                    if matris[i][column] == number:
                        return False
            else:
                for i in range(0, 9):
                    if matris[row][i] == number:
                        return False

                for i in range(12, 21):
                    if matris[i][column] == number:
                        return False

        # sağ alt
        elif row >= 12 and column >= 12:

            if (row == 12 and column == 12) or (row == 12 and column == 13) or (row == 12 and column == 14) or (
                    row == 13 and column == 12) \
                    or (row == 13 and column == 13) or (row == 13 and column == 14) or (row == 14 and column == 12) or (
                    row == 14 and column == 13) or (row == 14 and column == 14):

                for i in range(12, 21):
                    if matris[row][i] == number:
                        return False

                for i in range(12, 21):
                    if matris[i][column] == number:
                        return False

                for i in range(6, 15):
                    if matris[row][i] == number:
                        return False

                for i in range(6, 15):
                    if matris[i][column] == number:
                        return False

            else:
                for i in range(12, 21):
                    if matris[row][i] == number:
                        return False

                for i in range(12, 21):
                    if matris[i][column] == number:
                        return False

        return True
        # orta
    if x == 0:

        if 6 <= row <= 14 and 14 >= column >= 6:
            for i in range(6, 15):  # row13
                if matris[row][i] == number:
                    return False

            for i in range(6, 15):  # column 9
                if matris[i][column] == number:
                    return False

        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if matris[y0 + i][x0 + j] == number:
                    return False
        return True


class solust(threading.Thread):
    def run(self):
        start = time.time()
        for row in range(8, -1, -1):
            for column in range(8, -1, -1):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-1 calisti " + str + " numarayi yazdirdi.\n")
                            global x, y
                            x = row
                            y = column
                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0
                                pygame.time.delay(1)
                    return

                if column == 0 and row == 0:
                    return True

        for i in range(9):
            for j in range(9):
                matris2[i][j] = matris[i][j]


class sagust(threading.Thread):
    def run(self):
        start = time.time()
        for row in range(8, -1, -1):
            for column in range(12, 21):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-2 calisti " + str + " numarayi yazdirdi.\n")
                            global x, y
                            x = row
                            y = column

                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

                if column == 20 and row == 0:
                    return True




class solalt(threading.Thread):
    def run(self):
        start = time.time()

        for row in range(12, 21):
            for column in range(0, 9):

                if matris[row][column] == 0:

                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-3 calisti " + str + " numarayi yazdirdi.\n")

                            global x, y
                            x = row
                            y = column
                            pygame.time.delay(1)

                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

                if column == 8 and row == 20:
                    return True




class sagalt(threading.Thread):
    def run(self):
        start = time.time()
        global x, y
        for row in range(12, 21):
            for column in range(12, 21):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-4 calisti " + str + " numarayi yazdirdi.\n")
                            x = row
                            y = column
                            pygame.time.delay(2)

                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

                if column == 20 and row == 20:
                    return True



class orta(threading.Thread):
    def run(self):
        global x, y
        start = time.time()
        for row in range(9, 12):
            for column in range(6, 15):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 0):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-5 calisti " + str + " numarayi yazdirdi.\n")
                            x = row
                            y = column
                            pygame.time.delay(2)

                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

        for row in range(6, 9):
            for column in range(9, 12):
                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 0):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-5 calisti " + str + " numarayi yazdirdi.\n")
                            x = row
                            y = column

                            pygame.time.delay(2)
                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

        for row in range(12, 15):
            for column in range(9, 12):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 0):
                            matris[row][column] = number
                            str = repr(number)
                            dosyaislem.write("thread-5 calisti " + str + " numarayi yazdirdi.\n")
                            x = row
                            y = column
                            pygame.time.delay(2)

                            if self.run():
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0
                    return

                if column == 11 and row == 14:
                    return True


t1 = solust()
t2 = sagust()
t3 = solalt()
t4 = sagalt()
t5 = orta()

run = True
flag1 = 0
flag2 = 0
flag3 = 0
while run:

    screen.fill((200, 200, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag2 = 1


    if flag2== 1:

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        flag2 = 0

    if val != 0:
        draw_val(val)
        if tahmin(matris, int(x), int(y), val):
            matris2[int(x)][int(y)] = val
            flag1 = 0
        else:
            matris[int(x)][int(y)] = 0

        val = 0

    draw()

    pygame.display.update()

pygame.quit()
y1 = []

for i in range(1, len(x1) + 1):
    y1.append(i)

plt.plot(x1, y1, label="line 1")
for i in x1:
    a=repr(i)
    zaman.write(a+"\n")
x2 = [10, 5]
y2 = [5, 2]
plt.plot(x2, y2, label="line 2")
print(x1)
plt.xlabel('x - sure')
plt.ylabel('y - buldugu kare sayisi')
plt.legend()
plt.show()
