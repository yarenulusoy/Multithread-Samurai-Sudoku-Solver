import threading
import time
import pygame
import matplotlib.pyplot as plt

dosyaislem = open("islem2.txt", "w")
f = open('sudoku.txt', 'r')

matris = [[int(num) for num in line.split(',')] for line in f]
matris2 = [[0 for i in range(21)] for j in range(21)]
for i in range(21):
    for j in range(21):
        matris2[i][j] = matris[i][j]
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

def draw2():
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


def solust1(threadname,sayi):
        start = time.time()
        if sayi==1:
            for row in range(0, 9):
                for column in range(0, 9):

                    if matris[row][column] == 0:
                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 1):
                                time.sleep(0.2)
                                matris[row][column] = number
                                global x, y
                                x = row
                                y = column
                                if solust1(threadname, sayi):
                                    str = repr(number)
                                    dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0

                        return
                    if row == 8 and column == 8:
                        return True
        if sayi==2:
            for row in range(8, -1, -1):
                for column in range(8, -1, -1):

                    if matris[row][column] == 0:
                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 1):
                                matris[row][column] = number
                                time.sleep(0.2)
                                x = row
                                y = column
                                if solust1(threadname, sayi):
                                    str = repr(number)
                                    dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0
                                    pygame.time.delay(1)
                        return
                    if row == 0 and column == 0:
                        return True


def sagust1(threadname, sayi):
    start = time.time()
    if sayi == 1:
        for row in range(0,9):
            for column in range(12, 21):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):

                            matris[row][column] = number
                            time.sleep(0.2)
                            global x, y
                            x = row
                            y = column
                            if sagust1(threadname, sayi):
                                str = repr(number)
                                dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return
                if row == 8 and column == 20:
                    return True
    if sayi == 2:
        for row in range(8, -1, -1):
            for column in range(12,21):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            time.sleep(0.2)
                            x = row
                            y = column
                            if sagust1(threadname, sayi):
                                str = repr(number)
                                dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return
                if row == 0 and column == 20:
                    return True


def solalt1(threadname,sayi):
        start = time.time()
        if sayi==1:
            for row in range(12, 21):
                for column in range(0, 9):

                    if matris[row][column] == 0:

                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 1):
                                matris[row][column] = number
                                time.sleep(0.2)

                                global x, y
                                x = row
                                y = column


                                if solalt1(threadname,sayi):
                                    str = repr(number)
                                    dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0

                        return

                    if column == 8 and row == 20:
                        return True

        if sayi==2:
            for row in range(20, 12, -1):
                for column in range(8, -1, -1):

                    if matris[row][column] == 0:

                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 1):
                                matris[row][column] = number
                                time.sleep(0.2)

                                x = row
                                y = column
                                if solalt1(threadname,sayi):
                                    pygame.time.delay(1)
                                    str = repr(number)
                                    dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0

                        return

                    if column == 0 and row == 0:
                        return True




def sagalt1(threadname,sayi):
    if sayi==1:
        start = time.time()
        global x, y
        for row in range(12, 21):
            for column in range(12, 21):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            time.sleep(0.2)
                            x = row
                            y = column


                            if sagalt1(threadname,sayi):
                                str = repr(number)
                                dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

                if column == 20 and row == 20:
                    return True
    if sayi == 2:
        start = time.time()
        for row in range(20, 11, -1):
            for column in range(20, 11, -1):

                if matris[row][column] == 0:
                    for number in range(1, 10):
                        if tahmin(matris, row, column, number, 1):
                            matris[row][column] = number
                            time.sleep(0.2)
                            x = row
                            y = column


                            if sagalt1(threadname, sayi):
                                str = repr(number)
                                dosyaislem.write(""+threadname + " calisti "+str + " numarayi yazdirdi.\n")
                                end = time.time()
                                zaman = end - start
                                x1.append(zaman)
                                return True
                            else:
                                matris[row][column] = 0

                    return

                if column == 0 and row == 0:
                    return True



def orta1(threadname,sayi):
        global x, y
        start = time.time()

        if sayi==1:
            for row in range(9, 12):
                for column in range(6, 15):

                    if matris[row][column] == 0:
                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 0):
                                matris[row][column] = number
                                str = repr(number)
                                dosyaislem.write("" + threadname + " calisti " + str + " numarayi yazdirdi.\n")
                                time.sleep(0.2)
                                x = row
                                y = column

                                if orta1(threadname, sayi):

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
                                str = repr(number)
                                dosyaislem.write("" + threadname + " calisti " + str + " numarayi yazdirdi.\n")
                                matris[row][column] = number
                                time.sleep(0.2)
                                x = row
                                y = column

                                if orta1(threadname, sayi):


                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0
                        return

                    if column == 11 and row == 14:
                        return True

        if sayi==2:
            for row in range(6, 9):
                for column in range(9, 12):
                    if matris[row][column] == 0:
                        for number in range(1, 10):
                            if tahmin(matris, row, column, number, 0):
                                matris[row][column] = number
                                str = repr(number)
                                dosyaislem.write("" + threadname + " calisti " + str + " numarayi yazdirdi.\n")
                                time.sleep(0.2)
                                x = row
                                y = column
                                if orta1(threadname, sayi):
                                    end = time.time()
                                    zaman = end - start
                                    x1.append(zaman)
                                    return True
                                else:
                                    matris[row][column] = 0

                        return

thread1 = threading.Thread(target=solust1,
                           args=("thread-1",1))
thread2 = threading.Thread(target=solust1,
                           args=("thread-2",2))
thread3 = threading.Thread(target=sagust1,
                           args=("thread-3",1))
thread4 = threading.Thread(target=sagust1,
                           args=("thread-4",2))
thread5 = threading.Thread(target=solalt1,
                           args=("thread-5",1))
thread6 = threading.Thread(target=solalt1,
                           args=("thread-6",2))
thread7 = threading.Thread(target=sagalt1,
                           args=("thread-7",1))
thread8 = threading.Thread(target=sagalt1,
                           args=("thread-8",2))
thread9 = threading.Thread(target=orta1,
                           args=("thread-9",1))
thread10 = threading.Thread(target=orta1,
                           args=("thread-10",2))


run = True
flag1 = 0
flag2 = 0
flag3 = 0
while run:

    screen.fill((200, 200, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag2 = 1

            if event.key == pygame.K_o:
                flag3 = 1

    if flag2== 1:

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()

        flag2 = 0





    if val != 0:
        draw_val(val)
        if tahmin(matris, int(x), int(y), val):
            matris[int(x)][int(y)] = val
            flag1 = 0
        else:
            matris[int(x)][int(y)] = 0

        val = 0

    draw()

    pygame.display.update()

pygame.quit()
y1 =[]
y2=[]
x2=[]

for i in range(1, len(x1) + 1):
    y1.append(i)



line_count = 0
zaman = open('time.txt', 'r')
for line in zaman:
    if line != "\n":
        line_count += 1
zaman.close()
for i in range(1, line_count+ 1):
    y2.append(i)

zaman = open('time.txt', 'r')
for line in zaman:
    x2.extend([float(i) for i in line.split()])


zaman.close()

plt.plot(x2, y2, label="Thread-5")
plt.plot(x1, y1, label="Thread-10")

plt.xlabel('x - sure')
plt.ylabel('y - buldugu kare sayisi')
plt.legend()
plt.show()
