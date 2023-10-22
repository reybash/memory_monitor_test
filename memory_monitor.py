import psutil
import requests
import time

# Задайте порог для использования памяти в процентах
MEMORY_THRESHOLD_PERCENT = 80

# Задайте URL для отправки запроса
ALARM_URL = "http://localhost:5000/alarm"


def check_memory_usage():
    # Получаем информацию о памяти
    memory_percent = psutil.virtual_memory().percent

    if memory_percent > MEMORY_THRESHOLD_PERCENT:
        return True
    else:
        return False


def send_alarm():
    # Отправляем HTTP-запрос
    try:
        response = requests.get(ALARM_URL)
        if response.status_code == 200:
            print("Alarm sent successfully")
        else:
            print(f"Failed to send alarm. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error while sending alarm: {e}")


if __name__ == "__main__":
    while True:
        if check_memory_usage():
            send_alarm()
        time.sleep(5)  # Проверка каждую минуту
