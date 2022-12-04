import pyautogui,time
l1 = []
print("Paste the code here")
while(True):
	str = input("")

	if str.startswith("    "):
		str = str.replace("    ","")
	if str == "exit":
		break
	l1.append(str)
		
time.sleep(300)
for i in l1:
	pyautogui.typewrite(i)
	pyautogui.press("enter")
