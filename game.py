import pygame
import random as rnd

# Constants
width = 1000
height = 600
grid_size = 10

snake_color = (0, 255, 0)
black_color = (0, 0, 0)
apple_color = (255, 0, 0)

fps = 30
start_y_pos = (width/grid_size)/2
# =======================
left = 1
right = 2
up = 3
down = 4

down_edge = height/grid_size
up_edge = 0
right_edge = width/grid_size
left_edge = 0
# =======================
direction = right
# ----------------------

# Initializations
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen.fill(black_color)


def generate_snake(length=3):
    for i in range(length):
        tail.append([i, start_y_pos])

def draw_block(x, y, color):
    block = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, color, block, 0)

def update_snake():
    screen.fill(black_color)
    for block in tail:
        draw_block(block[0], block[1], snake_color)
        
def update_apple():
    draw_block(apple[0], apple[1], apple_color)
        
def update_screen():
    update_snake()
    update_apple()
    

def move_snake():
    if direction == left:
        last_tail_block = tail.pop(0)#удаляем последний элемент хвоста
        tail.append(last_tail_block)#Добавляем его в начало
        tail[len(tail)-1][1] = tail[len(tail)-2][1]#перерисовываем в соответствии с координатами головы
        tail[len(tail)-1][0] = tail[len(tail)-2][0] - 1

    elif direction == right:
        last_tail_block = tail.pop(0)
        tail.append(last_tail_block)
        tail[len(tail)-1][1] = tail[len(tail)-2][1]
        tail[len(tail)-1][0] = tail[len(tail)-2][0] + 1

    elif direction == up:
        last_tail_block = tail.pop(0)
        tail.append(last_tail_block)
        tail[len(tail)-1][0] = tail[len(tail)-2][0]
        tail[len(tail)-1][1] = tail[len(tail)-2][1] - 1

    elif direction == down:
        last_tail_block = tail.pop(0)
        tail.append(last_tail_block)
        tail[len(tail)-1][0] = tail[len(tail)-2][0]
        tail[len(tail)-1][1] = tail[len(tail)-2][1] + 1


def get_input(direction):
    for event in pygame.event.get():#Обрабатываем нажатия клавиатуры
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != right:
                direction = left
            elif event.key == pygame.K_RIGHT and direction != left:
                direction = right
            elif event.key == pygame.K_UP and direction != down:
                direction = up
            elif event.key == pygame.K_DOWN and direction != up:
                direction = down
    return direction

def spawn_apple():#Генерируем яблоко
    apple_coord = [rnd.randint(left_edge, right_edge-1), rnd.randint(up_edge, down_edge-1)]
    while apple_coord in tail:#Проверяем совпадение с координатами змеи
        apple_coord[0] = rnd.randint(left_edge, right_edge-1)
        apple_coord[1] = rnd.randint(up_edge, down_edge-1)
    return apple_coord
    
# Main programm
tail = []
generate_snake(5)
last_tail_block = tail[0]

apple = spawn_apple()
update_apple()

running = True
while running:
    clock.tick(fps)

    direction = get_input(direction)
    
    move_snake()

    if(tail[len(tail)-1][0] == right_edge or tail[len(tail)-1][0] == left_edge-1 or
        tail[len(tail)-1][1] == down_edge or tail[len(tail)-1][1] == up_edge-1):#Если змея упёрлась в стену, заканчиваем игру
        running = False
    
    if (tail.count(tail[len(tail)-1]) > 1):#Если змея укусила сама себя, заканчиваем игру
        running = False
        
    if(tail[len(tail)-1][0] == apple[0] and tail[len(tail)-1][1] == apple[1]):#Если змея съела яблоко добавляем его в хвост и спавним новое
        tail.insert(0, apple)
        apple = spawn_apple()
        
    
    update_screen()
    pygame.display.flip()#обновляем экран

print("exit")
