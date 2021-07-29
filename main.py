	# Simple Pygame Program

	# Import and initialize the pygame library
import pygame
pygame.init()

	# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

	# Run until user asks to quit
running = True

height = .1 
	# -------- Main Program Loop -----------
while running:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
		
  # Fill the backgroung with white
  screen.fill((255, 0, 0))

  # Draw a solid blue circle in the center    
  pygame.draw.circle(screen, (0, 0, 255), (xPos, yPos), 10)

  # Flip the display
  pygame.display.flip()
	 
# Close the window and quit.
pygame.quit()