from time import sleep

import rospy
import speech_recognition as sr

import control_uav


def main():
    r = sr.Recognizer()
    rospy.init_node("dron_speech")
    sleep(2)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            audio = r.listen(source, 5, 3)
            try:
                text = r.recognize_google(audio, language="es-MX")
                text = text.lower() + "."
                print(text)
                if text == "despegar.":
                    control_uav.setMode("GUIDED")
                    sleep(2)
                    control_uav.setArm()
                    sleep(2)
                    control_uav.setTakeofMode()
                    sleep(5)
                    print("Listening...")
                if text == "aterrizar.":
                    control_uav.setLandMode()
                    sleep(15)
                    print("Listening...")
                if text == "adiós.":
                    break
            except sr.UnknownValueError:
                print("Listening...")


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass