import pygame, sys, random, math
from Bird import Bird
import functionality

pygame.init()
pygame.font.init()
score_font = pygame.font.SysFont('arial', 30)
final_font = pygame.font.SysFont('arial', 70)

clock = pygame.time.Clock()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# SETTINGS

is_running = True
game_state = True
game_speed = 1400
create_pipe_timer = 200 # TIMER 5 seconds

# VARIBLES
player = Bird(screen, 100, SCREEN_HEIGHT/2, 10, (255, 255, 255))
pipes = []
score = 0
highscore = 0


while is_running:
	screen.fill((25, 25, 25))
	create_pipe_timer -= 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.jump()

			if event.key == pygame.K_SPACE and not game_state:
				score = 0
				pipes = []
				player.vel = -1.5
				player.posY = SCREEN_HEIGHT/2
				game_state = True

# ===========================================================

	if game_state:
		score += 0.001
		if functionality.floor_collision(player, SCREEN_HEIGHT):
			game_state = False

		if functionality.pipe_collision(player, pipes):
			game_state = False

		functionality.top_collision(player)

		player.update()

		score_text = score_font.render(f'Score: {math.floor(score)}', False, (255, 255, 255))
		screen.blit(score_text, (10, 10))


		#[CREATE PIPE]
		if create_pipe_timer <= 0:
			functionality.create_pipe(screen, pipes, game_state, SCREEN_WIDTH, SCREEN_HEIGHT)
			create_pipe_timer = game_speed / 2

		#[UPDATE PIPE] 
		for pipe in pipes:
			pipe.update()

		#[DELETE PIPE]
		functionality.delete_pipe(pipes)

	else:
		if score > highscore:
			highscore = score

		# TEXT
		score_text = final_font.render(f'Score: {math.floor(score)}', False, (255, 255, 255))
		score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
		screen.blit(score_text, score_rect)

		highscore_text = final_font.render(f'Highscore: {math.floor(highscore)}', False, (255, 255, 255))
		highscore_rect = highscore_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
		screen.blit(highscore_text, highscore_rect)



	pygame.display.flip()
	clock.tick(game_speed)

