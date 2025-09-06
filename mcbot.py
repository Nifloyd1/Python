import pyautogui
import time
import keyboard

# ----------- HELPER: Run this separately to get coords ----------
# Move your mouse over the "Save and Quit to Title" button in Minecraft,
# then run this small snippet once to print coordinates, then exit.
# Uncomment to use.
#
# print("Move your mouse to the 'Save and Quit to Title' button now.")
# time.sleep(5)
# print(f"Mouse position recorded: {pyautogui.position()}")
# exit()
# ---------------------------------------------------------------

time.sleep(5)

# --------------------- Config --------------------------
center_x, center_y = 957, 534
scan_radius = 5
scan_step = 1

idle_crosshair_color = (230, 230, 230)  # Sample this manually
tolerance = 8

# Hunger detection
hx, hy = 1240, 929
lowh_color = (40, 40, 40)
hunger_tolerance = 20

# Auto quit if we run out of food
max_failed_eat_attempts = 3
failed_eat_attempts = 0

# --------------------- Helpers --------------------------
def color_matches(c1, c2, tolerance=10):
    return all(abs(c1[i] - c2[i]) <= tolerance for i in range(3))

def scan_area_for_non_idle(cx, cy, idle_color, tolerance, radius, step=1):
    for dx in range(-radius, radius + 1, step):
        for dy in range(-radius, radius + 1, step):
            try:
                pixel = pyautogui.pixel(cx + dx, cy + dy)
                if not color_matches(pixel, idle_color, tolerance):
                    return True
            except:
                pass
    return False

# --------------------- Auto Quit --------------------------
def auto_quit():
    print("⚠️ Out of food. Quitting to avoid death...")

    pyautogui.press('esc')             # Open pause menu
    time.sleep(1)
    pyautogui.moveTo(430, 680)         
    time.sleep(0.3)
    pyautogui.click()                  # Click "Save and Quit to Title"
    time.sleep(2)

    exit()

# ---------------------------- MAIN LOOP ----------------------------
while True:
    # Attack check
    if scan_area_for_non_idle(center_x, center_y, idle_crosshair_color, tolerance, scan_radius, scan_step):
        for _ in range(3):
            pyautogui.click(button='left')
            time.sleep(0.01)

    # Hunger check
    hunger_pixel = pyautogui.pixel(hx, hy)
    if color_matches(hunger_pixel, lowh_color, hunger_tolerance):
        print("⚠️ Low hunger! Trying to eat...")
        pyautogui.press('9')                    # switch to food
        pyautogui.mouseDown(button='right')     # try to eat
        time.sleep(2)
        pyautogui.mouseUp(button='right')
        pyautogui.press('1')                    # switch back

        # Check if hunger still low after eating
        time.sleep(0.5)
        hunger_pixel = pyautogui.pixel(hx, hy)
        if color_matches(hunger_pixel, lowh_color, hunger_tolerance):
            failed_eat_attempts += 1
            print(f"❌ Still hungry. Failed attempts: {failed_eat_attempts}")
        else:
            failed_eat_attempts = 0  # Reset if eating succeeded

        if failed_eat_attempts >= max_failed_eat_attempts:
            auto_quit()

    if keyboard.is_pressed("p"):
        break

    time.sleep(0.05)
