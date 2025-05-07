from hub import light_matrix, port, sound
import time
import color_sensor
import color
import distance_sensor
import motor
import motor_pair
import runloop
import random
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

async def main():
    motor_pair.move(motor_pair.PAIR_1, 1000)
    time.sleep(2000)
    motor_pair.stop(motor_pair.PAIR_1)

    motor.run(port.A, 1000)
    time.sleep(2000)
    motor.stop(port.A)
    
    if color_sensor.color(port.A) == color.BLACK:
            await light_matrix.write("Hi!")

    if distance_sensor.distance(port.B) < 100:
            sound.beep(220, 100)


    await light_matrix.write("Hi!")

runloop.run(main())
