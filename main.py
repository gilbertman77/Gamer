	# Simple Pygame Program

  ## HOMEWORK
  # 0) Get this file from Github (gilbertman77/Gamer)
  # 1) Fix X bounce
  # 2) Condense if statements for bouncing
  # 3) Make bounce slight random angle
  # 4) Setup Pi and run the SH for adaptive cruise

	# Import and initialize the pygame library
import pygame
pygame.init()

scnHeight = 500
scnWidth = 500
	# Set up the drawing window
screen = pygame.display.set_mode([scnWidth, scnHeight])


xPos = 100
yPos = 200
YELLOW = (255, 255, 0)
position = [100, 200]

	# Run until user asks to quit
running = True
xVel = .5
yVel = xVel

	# -------- Main Program Loop -----------
while running:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
		
  # Fill the backgroung with yellow
  screen.fill(YELLOW)

  # Draw a solid blue circle in the center    
  #pygame.draw.circle(screen, (0, 0, 255), (xPos, yPos), 10)
  pygame.draw.circle(screen, (0, 0, 255), position, 10)

  if position[1] >= scnHeight:
    yVel = yVel * -1
  elif position[1] <= 0:
    yVel = yVel * -1

  position[1] = position[1] + yVel
  #print(position[1], position[0])
  
  # Flip the display
  pygame.display.flip()
	 
# Close the window and quit.
pygame.quit()