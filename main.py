import uinput
import GameController
SERIAL_PORT = "/dev/rfcomm0"
BTN_P1_BLUE =34
BTN_P1_RED =32
BTN_P1_YELLOW =30
BTN_P1_UP =28
BTN_P1_DOWN =24
BTN_P1_LEFT =26
BTN_P1_RIGHT =22
BTN_P2_BLUE =40
BTN_P2_RED =38
BTN_P2_YELLOW =36
BTN_P2_UP =48
BTN_P2_DOWN =44
BTN_P2_LEFT =46
BTN_P2_RIGHT =42
BTN_PLAYER_A =50
BTN_PLAYER_B =52


def main():
    controller = GameController.GameController(SERIAL_PORT)
    events = (
        #Player A
        uinput.ABS_X + (-1, 1, 0, 0),
        uinput.ABS_Y + (-1, 1, 0, 0),
        uinput.BTN_0,
        uinput.BTN_1,
        uinput.BTN_2,
        #Player B
        uinput.ABS_RX + (-1, 1, 0, 0),
        uinput.ABS_RY + (-1, 1, 0, 0),
        uinput.BTN_3,
        uinput.BTN_4,
        uinput.BTN_5,
        uinput.BTN_6,
        uinput.BTN_7,
        uinput.BTN_JOYSTICK,
    )
    
    device = uinput.Device(events) 
    device.emit_click(uinput.BTN_JOYSTICK)
    while 1:
        _events = controller.get_events()
        for i in _events:
            if i[1] == 1:
                if i[0] == BTN_PLAYER_A:
                    device.emit(uinput.BTN_6,1)
                elif i[0] == BTN_PLAYER_B:
                    device.emit(uinput.BTN_7,1)




                elif i[0] == BTN_P1_UP:
                    device.emit(uinput.ABS_Y,-1)
                elif i[0] == BTN_P1_DOWN:
                    device.emit(uinput.ABS_Y,1)
                elif i[0] == BTN_P1_LEFT:
                    device.emit(uinput.ABS_X,-1)
                elif i[0] == BTN_P1_RIGHT:
                    device.emit(uinput.ABS_X,1)
                elif i[0] == BTN_P1_BLUE:
                    device.emit(uinput.BTN_0,1)
                elif i[0] == BTN_P1_RED:
                    device.emit(uinput.BTN_1,1)
                elif i[0] == BTN_P1_YELLOW:
                    device.emit(uinput.BTN_2,1)



                elif i[0] == BTN_P2_UP:
                    device.emit(uinput.ABS_RY,-1)
                elif i[0] == BTN_P2_DOWN:
                    device.emit(uinput.ABS_RY,1)
                elif i[0] == BTN_P2_LEFT:
                    device.emit(uinput.ABS_RX,-1)
                elif i[0] == BTN_P2_RIGHT:
                    device.emit(uinput.ABS_RX,1)
                elif i[0] == BTN_P2_BLUE:
                    device.emit(uinput.BTN_3,1)
                elif i[0] == BTN_P2_RED:
                    device.emit(uinput.BTN_4,1)
                elif i[0] == BTN_P2_YELLOW:
                    device.emit(uinput.BTN_5,1)




            elif i[1] == 0:
                if i[0] == BTN_PLAYER_A:
                    device.emit(uinput.BTN_6,0)
                elif i[0] == BTN_PLAYER_B:
                    device.emit(uinput.BTN_7,0)





                if i[0] == BTN_P1_UP:
                    device.emit(uinput.ABS_Y,0)
                elif i[0] == BTN_P1_DOWN:
                    device.emit(uinput.ABS_Y,0)
                elif i[0] == BTN_P1_LEFT:
                    device.emit(uinput.ABS_X,0)
                elif i[0] == BTN_P1_RIGHT:
                    device.emit(uinput.ABS_X,0)
                elif i[0] == BTN_P1_BLUE:
                    device.emit(uinput.BTN_0,0)
                elif i[0] == BTN_P1_RED:
                    device.emit(uinput.BTN_1,0)
                elif i[0] == BTN_P1_YELLOW:
                    device.emit(uinput.BTN_2,0)


                elif i[0] == BTN_P2_UP:
                    device.emit(uinput.ABS_RY,0)
                elif i[0] == BTN_P2_DOWN:
                    device.emit(uinput.ABS_RY,0)
                elif i[0] == BTN_P2_LEFT:
                    device.emit(uinput.ABS_RX,0)
                elif i[0] == BTN_P2_RIGHT:
                    device.emit(uinput.ABS_RX,0)
                elif i[0] == BTN_P2_BLUE:
                    device.emit(uinput.BTN_3,0)
                elif i[0] == BTN_P2_RED:
                    device.emit(uinput.BTN_4,0)
                elif i[0] == BTN_P2_YELLOW:
                    device.emit(uinput.BTN_5,0)

if __name__ == "__main__":
    main()
