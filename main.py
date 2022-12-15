import pyautogui,time
l1 = []

print("Paste the code here")
while(True):
	str = input("")

	while(str.startswith("\t") or str.startswith("  ")):
		str = str.replace("\t","")
		str = str.replace("  ","")


	if str == "exit":
		break
	if '<' in str:
		str1,str2= str.split("<")
		l1.append(str1)
		l1.append('<')
		l1.append(str2)
		boo =0
	else:
		l1.append(str)
		
time.sleep(5)
for j,i in enumerate(l1):
	if i =='<':
		pyautogui.keyDown("<")
		time.sleep(0.59)
		pyautogui.keyUp("<")
		pyautogui.press("left")
		pyautogui.press("backspace")
		pyautogui.press("right")

	else:
		if l1[j+1]=='<':
			pyautogui.typewrite(i)
		else:
			pyautogui.typewrite(i)
			pyautogui.press("enter")
