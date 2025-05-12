from hub import light_matrix, port, sound
import time
import color_sensor
import color
import distance_sensor
import motor
import motor_pair
import runloop
import random
# подключить touch sensor (кнопка)
import force_sensor
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

async def main():
    motor_pair.move(motor_pair.PAIR_1, 1000)
    time.sleep(2000)
    motor_pair.stop(motor_pair.PAIR_1)

    motor.run(port.A, 1000)
    time.sleep(2000)
    motor.stop(port.A)

    # если touch sensor нажать то true
    # иначе false
    if force_sensor.pressed(port.C):
        await light_matrix.write("Hi!")

    # range 0 to 100
    # иначе говоря чем сильнее нажимаете на toush sensor тем больше значение
    if force_sensor.force(port.C) > 50:
                await light_matrix.write("Hi!")

    if color_sensor.color(port.A) == color.BLACK:
            await light_matrix.write("Hi!")

    if distance_sensor.distance(port.B) < 100:
            sound.beep(220, 100)


    await light_matrix.write("Hi!")

runloop.run(main())
