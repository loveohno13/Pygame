

CATONKEYBOARD = USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad Cat!")
pygame.event.post(my_event)


for event in pygame.event.get():
	if event.type == CATONKEYBOARD:
		print (event.message)