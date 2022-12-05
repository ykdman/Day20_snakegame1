# Day 20 : Snake Game .Part1
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # 스크린 컬러 변경
screen.title("My Snake Game")  # 화면 제목
screen.tracer(0)  # Animation 끄기

snake = Snake()
food = Food()  # 먹이 클래스
scoreboard = Scoreboard()


# 키 입력 받기
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 1초씩 딜레이
    snake.move()

    # Detect collision with food. = 먹이와 충돌 감지
    if snake.head.distance(food) < 15:  # head 는 snake 에서 선언된 뱀의 머리 = segment[0]
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Dectect collision with wall = 벽과의 충돌 감지
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
