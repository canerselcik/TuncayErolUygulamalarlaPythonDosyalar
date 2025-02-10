import turtle
import time

# Kalp çizme fonksiyonu
kalp = turtle.Turtle()
kalp.color("red")
kalp.speed(3)
kalp.penup()
kalp.goto(0, -240)  # Kalbin konumu daha aşağıya taşındı
kalp.pendown()

def draw_heart():
    kalp.begin_fill()
    kalp.left(50)
    kalp.forward(133)
    kalp.circle(50, 200)
    kalp.right(140)
    kalp.circle(50, 200)
    kalp.forward(133)
    kalp.end_fill()
    kalp.hideturtle()

# Deprem etkisini simgeleyen shake_effect fonksiyonu
def shake_effect():
    for _ in range(10):
        kalp.setx(kalp.xcor() + 10)
        kalp.setx(kalp.xcor() - 20)
        kalp.setx(kalp.xcor() + 10)
        time.sleep(0.1)

# Kelime kelime gelen anma mesajını gösteren fonksiyon
def display_message():
    mesaj = "Kayıplarımızı saygıyla anıyoruz."
    kalp.penup()
    kalp.goto(0, 0)
    kalp.color("black")
    kalp.hideturtle()
    for harf in mesaj:
        kalp.write(harf, move=True, align="center", font=("Arial", 24, "normal"))
        time.sleep(0.2)

# *Anma Animasyonu Başlat*
shake_effect()  # Deprem etkisini simgele
display_message()  # Anma mesajını göster
draw_heart()  # Kayıplarımız için kalp çiz

# Sonsuz döngüyle ekranı açık tut
turtle.done()
